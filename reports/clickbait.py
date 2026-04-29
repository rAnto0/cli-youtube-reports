from reports.base import BaseReport


class ClickbaitReport(BaseReport):
    def generate(self, rows: list[dict[str, str]]) -> list[dict[str, str]]:
        result: list[dict[str, str]] = [
            {
                "title": row["title"],
                "ctr": row["ctr"],
                "retention_rate": row["retention_rate"],
            }
            for row in rows
            if float(row["ctr"]) > 15 and float(row["retention_rate"]) < 40
        ]

        result.sort(key=lambda row: float(row["ctr"]), reverse=True)

        return result
