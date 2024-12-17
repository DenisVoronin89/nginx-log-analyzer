import unittest
import os
from output.log_writer import LogWriter  # Импорт из пакета output


class TestLogWriter(unittest.TestCase):

    def test_write_to_html(self):
        # Пример данных
        data = [
            {
                "url": "/index.html",
                "count": 10,
                "count_perc": 50,
                "time_avg": 0.320,
                "time_max": 0.59,
                "time_med": 0.31,
                "time_perc": 60,
                "time_sum": 3.2,
            },
            {
                "url": "/about.html",
                "count": 10,
                "count_perc": 50,
                "time_avg": 0.250,
                "time_max": 0.45,
                "time_med": 0.28,
                "time_perc": 40,
                "time_sum": 2.5,
            },
        ]

        # Путь к временному файлу
        test_file_path = "test_report.html"

        # Вызов метода для записи в HTML
        LogWriter.write_to_html(test_file_path, data)

        # Проверка наличия файла
        self.assertTrue(os.path.exists(test_file_path))

        # Открытие и проверка содержимого
        with open(test_file_path, "r", encoding="utf-8") as file:
            content = file.read()

            # Проверка, что данные правильно вставлены в HTML
            self.assertIn("/index.html", content)
            self.assertIn("10", content)  # Проверка наличия количества
            self.assertIn("50%", content)  # Проверка процента
            self.assertIn(
                "0.32", content
            )  # Проверка среднего времени (2 знака после запятой)

        os.remove(test_file_path)


if __name__ == "__main__":
    unittest.main()
