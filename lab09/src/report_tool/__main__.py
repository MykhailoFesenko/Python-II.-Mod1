"""
Entry point for: python -m report_tool
"""

from report_tool import (
    parse_numbers,
    analyze_numbers,
    build_sorted_report,
    save_report,
    read_back,
)


def _show_info() -> None:
    print("=" * 40)
    print("report_tool — numeric report generator")
    print("=" * 40)
    print()
    print("Description:")
    print("  Parses a string of numbers, computes basic statistics,")
    print("  formats a readable report, and optionally saves it to a file.")
    print()
    print("Public API (importable from report_tool):")
    print("  parse_numbers(text)                  — parse comma/semicolon string to floats")
    print("  analyze_numbers(numbers)             — compute count, sum, min, max, mean")
    print("  build_report(stats)                  — format stats into a text report")
    print("  build_sorted_report(numbers, stats)  — same, with sorted values")
    print("  save_report(content, filename)       — save report to a .txt file")
    print("  read_back(path)                      — read a saved report file")
    print()
    print("Usage example:")
    print("  from report_tool import parse_numbers, analyze_numbers, build_report")
    print("  nums  = parse_numbers('4, 8, 15, 16, 23, 42')")
    print("  stats = analyze_numbers(nums)")
    print("  print(build_report(stats))")
    print()


def _run_example() -> None:
    text = "4, 8, 15, 16, 23, 42"
    numbers = parse_numbers(text)
    stats = analyze_numbers(numbers)
    report = build_sorted_report(numbers, stats)

    print("--- Example output ---")
    print(f"Input: {text!r}")
    print()
    print(report)
    print()

    path = save_report(report, "report_output")
    print(f"Saved to: {path}")
    print()
    print("File content:")
    print(read_back(str(path)))


if __name__ == "__main__":
    _show_info()
    _run_example()
