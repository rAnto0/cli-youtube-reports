from reports import REPORTS
from reports.clickbait import ClickbaitReport

clickbait = ClickbaitReport()


def test_filters_clickbait_videos(rows: list[dict[str, str]]) -> None:
    result = clickbait.generate(rows)
    titles = [row["title"] for row in result]

    assert len(result) == 2
    assert "Video 1" in titles
    assert "Video 2" in titles


def test_boundary_values_not_included(rows: list[dict[str, str]]) -> None:
    result = clickbait.generate(rows)
    titles = [row["title"] for row in result]

    assert "Video 5" not in titles
    assert "Video 6" not in titles


def test_sorted_by_ctr_descending(rows: list[dict[str, str]]) -> None:
    result = clickbait.generate(rows)

    assert result[0]["title"] == "Video 1"
    assert result[1]["title"] == "Video 2"


def test_only_required_columns(rows: list[dict[str, str]]) -> None:
    result = clickbait.generate(rows)

    for row in result:
        assert set(row.keys()) == {"title", "ctr", "retention_rate"}


def test_empty_input() -> None:
    result = clickbait.generate([])

    assert result == []


def test_clickbait_in_registry() -> None:
    assert "clickbait" in REPORTS
