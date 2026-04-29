import csv
from pathlib import Path


def read_files(paths: list[str]) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []

    for file_path in paths:
        path = Path(file_path)

        if not path.exists():
            raise FileNotFoundError(f"File not found: {file_path}")

        with path.open(newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            rows.extend(reader)

    return rows
