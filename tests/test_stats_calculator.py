import unittest
from analytics.stats_calculator import StatsCalculator


class TestStatsCalculator(unittest.TestCase):

    def test_calculate_statistics(self):
        # Пример данных для теста
        response_times = [0.12, 0.15, 0.20, 0.35, 0.50]

        # Ожидаемые результаты
        expected_stats = {
            "average": 0.264,
            "median": 0.20,
            "max": 0.50,
            "min": 0.12,
            "total_requests": 5,
        }

        stats = StatsCalculator.calculate(response_times)

        # Проверка, что рассчитанные значения соответствуют ожидаемым
        self.assertEqual(stats["average"], expected_stats["average"])
        self.assertEqual(stats["median"], expected_stats["median"])
        self.assertEqual(stats["max"], expected_stats["max"])
        self.assertEqual(stats["min"], expected_stats["min"])
        self.assertEqual(
            stats["total_requests"], expected_stats["total_requests"]
        )

    def test_empty_list(self):
        # Проверка поведения на пустом списке
        response_times = []
        stats = StatsCalculator.calculate(response_times)
        self.assertEqual(stats["average"], 0)
        self.assertEqual(stats["median"], 0)
        self.assertEqual(stats["max"], 0)
        self.assertEqual(stats["min"], 0)
        self.assertEqual(stats["total_requests"], 0)


if __name__ == "__main__":
    unittest.main()
