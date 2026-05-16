"""Unit tests for async_tool.core.process_item."""

import pytest

from async_tool.core import TaskItem, process_item


@pytest.mark.asyncio
async def test_success_returns_done_status() -> None:
    item: TaskItem = {"id": 1, "delay": 0, "good": True}
    result = await process_item(item)
    assert result == {"id": 1, "status": "done"}


@pytest.mark.asyncio
async def test_failure_raises_value_error() -> None:
    item: TaskItem = {"id": 2, "delay": 0, "good": False}
    with pytest.raises(ValueError, match="Task 2 failed"):
        await process_item(item)


@pytest.mark.asyncio
async def test_result_structure() -> None:
    item: TaskItem = {"id": 42, "delay": 0, "good": True}
    result = await process_item(item)
    assert set(result.keys()) == {"id", "status"}
    assert result["id"] == 42
    assert result["status"] == "done"


@pytest.mark.asyncio
@pytest.mark.parametrize("task_id", [1, 7, 100, 12345])
async def test_id_is_preserved(task_id: int) -> None:
    item: TaskItem = {"id": task_id, "delay": 0, "good": True}
    result = await process_item(item)
    assert result["id"] == task_id


@pytest.mark.asyncio
async def test_delay_does_not_break_success() -> None:
    item: TaskItem = {"id": 1, "delay": 0.05, "good": True}
    result = await process_item(item)
    assert result["status"] == "done"


@pytest.mark.asyncio
async def test_failure_message_mentions_task_id() -> None:
    item: TaskItem = {"id": 99, "delay": 0, "good": False}
    with pytest.raises(ValueError) as exc_info:
        await process_item(item)
    assert "99" in str(exc_info.value)
