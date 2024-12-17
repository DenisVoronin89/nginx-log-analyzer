from typing import List, Dict
from statistics import mean, median


class StatsCalculator:
    """
    Расчет статистики по времени ответа для каждого URL.
    """

    @staticmethod
    def calculate(
        urls: List[str], response_times: List[float]
    ) -> List[Dict[str, float]]:
        """
        Вычисление статистики по времени отклика для каждого URL.
        """
        if not urls or not response_times:
            return []

        # Группировка по URL и вычисление статистики
        url_stats = {}
        for url, time in zip(urls, response_times):
            if url not in url_stats:
                url_stats[url] = []
            url_stats[url].append(time)

        result = []
        for url, times in url_stats.items():
            # Сортировка времени отклика для корректной медианы
            times.sort()
            result.append(
                {
                    "url": url,
                    "count": len(times),
                    "count_perc": len(times) / len(response_times) * 100,
                    "time_avg": mean(times),
                    "time_max": max(times),
                    "time_med": median(times),
                    "time_perc": sum(times) / sum(response_times) * 100,
                    "time_sum": sum(times),
                }
            )
        return result
