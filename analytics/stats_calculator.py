import statistics


class StatsCalculator:
    """
    Класс для расчета статистики по метрикам.
    """

    @staticmethod
    def calculate(response_times):
        if (
            not response_times
        ):  # Если список пустой, возвращаем значения по умолчанию
            return {
                "average": 0,
                "median": 0,
                "max": 0,
                "min": 0,
                "total_requests": 0,
            }

        # Вычисление статистики
        total_requests = len(response_times)
        average = sum(response_times) / total_requests
        sorted_times = sorted(response_times)
        median = (
            sorted_times[total_requests // 2]
            if total_requests % 2 != 0
            else (
                sorted_times[total_requests // 2 - 1]
                + sorted_times[total_requests // 2]
            )
            / 2
        )
        return {
            "average": average,
            "median": median,
            "max": max(response_times),
            "min": min(response_times),
            "total_requests": total_requests,
        }
