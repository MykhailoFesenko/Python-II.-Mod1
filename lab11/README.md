# async_tool

A CLI tool for processing a batch of tasks in different execution modes:
sequential, fully concurrent, and concurrency-limited.

## What it does

- Reads a JSON file with a list of tasks (`id`, `delay`, `good`)
- Runs each task via the provided `process_item` coroutine
- Supports three execution modes: `sync`, `async`, `limited`
- Prints a JSON array of results to stdout in the same order as the input
- Handles errors strictly (stop on first failure) or leniently (`--continue-on-error`)

## Project structure

```
lab11/
├── README.md
├── requirements.txt
├── input_example.json
├── src/
│   └── async_tool/
│       ├── __init__.py     ← public package API
│       ├── __main__.py     ← entry point (python -m async_tool)
│       ├── cli.py          ← argparse parser
│       ├── core.py         ← process_item + run_sync / run_async / run_limited
│       └── loader.py       ← load and validate input JSON
└── report/
    └── answers.md
```

## How to run

```bash
cd src
python -m async_tool ../input_example.json [OPTIONS]
```

### Examples

```bash
# default: sequential, stop on first failure
python -m async_tool ../input_example.json

# fully concurrent, do not stop on errors
python -m async_tool ../input_example.json --mode async --continue-on-error

# concurrency-limited (max 2 in flight), with INFO logs to stderr
python -m async_tool ../input_example.json --mode limited --limit 2 \
    --continue-on-error --log-level INFO
```

## CLI options

| Option | Values | Default | Description |
|---|---|---|---|
| `input` | path | — | path to input JSON file (positional) |
| `--mode` | `sync` / `async` / `limited` | `sync` | execution strategy |
| `--limit` | int | `5` | max concurrent tasks (only with `--mode limited`) |
| `--continue-on-error` | flag | off | do not stop on first failure; produce error results instead |
| `--log-level` | `DEBUG` / `INFO` / `WARNING` / `ERROR` | `WARNING` | logging level (logs go to stderr) |

## Input format

A JSON array of task objects:

```json
[
  {"id": 1, "delay": 1, "good": true},
  {"id": 2, "delay": 2, "good": false},
  {"id": 3, "delay": 1, "good": true}
]
```

- `id` — unique integer identifier
- `delay` — time in seconds the task waits (passed to `asyncio.sleep`)
- `good` — if `false`, the task raises a `ValueError`

## Output format

A JSON array printed to stdout, in input order:

```json
[
  {"id": 1, "status": "done"},
  {"id": 2, "status": "error", "message": "Task 2 failed"},
  {"id": 3, "status": "done"}
]
```

## Exit codes

- `0` — all tasks completed (or `--continue-on-error` swallowed the failures)
- `1` — a task failed and `--continue-on-error` was not set, or the input file was invalid

## Public API

| Function | Module | Description |
|---|---|---|
| `process_item(item)` | core | Provided coroutine — runs one task |
| `run_sync(items, *, continue_on_error)` | core | Sequential execution (`await` in a loop) |
| `run_async(items, *, continue_on_error)` | core | Full concurrency (`asyncio.gather`) |
| `run_limited(items, *, limit, continue_on_error)` | core | Bounded concurrency (`asyncio.Semaphore`) |
| `load_tasks(path)` | loader | Read and validate input JSON |

## Requirements

- Python 3.11+
- No external runtime dependencies
- `mypy` for the type check: `mypy --strict src/async_tool/`

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate     # on Windows: .venv\Scripts\activate
pip install -r requirements.txt

# run the type checker
cd src
mypy --strict async_tool/
```
