import sys
import os
import gzip
import logging
from parsers.log_parser import LogParser
from analytics.stats_calculator import StatsCalculator
from output.log_writer import LogWriter


def setup_logging():
    """
    Настройка логирования.
    """
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
    )


def main(log_file_path: str, timezone: str, output_file: str):
    setup_logging()

    log_file_path = os.path.abspath(log_file_path)
    output_file = os.path.abspath(output_file)

    logging.info(f"Using log file path: {log_file_path}")
    logging.info(f"Using output file path: {output_file}")

    # Проверка наличия отчета
    if os.path.exists(output_file):
        logging.info(
            f"Report already exists at: {output_file}. Skipping processing."
        )
        return

    # Проверка лог-файла
    if not os.path.exists(log_file_path):
        logging.error(f"File not found: {log_file_path}")
        sys.exit(1)

    # Создание папки для отчета
    output_dir = os.path.dirname(output_file)
    if not os.path.exists(output_dir):
        logging.info(f"Output directory not found. Creating: {output_dir}")
        os.makedirs(output_dir)

    parser = LogParser(timezone)
    response_times = []
    urls = []

    try:
        logging.info(f"Opening log file: {log_file_path}")
        open_func = gzip.open if log_file_path.endswith(".gz") else open
        with open_func(log_file_path, "rt") as log_file:
            for line in log_file:
                try:
                    log_data = parser.parse_line(line)
                    response_times.append(log_data["response_time"])
                    urls.append(log_data["url"])  # Добавляем URL
                except ValueError as e:
                    logging.warning(
                        f"Error parsing line: {line.strip()} - {e}"
                    )
    except FileNotFoundError:
        logging.error(f"File not found: {log_file_path}")
        sys.exit(1)

    logging.info(f"Parsed {len(response_times)} response times.")

    if response_times:
        logging.info(
            f"Calculating statistics for {len(response_times)} response times."
        )
        stats = StatsCalculator.calculate(urls, response_times)
        logging.info(f"Writing statistics to HTML file: {output_file}")
        LogWriter.write_to_html(output_file, stats)
        logging.info(f"Report saved to {output_file}")
    else:
        logging.info("No response times found. Report not generated.")


if __name__ == "__main__":
    main("logs/nginx.log", "Europe/Moscow", "logs/report.html")
