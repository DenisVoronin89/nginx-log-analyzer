# Nginx Log Analyzer

## Описание
Сервис анализирует логи Nginx и генерирует отчет со следующими метриками:
- Среднее время ответа
- Медианное время ответа
- Максимальное и минимальное время ответа
- Количество запросов

## Требования
- Python 3.10+
- Docker 

## Установка и запуск
### Локальный запуск:
1. Установите зависимости:

### Локальный запуск:
1. Установите зависимости:

   pip install -r requirements.txt

2. Для локального запуска без Docker используйте команду:

    python main.py

### Запуск с импользованием Docker:

1. Соберите Docker-образ:

   docker build -t nginx-log-analyzer .

2. Запустите контейнер:

   docker run -v /path/to/nginx/logs:/app/logs nginx-log-analyzer

### Тестирование:

Для запуска тестов используйте команду:

   python -m unittest discover -s tests

### CI/CD:

Проект настроен с использованием GitHub Actions для автоматического запуска линтеров, 
тестов и сборки Docker-образа при каждом пуше в ветку main или при создании пулл-реквеста.

### Лицензия:

Этот проект распространяется под лицензией MIT.
