import sys
import os
from parsers.log_parser import LogParser
from analytics.stats_calculator import StatsCalculator
from output.csv_writer import CSVWriter


def main(log_file_path: str, timezone: str, output_file: str):
    log_file_path = os.path.abspath(log_file_path)
    output_file = os.path.abspath(output_file)

    print(f"Using log file path: {log_file_path}")
    print(f"Using output file path: {output_file}")

    # Проверка наличий лог файла
    if not os.path.exists(log_file_path):
        sys.exit(f"File not found: {log_file_path}")

    # Проверка наличия output папки
    output_dir = os.path.dirname(output_file)
    if not os.path.exists(output_dir):
        print(f"Output directory not found. Creating: {output_dir}")
        os.makedirs(output_dir)
    else:
        print(f"Output directory exists: {output_dir}")

    parser = LogParser(timezone)
    response_times = []

    try:
        print(f"Opening log file: {log_file_path}")
        with open(log_file_path, "r") as log_file:
            for line in log_file:
                try:
                    log_data = parser.parse_line(line)
                    response_times.append(log_data["response_time"])
                except ValueError as e:
                    print(f"Error parsing line: {line.strip()} - {e}")
    except FileNotFoundError:
        sys.exit(f"File not found: {log_file_path}")

    print(f"Parsed {len(response_times)} response times.")

    if response_times:
        print(
            f"Calculating statistics for {len(response_times)} response times."
        )
        stats = StatsCalculator.calculate(response_times)
        print(f"Writing statistics to CSV file: {output_file}")
        CSVWriter.write_to_csv(output_file, stats)
        print(f"Report saved to {output_file}")
    else:
        print("No response times found. Report not generated.")


if __name__ == "__main__":
    main("/app/logs/nginx.log", "Europe/Moscow", "/app/output/report.csv")
