"""
core.py — task processing engine.

Provides the (unmodifiable) `process_item` coroutine and three execution
strategies for a batch of tasks: sequential, fully concurrent, and
concurrency-limited via a semaphore.

Public functions:
    run_sync(items, *, continue_on_error)
    run_async(items, *, continue_on_error)
    run_limited(items, *, limit, continue_on_error)
"""

import asyncio
import logging
from collections.abc import Awaitable, Callable
from typing import TypedDict


logger = logging.getLogger(__name__)


class TaskItem(TypedDict):
    id: int
    delay: float
    good: bool


class TaskResult(TypedDict, total=False):
    id: int
    status: str
    message: str


Runner = Callable[[TaskItem], Awaitable[TaskResult]]


async def process_item(item: TaskItem) -> TaskResult:
    """Provided function — DO NOT MODIFY."""
    await asyncio.sleep(item["delay"])
    if not item["good"]:
        raise ValueError(f"Task {item['id']} failed")
    return {
        "id": item["id"],
        "status": "done",
    }


async def _run_one(item: TaskItem) -> TaskResult:
    """Run a single task with start/done logging."""
    logger.info("task %d started", item["id"])
    result = await process_item(item)
    logger.info("task %d done", item["id"])
    return result


async def _safe_run(item: TaskItem) -> TaskResult:
    """Run a task, converting any exception into an error result."""
    try:
        return await _run_one(item)
    except Exception as exc:
        logger.warning("task %d failed: %s", item["id"], exc)
        return {"id": item["id"], "status": "error", "message": str(exc)}


def _pick_runner(continue_on_error: bool) -> Runner:
    return _safe_run if continue_on_error else _run_one


async def run_sync(
    items: list[TaskItem], *, continue_on_error: bool
) -> list[TaskResult]:
    """Process tasks one by one (sequential)."""
    runner = _pick_runner(continue_on_error)
    results: list[TaskResult] = []
    for item in items:
        results.append(await runner(item))
    return results


async def run_async(
    items: list[TaskItem], *, continue_on_error: bool
) -> list[TaskResult]:
    """Process all tasks concurrently via asyncio.gather."""
    runner = _pick_runner(continue_on_error)
    return list(await asyncio.gather(*(runner(item) for item in items)))


async def run_limited(
    items: list[TaskItem], *, limit: int, continue_on_error: bool
) -> list[TaskResult]:
    """Process tasks concurrently with a semaphore-bounded limit."""
    if limit < 1:
        raise ValueError(f"limit must be >= 1, got {limit}")

    semaphore = asyncio.Semaphore(limit)
    runner = _pick_runner(continue_on_error)

    async def _bounded(item: TaskItem) -> TaskResult:
        async with semaphore:
            return await runner(item)

    return list(await asyncio.gather(*(_bounded(item) for item in items)))
