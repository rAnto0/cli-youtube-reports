from pathlib import Path

import pytest

from reader import read_files


def test_read_single_file(tmp_path: Path, csv_content: str) -> None:
    file = tmp_path / "stats.csv"
    file.write_text(csv_content, encoding="utf-8")

    rows = read_files([str(file)])

    assert len(rows) == 2
    assert rows[0]["title"] == "Video 1"


def test_read_multiple_files(tmp_path: Path, csv_content: str) -> None:
    file1 = tmp_path / "stats1.csv"
    file2 = tmp_path / "stats2.csv"

    file1.write_text(csv_content, encoding="utf-8")
    file2.write_text(csv_content, encoding="utf-8")

    rows = read_files([str(file1), str(file2)])

    assert len(rows) == 4


def test_read_missing_file() -> None:
    with pytest.raises(FileNotFoundError):
        read_files(["missing.csv"])
