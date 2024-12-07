FROM python:3.10-slim

WORKDIR /app

COPY . .

RUN mkdir -p /app/output

RUN pip install -r requirements.txt

CMD ["python", "main.py", "/app/logs/nginx.log", "Europe/Moscow", "/app/output/report.csv"]
