"""
report_tool — a small tool for parsing, analysing, and saving numeric reports.

Public API:
    from report_tool import parse_numbers
    from report_tool import analyze_numbers
    from report_tool import build_report
    from report_tool import build_sorted_report
    from report_tool import save_report
    from report_tool import read_back
"""

from report_tool.analyzer import parse_numbers, analyze_numbers
from report_tool.formatter import build_report, build_sorted_report
from report_tool.storage import save_report, read_back

__all__ = [
    "parse_numbers",
    "analyze_numbers",
    "build_report",
    "build_sorted_report",
    "save_report",
    "read_back",
]
