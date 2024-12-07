import csv


class CSVWriter:
    """
    Класс для формирования и сохранения отчета в формате CSV.
    """

    @staticmethod
    def write_to_csv(file_path: str, data: dict):
        """
        Сохраняет данные статистики в CSV-файл в формате 'ключ - значение'.
        """
        # Приводим все значения данных до 2 знаков после запятой
        formatted_data = {
            key: round(value, 2) if isinstance(value, (int, float)) else value
            for key, value in data.items()
        }

        # Запись данных в формате в файл
        with open(file_path, mode="w", newline="") as file:
            for key, value in formatted_data.items():
                file.write(f"{key} - {value}\n")
