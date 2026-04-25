"""
storage.py — saving and reading report files.

Public functions:
    save_report(content, filename) — save a report string to a .txt file
    read_back(path)                — read the content of a saved report file

Examples:
    >>> from report_tool.storage import save_report, read_back
    >>> path = save_report("my report text", "output")
    >>> print(read_back(str(path)))
    my report text
"""

from pathlib import Path


def _resolve_output_path(filename: str) -> Path:
    """Return an absolute Path for the given filename (adds .txt if needed)."""
    p = Path(filename)
    if p.suffix == "":
        p = p.with_suffix(".txt")
    return p.resolve()


def save_report(content: str, filename: str) -> Path:
    """
    Save a report string to a text file.

    Args:
        content:  the text to write
        filename: target file path (without or with .txt extension)

    Returns:
        Path object pointing to the saved file
    """
    path = _resolve_output_path(filename)
    path.write_text(content, encoding="utf-8")
    return path


def read_back(path: str) -> str:
    """
    Read and return the content of a previously saved report file.

    Args:
        path: file path as string

    Returns:
        file contents as string

    Raises:
        FileNotFoundError: if the file does not exist
    """
    return Path(path).read_text(encoding="utf-8")


if __name__ == "__main__":
    import tempfile

    print("storage.py — saving and reading report files")
    print()
    print("Public functions:")
    print("  save_report(content, filename) — write report text to a .txt file")
    print("  read_back(path)                — read content of a saved report file")
    print()
    print("Example:")
    with tempfile.TemporaryDirectory() as tmp:
        _path = save_report("Example report content.", str(Path(tmp) / "demo"))
        print(f"  Saved to: {_path}")
        print(f"  Content:  {read_back(str(_path))!r}")
