"""
loader.py — input file loading and validation.

Public functions:
    load_tasks(path) — read a JSON file and return a list of validated TaskItem dicts
"""

import json
from pathlib import Path
from typing import cast

from async_tool.core import TaskItem


def _validate_task(raw: object, index: int) -> TaskItem:
    if not isinstance(raw, dict):
        raise ValueError(
            f"task #{index}: expected object, got {type(raw).__name__}"
        )
    for key in ("id", "delay", "good"):
        if key not in raw:
            raise ValueError(f"task #{index}: missing key {key!r}")

    if not isinstance(raw["id"], int) or isinstance(raw["id"], bool):
        raise ValueError(f"task #{index}: 'id' must be int")
    if not isinstance(raw["delay"], (int, float)) or isinstance(raw["delay"], bool):
        raise ValueError(f"task #{index}: 'delay' must be a number")
    if not isinstance(raw["good"], bool):
        raise ValueError(f"task #{index}: 'good' must be bool")

    return cast(TaskItem, raw)


def load_tasks(path: Path) -> list[TaskItem]:
    """Load tasks from a JSON file and validate their shape."""
    text = path.read_text(encoding="utf-8")
    data = json.loads(text)
    if not isinstance(data, list):
        raise ValueError("input file must contain a JSON array of tasks")
    return [_validate_task(raw, i) for i, raw in enumerate(data)]
