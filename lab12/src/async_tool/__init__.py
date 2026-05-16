"""
async_tool — process a batch of tasks in sync / async / limited modes.

Public API:
    from async_tool import TaskItem, TaskResult
    from async_tool import run_sync, run_async, run_limited
    from async_tool import load_tasks
"""

from async_tool.core import (
    TaskItem,
    TaskResult,
    process_item,
    run_async,
    run_limited,
    run_sync,
)
from async_tool.loader import load_tasks

__all__ = [
    "TaskItem",
    "TaskResult",
    "process_item",
    "run_sync",
    "run_async",
    "run_limited",
    "load_tasks",
]
