"""
formatter.py — report formatting utilities.

Public functions:
    build_report(stats)               — format a statistics dict into a plain text report
    build_sorted_report(numbers, stats) — same as build_report, with an extra sorted-values line

Examples:
    >>> from report_tool.formatter import build_report
    >>> from report_tool.analyzer import parse_numbers, analyze_numbers
    >>> nums = parse_numbers("3, 1, 2")
    >>> print(build_report(analyze_numbers(nums)))
    Number Report
    --------------------
    count: 3
    ...
"""

from report_tool.analyzer import _sort_numbers


def _line_maker(name: str, value) -> str:
    """Format a single label-value line."""
    return f"{name}: {value}"


def _pretty_title(text: str) -> str:
    """Return text converted to title case."""
    return text.strip().title()


def _separator(width: int = 20) -> str:
    """Return a horizontal separator line."""
    return "-" * width


def build_report(stats: dict) -> str:
    """
    Format a statistics dict into a plain text report.

    Args:
        stats: dict with keys count, sum, min, max, mean (as returned by analyze_numbers)

    Returns:
        formatted multi-line string
    """
    lines = [
        _pretty_title("number report"),
        _separator(),
        _line_maker("count", stats["count"]),
        _line_maker("sum", stats["sum"]),
        _line_maker("min", stats["min"]),
        _line_maker("max", stats["max"]),
        _line_maker("mean", round(stats["mean"], 2)),
    ]
    return "\n".join(lines)


def build_sorted_report(numbers: list[float], stats: dict) -> str:
    """
    Format a report that includes a sorted listing of the input values.

    Args:
        numbers: original list of floats
        stats:   dict as returned by analyze_numbers

    Returns:
        formatted multi-line string
    """
    lines = [
        _pretty_title("number report"),
        _separator(),
        _line_maker("count", stats["count"]),
        _line_maker("sum", stats["sum"]),
        _line_maker("min", stats["min"]),
        _line_maker("max", stats["max"]),
        _line_maker("mean", round(stats["mean"], 2)),
        _line_maker("sorted", _sort_numbers(numbers)),
    ]
    return "\n".join(lines)


if __name__ == "__main__":
    from report_tool.analyzer import parse_numbers, analyze_numbers

    print("formatter.py — report formatting utilities")
    print()
    print("Public functions:")
    print("  build_report(stats)                 — format stats dict into text report")
    print("  build_sorted_report(numbers, stats) — same, with sorted values appended")
    print()
    print("Example:")
    _nums = parse_numbers("4, 8, 15, 16, 23, 42")
    _stats = analyze_numbers(_nums)
    print(build_sorted_report(_nums, _stats))
