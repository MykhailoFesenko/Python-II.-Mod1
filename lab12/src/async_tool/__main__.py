"""
Entry point for: python -m async_tool input.json [OPTIONS]
"""

import asyncio
import json
import logging
import sys
from pathlib import Path

from async_tool.cli import build_parser
from async_tool.core import (
    TaskResult,
    run_async,
    run_limited,
    run_sync,
)
from async_tool.loader import load_tasks


def main() -> int:
    args = build_parser().parse_args()

    input_path: Path = args.input
    mode: str = args.mode
    limit: int = args.limit
    continue_on_error: bool = args.continue_on_error
    log_level: str = args.log_level

    logging.basicConfig(
        level=log_level,
        format="%(levelname)s %(name)s: %(message)s",
        stream=sys.stderr,
    )

    try:
        items = load_tasks(input_path)
        results: list[TaskResult]
        if mode == "sync":
            results = asyncio.run(
                run_sync(items, continue_on_error=continue_on_error)
            )
        elif mode == "async":
            results = asyncio.run(
                run_async(items, continue_on_error=continue_on_error)
            )
        else:
            results = asyncio.run(
                run_limited(
                    items, limit=limit, continue_on_error=continue_on_error
                )
            )
    except Exception as exc:
        logging.error("processing failed: %s", exc)
        return 1

    json.dump(results, sys.stdout, ensure_ascii=False)
    sys.stdout.write("\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
