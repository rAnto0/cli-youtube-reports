import pytest


@pytest.fixture
def csv_content() -> str:
    return """title,ctr,retention_rate,views
Video 1,18,35,1000
Video 2,22,28,2000
"""


@pytest.fixture
def rows() -> list[dict[str, str]]:
    return [
        {
            "title": "Video 1",
            "ctr": "20",
            "retention_rate": "30",
            "views": "1000",
            "likes": "100",
            "avg_watch_time": "4.2",
        },
        {
            "title": "Video 2",
            "ctr": "16",
            "retention_rate": "39",
            "views": "2000",
            "likes": "200",
            "avg_watch_time": "3.1",
        },
        {
            "title": "Video 3",
            "ctr": "10",
            "retention_rate": "30",
            "views": "3000",
            "likes": "300",
            "avg_watch_time": "5.0",
        },
        {
            "title": "Video 4",
            "ctr": "20",
            "retention_rate": "50",
            "views": "4000",
            "likes": "400",
            "avg_watch_time": "6.0",
        },
        {
            "title": "Video 5",
            "ctr": "15",
            "retention_rate": "30",
            "views": "5000",
            "likes": "500",
            "avg_watch_time": "7.0",
        },
        {
            "title": "Video 6",
            "ctr": "20",
            "retention_rate": "40",
            "views": "6000",
            "likes": "600",
            "avg_watch_time": "8.0",
        },
    ]
