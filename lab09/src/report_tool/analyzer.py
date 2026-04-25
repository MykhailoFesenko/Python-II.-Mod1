"""
analyzer.py — number parsing and statistical analysis.

Public functions:
    parse_numbers(text)    — parse a comma- or semicolon-separated string into a list of floats
    analyze_numbers(numbers) — compute basic statistics for a list of numbers

Examples:
    >>> from report_tool.analyzer import parse_numbers, analyze_numbers
    >>> nums = parse_numbers("4, 8, 15, 16, 23, 42")
    >>> stats = analyze_numbers(nums)
    >>> print(stats)
    {'count': 6, 'sum': 108, 'min': 4, 'max': 42, 'mean': 18.0}
"""


def _cleanup_pieces(parts: list[str]) -> list[str]:
    """Remove empty and whitespace-only entries from a list of strings."""
    return [item.strip() for item in parts if item.strip() != ""]


def _check_input(numbers: list[float]) -> None:
    """Raise ValueError if numbers list is empty."""
    if not numbers:
        raise ValueError("numbers must not be empty")


def _sort_numbers(numbers: list[float]) -> list[float]:
    """Return a sorted copy of the numbers list."""
    return sorted(numbers)


def parse_numbers(text: str) -> list[float]:
    """
    Parse a comma- or semicolon-separated string into a list of floats.

    Args:
        text: input string, e.g. "1, 2.5; 3"

    Returns:
        list of float values

    Raises:
        ValueError: if any token cannot be converted to float
    """
    pieces = text.replace(";", ",").split(",")
    pieces = _cleanup_pieces(pieces)
    return [float(p) for p in pieces]


def analyze_numbers(numbers: list[float]) -> dict:
    """
    Compute basic statistics for a list of numbers.

    Args:
        numbers: non-empty list of floats

    Returns:
        dict with keys: count, sum, min, max, mean

    Raises:
        ValueError: if numbers is empty
    """
    _check_input(numbers)
    total = sum(numbers)
    count = len(numbers)
    return {
        "count": count,
        "sum": total,
        "min": min(numbers),
        "max": max(numbers),
        "mean": total / count,
    }


if __name__ == "__main__":
    print("analyzer.py — number parsing and statistical analysis")
    print()
    print("Public functions:")
    print("  parse_numbers(text)      — parse comma/semicolon-separated string")
    print("  analyze_numbers(numbers) — compute count, sum, min, max, mean")
    print()
    print("Example:")
    _sample = parse_numbers("4, 8, 15, 16, 23, 42")
    _stats = analyze_numbers(_sample)
    print(f"  Input:  '4, 8, 15, 16, 23, 42'")
    print(f"  Parsed: {_sample}")
    print(f"  Stats:  {_stats}")
