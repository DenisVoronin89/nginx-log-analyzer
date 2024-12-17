import re
from datetime import datetime
from typing import Dict
import pytz


class LogParser:
    """
    Парсинг логов Nginx с учетом временной зоны.
    """

    # Регулярное выражение для извлечения IP, времени, статуса, времени отклика и URL
    LOG_PATTERN = re.compile(
        r"(?P<ip>\S+) \S+ \S+ "
        r"\[(?P<datetime>[^\]]+)\] "
        r'"\S+ (?P<url>\S+) \S+" '
        r"(?P<status>\d{3}) \S+ (?P<response_time>\d+\.\d+)"
    )

    def __init__(self, timezone: str = "UTC"):
        """
        Инициализация парсера.
        """
        self.timezone = pytz.timezone(timezone)

    def parse_line(self, line: str) -> Dict[str, float | str | datetime]:
        """
        Парсинг строки лога.
        """
        match = self.LOG_PATTERN.match(line)
        if not match:
            raise ValueError(f"Invalid log format: {line.strip()}")

        data = match.groupdict()
        data["datetime"] = self._convert_to_timezone(data["datetime"])
        data["response_time"] = float(data["response_time"])
        return data

    def _convert_to_timezone(self, log_datetime: str) -> datetime:
        """
        Конвертация времени лога в целевую временную зону.
        """
        naive_datetime = datetime.strptime(
            log_datetime, "%d/%b/%Y:%H:%M:%S %z"
        )
        return naive_datetime.astimezone(self.timezone)
