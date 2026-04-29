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