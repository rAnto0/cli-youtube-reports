from pathlib import Path
from unittest.mock import patch

import pytest

from main import main


def test_unknown_report(capsys: pytest.CaptureFixture) -> None:
    with patch(
        "sys.argv", ["main.py", "--files", "data/example.csv", "--report", "vlad"]
    ):
        with pytest.raises(SystemExit) as exc:
            main()

    assert exc.value.code == 1
    assert "Unknown report" in capsys.readouterr().out


def test_missing_file(capsys: pytest.CaptureFixture) -> None:
    with patch(
        "sys.argv", ["main.py", "--files", "missing.csv", "--report", "clickbait"]
    ):
        with pytest.raises(SystemExit) as exc:
            main()

    assert exc.value.code == 1
    assert "File not found" in capsys.readouterr().out


def test_successful_run(
    capsys: pytest.CaptureFixture, tmp_path: Path, csv_content: str
) -> None:
    csv_file = tmp_path / "stats.csv"
    csv_file.write_text(
        csv_content,
        encoding="utf-8",
    )

    with patch(
        "sys.argv", ["main.py", "--files", str(csv_file), "--report", "clickbait"]
    ):
        main()

    output = capsys.readouterr().out
    assert "Video 1" in output
    assert "Video 3" not in output
    assert "ctr" in output
    assert "retention_rate" in output
