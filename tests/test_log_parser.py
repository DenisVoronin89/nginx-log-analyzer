from datetime import datetime
import pytz
import unittest
from parsers.log_parser import LogParser


class TestLogParser(unittest.TestCase):

    def setUp(self):
        # Устанавливаем временную зону для теста
        self.parser = LogParser(timezone="Europe/Moscow")

    def test_parse_valid_log(self):
        # Пример корректной строки лога
        log_line = '192.168.1.1 - - [06/Dec/2024:13:00:00 +0300] "GET /index.html HTTP/1.1" 200 1234 0.320'

        # Ожидаемые данные
        expected_data = {
            "ip": "192.168.1.1",
            "datetime": datetime(
                2024, 12, 6, 13, 0, 0, tzinfo=pytz.timezone("Europe/Moscow")
            ),
            "status": "200",
            "response_time": 0.320,
        }

        # Парсим строку лога
        result = self.parser.parse_line(log_line)

        # Проверяем, что результат соответствует ожиданиям
        self.assertEqual(result["ip"], expected_data["ip"])
        self.assertEqual(result["status"], expected_data["status"])
        self.assertEqual(
            result["response_time"], expected_data["response_time"]
        )

        # Игнорируем временную зону при сравнении времени
        self.assertEqual(
            result["datetime"].replace(tzinfo=None),
            expected_data["datetime"].replace(tzinfo=None),
        )

    def test_parse_invalid_log(self):
        # Пример некорректной строки лога
        log_line = "Invalid log format"

        # Проверяем, что при парсинге некорректной строки возникает ValueError
        with self.assertRaises(ValueError):
            self.parser.parse_line(log_line)

    def test_convert_to_timezone(self):
        # Проверяем, что время корректно конвертируется в нужную временную зону
        naive_datetime = "06/Dec/2024:13:00:00 +0300"
        expected_datetime = datetime(
            2024, 12, 6, 13, 0, 0, tzinfo=pytz.timezone("Europe/Moscow")
        )

        # Проверяем, что конвертация времени правильная
        result = self.parser._convert_to_timezone(naive_datetime)

        # Игнорируем временную зону при сравнении
        self.assertEqual(
            result.replace(tzinfo=None), expected_datetime.replace(tzinfo=None)
        )


if __name__ == "__main__":
    unittest.main()
