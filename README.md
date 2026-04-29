# CLI YouTube Reports

CLI-приложение для анализа метрик YouTube-видео из CSV-файлов.

## Установка

Основные зависимости:
```bash
uv sync
```

Для разработки и тестов:
```bash
uv sync --extra dev
```

## Запуск

```bash
uv run python main.py --files data/stats1.csv data/stats2.csv --report clickbait
```

## Добавление нового отчёта

1. Создать файл `reports/your_report.py` и унаследоваться от `BaseReport`:

```python
from reports.base import BaseReport

class YourReport(BaseReport):
    def generate(self, rows: list[dict[str, str]]) -> list[dict[str, str]]:
        # логика фильтрации и сортировки
        ...
```

2. Зарегистрировать в `reports/__init__.py`:

```python
from reports.your_report import YourReport

REPORTS = {
    "clickbait": ClickbaitReport,
    "your_report": YourReport,
}
```

3. Запустить:
```bash
uv run python main.py --files data/stats1.csv --report your_report
```

## Пример вывода

### Успешная генерация отчета
![Результат](images/screenshot1.png)

### Ошибка: неизвестный тип отчёта
![Неизвестный тип отчёта](images/screenshot2.png)

### Ошибка: несуществующий файл
![Несуществующий файл](images/screenshot3.png)

## Тесты

```bash
uv run pytest
```

### Результаты тестов
![Результат тестов](images/screenshot4.png)