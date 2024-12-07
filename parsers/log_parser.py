import re
from datetime import datetime
import pytz


class LogParser:
    """
    Класс для парсинга логов Nginx.
    """

    # регулярное выражение
    LOG_PATTERN = r'(?P<ip>\S+) \S+ \S+ \[(?P<datetime>[^\]]+)\] "\S+ \S+ \S+" (?P<status>\d{3}) \S+ (?P<response_time>\d+\.\d+)'

    def __init__(self, timezone: str = "UTC"):
        self.timezone = pytz.timezone(timezone)

    def parse_line(self, line: str):
        """
        Парсинг строки лога.
        """
        match = re.match(self.LOG_PATTERN, line)
        if not match:
            raise ValueError("Invalid log format")

        data = match.groupdict()
        data["datetime"] = self._convert_to_timezone(data["datetime"])
        data["response_time"] = float(data["response_time"])
        return data

    def _convert_to_timezone(self, log_datetime: str):
        """
        Конвертация времени из строки в datetime с учетом временной зоны.
        """
        naive_datetime = datetime.strptime(
            log_datetime, "%d/%b/%Y:%H:%M:%S %z"
        )
        return naive_datetime.astimezone(self.timezone)
