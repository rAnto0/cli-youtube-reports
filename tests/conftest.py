import pytest


@pytest.fixture
def csv_content() -> str:
    return """title,ctr,retention_rate,views
Video 1,18,35,1000
Video 2,22,28,2000
"""
