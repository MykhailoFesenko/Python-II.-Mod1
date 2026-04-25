# report_tool

A small Python tool for parsing, analysing, and saving numeric reports.

## What it does

- Parses a comma- or semicolon-separated string of numbers
- Computes basic statistics (count, sum, min, max, mean)
- Formats a readable plain-text report
- Saves the report to a file and reads it back

## Project structure

```
lab09/
├── README.md
├── requirements.txt
├── src/
│   └── report_tool/
│       ├── __init__.py     ← public package API
│       ├── __main__.py     ← entry point (python -m report_tool)
│       ├── analyzer.py     ← parse_numbers, analyze_numbers
│       ├── formatter.py    ← build_report, build_sorted_report
│       └── storage.py      ← save_report, read_back
└── report/
    └── report.md
```

## How to run

### As a package

```bash
cd src
python -m report_tool
```

Prints a description of the tool, its public API, and a live example.

### Individual modules

```bash
cd src
python -m report_tool.analyzer
python -m report_tool.formatter
python -m report_tool.storage
```

Each module prints its purpose, public functions, and a usage example.

## How to use (import)

```python
from report_tool import parse_numbers, analyze_numbers, build_report, save_report, read_back

numbers = parse_numbers("4, 8, 15, 16, 23, 42")
stats   = analyze_numbers(numbers)
report  = build_report(stats)
print(report)

path = save_report(report, "my_report")
print(read_back(str(path)))
```

## Public API

| Function | Module | Description |
|---|---|---|
| `parse_numbers(text)` | analyzer | Parse string → list of floats |
| `analyze_numbers(numbers)` | analyzer | Compute count, sum, min, max, mean |
| `build_report(stats)` | formatter | Format stats dict → text report |
| `build_sorted_report(numbers, stats)` | formatter | Same + sorted values line |
| `save_report(content, filename)` | storage | Write report to .txt file |
| `read_back(path)` | storage | Read a saved report file |

## Requirements

No external dependencies. Requires Python 3.10+.
