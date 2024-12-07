import unittest
import os
from output.csv_writer import CSVWriter


class TestCSVWriter(unittest.TestCase):

    def test_write_to_csv(self):
        # Пример данных
        data = {
            "average": 0.32,
            "median": 0.31,
            "max": 0.59,
            "min": 0.12,
            "total_requests": 20
        }

        # Путь к временному файлу
        test_file_path = "test_report.csv"

        # Вызов метода для записи в CSV
        CSVWriter.write_to_csv(test_file_path, data)

        # Проверка наличия файла
        self.assertTrue(os.path.exists(test_file_path))

        # Открытие и проверка содержимого
        with open(test_file_path, "r") as file:
            lines = file.readlines()
            self.assertEqual(len(lines), 5)
            self.assertIn("average - 0.32\n", lines)
            self.assertIn("total_requests - 20\n", lines)

        os.remove(test_file_path)


if __name__ == "__main__":
    unittest.main()

