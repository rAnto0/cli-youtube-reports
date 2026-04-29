import argparse
import sys
from pathlib import Path

from tabulate import tabulate

from reader import read_files
from reports import REPORTS


def main() -> None:
    parser = argparse.ArgumentParser(description="YouTube video metrics reporter")

    parser.add_argument("--files", nargs="+", required=True, help="Paths to CSV files")
    parser.add_argument("--report", required=True, help="Report type (e.g. clickbait)")

    args = parser.parse_args()

    if args.report not in REPORTS:
        print(
            f"Unknown report: '{args.report}'. Available: {', '.join(REPORTS.keys())}"
        )
        sys.exit(1)

    for file_path in args.files:
        if not Path(file_path).exists():
            print(f"File not found: {file_path}")
            sys.exit(1)

    rows = read_files(args.files)
    report = REPORTS[args.report]()

    result = report.generate(rows)

    print(tabulate(result, headers="keys", tablefmt="outline"))


if __name__ == "__main__":
    main()
