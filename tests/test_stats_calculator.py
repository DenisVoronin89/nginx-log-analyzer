import unittest
from analytics.stats_calculator import StatsCalculator


class TestStatsCalculator(unittest.TestCase):

    def test_calculate_statistics(self):
        # Пример данных для теста
        urls = [
            "/index.html",
            "/about.html",
            "/index.html",
            "/index.html",
            "/about.html",
        ]
        response_times = [0.12, 0.15, 0.20, 0.35, 0.50]

        # Ожидаемые результаты
        expected_stats = [
            {
                "url": "/index.html",
                "count": 3,
                "count_perc": 60.0,
                "time_avg": 0.22333333333333333,
                "time_max": 0.35,
                "time_med": 0.20,
                "time_perc": 50.76,
                "time_sum": 0.67,
            },
            {
                "url": "/about.html",
                "count": 2,
                "count_perc": 40.0,
                "time_avg": 0.325,
                "time_max": 0.50,
                "time_med": 0.325,
                "time_perc": 49.24,
                "time_sum": 0.65,
            },
        ]

        # Рассчет статистики
        stats = StatsCalculator.calculate(urls, response_times)

        # Проверка, что рассчитанные значения соответствуют ожидаемым
        for expected_stat, stat in zip(expected_stats, stats):
            self.assertEqual(stat["url"], expected_stat["url"])
            self.assertEqual(stat["count"], expected_stat["count"])
            self.assertAlmostEqual(
                stat["count_perc"], expected_stat["count_perc"], places=1
            )
            self.assertAlmostEqual(
                stat["time_avg"], expected_stat["time_avg"], places=2
            )
            self.assertEqual(stat["time_max"], expected_stat["time_max"])
            self.assertAlmostEqual(
                stat["time_med"], expected_stat["time_med"], places=2
            )  # Проверка медианы
            self.assertAlmostEqual(
                stat["time_perc"], expected_stat["time_perc"], places=1
            )
            self.assertAlmostEqual(
                stat["time_sum"], expected_stat["time_sum"], places=2
            )

    def test_empty_list(self):
        # Проверка поведения на пустом списке
        urls = []
        response_times = []
        stats = StatsCalculator.calculate(urls, response_times)

        self.assertEqual(stats, [])


if __name__ == "__main__":
    unittest.main()
