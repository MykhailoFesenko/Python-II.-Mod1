"""
cli.py — command-line argument parsing.
"""

import argparse
from pathlib import Path


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="async_tool",
        description="Process a batch of tasks in sync / async / limited mode.",
    )
    parser.add_argument(
        "input",
        type=Path,
        help="path to input JSON file",
    )
    parser.add_argument(
        "--mode",
        choices=("sync", "async", "limited"),
        default="sync",
        help="execution mode (default: sync)",
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=5,
        help="max concurrent tasks for --mode limited (default: 5)",
    )
    parser.add_argument(
        "--continue-on-error",
        action="store_true",
        help="do not stop on first failure; produce error results instead",
    )
    parser.add_argument(
        "--log-level",
        choices=("DEBUG", "INFO", "WARNING", "ERROR"),
        default="WARNING",
        help="logging level (default: WARNING)",
    )
    return parser
