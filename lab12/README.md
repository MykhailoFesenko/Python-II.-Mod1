# async_tool — tests

Automated tests for the `async_tool` CLI built in lab 11.

## What it tests

- **Unit tests** for the async `process_item` coroutine (called directly)
- **Behavior / black-box tests** for the CLI tool (invoked via `subprocess`)
- All three execution modes (`sync`, `async`, `limited`)
- Error handling with and without `--continue-on-error`
- Output structure: valid JSON, correct count, preserved order

## Project structure

```
lab12/
├── README.md
├── requirements.txt
├── pytest.ini             ← pytest config: pythonpath = src
├── mypy.ini               ← mypy config: strict, mypy_path = src
├── src/
│   └── async_tool/        ← unchanged copy of the tool from lab 11
│       ├── __init__.py
│       ├── __main__.py
│       ├── cli.py
│       ├── core.py
│       └── loader.py
├── tests/
│   ├── test_process_item.py   ← unit tests (async)
│   └── test_cli.py            ← behavior tests (subprocess)
└── report/
    └── answers.md
```

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate     # on Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## How to run

```bash
# all tests
pytest

# verbose
pytest -v

# only unit tests
pytest tests/test_process_item.py

# only CLI tests
pytest tests/test_cli.py

# strict type check
mypy src/async_tool tests
```

## What is covered

### Unit tests (`test_process_item.py`)

| Test | Checks |
|---|---|
| `test_success_returns_done_status` | valid input returns `{"id": ..., "status": "done"}` |
| `test_failure_raises_value_error` | `good: false` raises `ValueError` with the expected message |
| `test_result_structure` | return value has exactly `id` and `status` keys |
| `test_id_is_preserved` (parametrized) | id is echoed back unchanged for several values |
| `test_delay_does_not_break_success` | a small non-zero delay still succeeds |
| `test_failure_message_mentions_task_id` | error message contains the failing task id |

### Behavior tests (`test_cli.py`)

| Test | Checks |
|---|---|
| `test_basic_execution_exits_with_zero` | exit code 0 on valid input |
| `test_output_is_valid_json` | stdout is a JSON array |
| `test_mode_completes_successfully` (parametrized over `sync`/`async`/`limited`) | each mode runs to completion |
| `test_limited_mode_respects_limit_option` | `--limit N` works as a CLI option |
| `test_error_without_flag_fails` (parametrized) | failing task → non-zero exit in every mode |
| `test_error_with_flag_does_not_crash` | `--continue-on-error` → exit 0 |
| `test_error_with_flag_produces_error_status` | failed task appears with `status: "error"` |
| `test_error_result_contains_message` | error result has a `message` field with the cause |
| `test_output_count_matches_input` | output length = input length |
| `test_output_order_matches_input` | output ids in the same order as input ids |
| `test_each_result_has_required_keys` | every result has `id` and `status` |

## Test design

- **Direct call** for `process_item` — async unit tests via `pytest-asyncio`, no subprocess
- **subprocess.run** for CLI tests — `capture_output=True`, `text=True`, `timeout=30`
- **`tmp_path`** for input files — each test writes its own JSON, no shared state
- **`pytest.mark.parametrize`** for repetition across modes and task ids
- **No timing thresholds** — comparing wall-clock time across modes is intentionally avoided (it depends on the runner and is prone to flakiness)

## Requirements

- Python 3.11+
- `pytest`, `pytest-asyncio`
- `mypy` (for `--strict` type checking)
