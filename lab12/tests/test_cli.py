"""Behavior / black-box tests for the async_tool CLI."""

import json
import subprocess
import sys
from pathlib import Path
from typing import Any

import pytest


SRC_DIR = Path(__file__).resolve().parent.parent / "src"


GOOD_TASKS: list[dict[str, Any]] = [
    {"id": 1, "delay": 0, "good": True},
    {"id": 2, "delay": 0, "good": True},
    {"id": 3, "delay": 0, "good": True},
]

MIXED_TASKS: list[dict[str, Any]] = [
    {"id": 1, "delay": 0, "good": True},
    {"id": 2, "delay": 0, "good": False},
    {"id": 3, "delay": 0, "good": True},
]


def write_tasks(tmp_path: Path, tasks: list[dict[str, Any]]) -> Path:
    path = tmp_path / "input.json"
    path.write_text(json.dumps(tasks), encoding="utf-8")
    return path


def run_cli(input_path: Path, *args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, "-m", "async_tool", str(input_path), *args],
        cwd=SRC_DIR,
        capture_output=True,
        text=True,
        timeout=30,
    )


# ---------- 1. Basic execution ----------

def test_basic_execution_exits_with_zero(tmp_path: Path) -> None:
    input_path = write_tasks(tmp_path, GOOD_TASKS)
    result = run_cli(input_path)
    assert result.returncode == 0


def test_output_is_valid_json(tmp_path: Path) -> None:
    input_path = write_tasks(tmp_path, GOOD_TASKS)
    result = run_cli(input_path)
    parsed = json.loads(result.stdout)
    assert isinstance(parsed, list)


# ---------- 2. Mode behavior ----------

@pytest.mark.parametrize("mode", ["sync", "async", "limited"])
def test_mode_completes_successfully(tmp_path: Path, mode: str) -> None:
    input_path = write_tasks(tmp_path, GOOD_TASKS)
    result = run_cli(input_path, "--mode", mode)
    assert result.returncode == 0
    parsed = json.loads(result.stdout)
    assert all(item["status"] == "done" for item in parsed)


def test_limited_mode_respects_limit_option(tmp_path: Path) -> None:
    input_path = write_tasks(tmp_path, GOOD_TASKS)
    result = run_cli(input_path, "--mode", "limited", "--limit", "2")
    assert result.returncode == 0
    parsed = json.loads(result.stdout)
    assert len(parsed) == 3


# ---------- 3. Error without flag ----------

@pytest.mark.parametrize("mode", ["sync", "async", "limited"])
def test_error_without_flag_fails(tmp_path: Path, mode: str) -> None:
    input_path = write_tasks(tmp_path, MIXED_TASKS)
    result = run_cli(input_path, "--mode", mode)
    assert result.returncode != 0


# ---------- 4. Error with flag ----------

def test_error_with_flag_does_not_crash(tmp_path: Path) -> None:
    input_path = write_tasks(tmp_path, MIXED_TASKS)
    result = run_cli(input_path, "--mode", "sync", "--continue-on-error")
    assert result.returncode == 0


def test_error_with_flag_produces_error_status(tmp_path: Path) -> None:
    input_path = write_tasks(tmp_path, MIXED_TASKS)
    result = run_cli(input_path, "--mode", "sync", "--continue-on-error")
    parsed = json.loads(result.stdout)
    statuses = {item["id"]: item["status"] for item in parsed}
    assert statuses == {1: "done", 2: "error", 3: "done"}


def test_error_result_contains_message(tmp_path: Path) -> None:
    input_path = write_tasks(tmp_path, MIXED_TASKS)
    result = run_cli(input_path, "--continue-on-error")
    parsed = json.loads(result.stdout)
    failed = next(item for item in parsed if item["id"] == 2)
    assert failed["status"] == "error"
    assert "message" in failed
    assert "Task 2 failed" in failed["message"]


# ---------- 5. Output structure ----------

def test_output_count_matches_input(tmp_path: Path) -> None:
    tasks = [{"id": i, "delay": 0, "good": True} for i in range(1, 11)]
    input_path = write_tasks(tmp_path, tasks)
    result = run_cli(input_path, "--mode", "async")
    parsed = json.loads(result.stdout)
    assert len(parsed) == len(tasks)


def test_output_order_matches_input(tmp_path: Path) -> None:
    tasks: list[dict[str, Any]] = [
        {"id": 5, "delay": 0, "good": True},
        {"id": 2, "delay": 0, "good": True},
        {"id": 9, "delay": 0, "good": True},
        {"id": 1, "delay": 0, "good": True},
    ]
    input_path = write_tasks(tmp_path, tasks)
    result = run_cli(input_path, "--mode", "async")
    parsed = json.loads(result.stdout)
    assert [item["id"] for item in parsed] == [5, 2, 9, 1]


def test_each_result_has_required_keys(tmp_path: Path) -> None:
    input_path = write_tasks(tmp_path, GOOD_TASKS)
    result = run_cli(input_path)
    parsed = json.loads(result.stdout)
    for item in parsed:
        assert "id" in item
        assert "status" in item
