# Lab 09 — Report

## 1. What was wrong in the original project

**Structure and naming:**
- No `__init__.py` — the directory was not a proper Python package.
- No `__main__.py` — `python -m report_tool` was impossible.
- Module names were vague and non-descriptive (`helpers.py`, `textstuff.py`, `saveit.py`).

**Imports:**
- `run.py` used bare imports (`from helpers import ...`) that only work when running from inside the package directory — they break as soon as the project is installed or run from anywhere else.

**Top-level executable code:**
- `helpers.py` ran a test on every import: `temp = demoData()` + `print(...)`.
- `textstuff.py` built a sample report on every import: `sample_text = build_report(...)`.
- `run.py` printed `"run.py loaded"` on import.
- These side effects make the modules unreliable to import.

**Public vs private API:**
- No distinction between public and internal functions: `cleanupPieces`, `checkInput`, `sortNumbers`, `lineMaker`, `prettyTitle`, `internalBanner`, `demoData` were all exposed with no underscore convention.
- Naming was inconsistent — a mix of `camelCase` and `snake_case`.

**Missing implementation:**
- `saveit.py` was completely empty, yet `run.py` imported `save_report` and `read_back` from it.

**Dependencies:**
- `requirements.txt` listed `requests`, `colorama`, `certifi`, `charset-normalizer`, `idna`, `urllib3` — none of which are used in the project.

**README:**
- Contained only three vague lines with no real instructions.

---

## 2. What was improved

- Modules were renamed to reflect their purpose: `analyzer.py`, `formatter.py`, `storage.py`.
- `__init__.py` was added to make the directory a proper package with a clean, explicit public API.
- `__main__.py` was added so the tool can be run with `python -m report_tool`.
- All imports were changed to absolute package imports (`from report_tool.analyzer import ...`).
- All top-level executable code was removed from modules; demo code was moved inside `if __name__ == "__main__"` blocks.
- Internal helper functions were renamed with a leading underscore: `_cleanup_pieces`, `_check_input`, `_sort_numbers`, `_line_maker`, `_pretty_title`, `_separator`.
- All function names were normalized to `snake_case`.
- `storage.py` was fully implemented with `save_report` and `read_back`.
- `requirements.txt` was cleaned — the project has no external dependencies.
- `README.md` was rewritten with structure explanation, run instructions, and usage examples.
- Each module was given a docstring and a standalone `__main__` block that describes its purpose and shows a live example.

---

## 3. Why these changes matter

**Readability:**
Module names like `analyzer`, `formatter`, and `storage` immediately tell a reader what each file is responsible for. Consistent `snake_case` naming and clear docstrings reduce the time needed to understand the code.

**Usability:**
Absolute imports mean the package works correctly regardless of where it is run from. The `__init__.py` public API lets users write `from report_tool import parse_numbers` without knowing the internal structure. The `__main__.py` entry point gives a clear, documented way to run the tool.

**Stability:**
Removing top-level side effects means importing any module is safe and predictable — it will never print to stdout or compute anything unintentionally. This is essential for testing and reuse.

**Maintainability:**
The underscore convention for internal functions signals clearly which parts of the code are implementation details and which are part of the public contract. This makes it safe to refactor internals without breaking callers.
