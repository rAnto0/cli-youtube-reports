from abc import ABC, abstractmethod


class BaseReport(ABC):
    @abstractmethod
    def generate(self, rows: list[dict[str, str]]) -> list[dict[str, str]]: ...
