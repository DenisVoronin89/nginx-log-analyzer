import pytest
from datetime import datetime
import pytz
from parsers.log_parser import LogParser  # Импорт из пакета parsers


@pytest.fixture
def log_parser():
    # Фикстура для создания экземпляра LogParser
    return LogParser(timezone="Europe/Moscow")


def test_parse_valid_log(log_parser):
    log_line = '192.168.1.1 - - [06/Dec/2024:13:00:00 +0300] "GET /index.html HTTP/1.1" 200 1234 0.320'

    expected_data = {
        "ip": "192.168.1.1",
        "datetime": datetime(
            2024, 12, 6, 13, 0, 0, tzinfo=pytz.FixedOffset(180)
        ),
        "status": "200",
        "response_time": 0.320,
    }

    result = log_parser.parse_line(log_line)

    assert result["ip"] == expected_data["ip"]
    assert result["status"] == expected_data["status"]
    assert abs(result["response_time"] - expected_data["response_time"]) < 1e-3
    assert result["datetime"].astimezone(pytz.utc) == expected_data[
        "datetime"
    ].astimezone(pytz.utc)


def test_parse_invalid_log(log_parser):
    log_line = "Invalid log format"
    with pytest.raises(ValueError, match="Invalid log format"):
        log_parser.parse_line(log_line)


def test_parse_partial_invalid_log(log_parser):
    log_line = '192.168.1.1 - - [06/Dec/2024:13:00:00] "GET /index.html HTTP/1.1" 200 1234'
    with pytest.raises(ValueError):
        log_parser.parse_line(log_line)


def test_timezone_conversion():
    parser = LogParser(timezone="UTC")
    log_datetime = "06/Dec/2024:13:00:00 +0300"
    expected_datetime = datetime(2024, 12, 6, 10, 0, 0, tzinfo=pytz.UTC)

    result = parser._convert_to_timezone(log_datetime)
    assert result == expected_datetime


def test_different_timezones():
    parser_moscow = LogParser(timezone="Europe/Moscow")
    parser_utc = LogParser(timezone="UTC")

    log_line = '192.168.1.1 - - [06/Dec/2024:13:00:00 +0300] "GET /index.html HTTP/1.1" 200 1234 0.320'

    result_moscow = parser_moscow.parse_line(log_line)
    result_utc = parser_utc.parse_line(log_line)

    expected_moscow = datetime(
        2024, 12, 6, 13, 0, 0, tzinfo=pytz.FixedOffset(180)
    )
    expected_utc = datetime(2024, 12, 6, 10, 0, 0, tzinfo=pytz.UTC)

    assert result_moscow["datetime"] == expected_moscow
    assert result_utc["datetime"] == expected_utc
