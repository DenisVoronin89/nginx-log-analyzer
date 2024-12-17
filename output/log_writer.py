from jinja2 import Template
from typing import List, Dict


class LogWriter:
    """
    Формирование и сохранение отчета в формате HTML.
    """

    @staticmethod
    def write_to_html(file_path: str, data: List[Dict[str, float]]):
        """
        Сохранение данных статистики в HTML-файл в формате таблицы.
        """
        template = Template(
            """\
            <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Log Report</title>
                <style>
                    table { border-collapse: collapse; width: 100%; }
                    th, td { border: 1px solid #ddd; padding: 8px; text-align: left; }
                    th { background-color: #f2f2f2; }
                </style>
            </head>
            <body>
                <h1>Log Report</h1>
                <table>
                    <thead>
                        <tr>
                            <th>URL</th>
                            <th>Count</th>
                            <th>Count Percentage</th>
                            <th>Avg Time</th>
                            <th>Max Time</th>
                            <th>Median Time</th>
                            <th>Time Percentage</th>
                            <th>Time Sum</th>
                        </tr>
                    </thead>
                    <tbody>
                        {% for row in data %}
                        <tr>
                            <td>{{ row.url }}</td>
                            <td>{{ row.count }}</td>
                            <td>{{ row.count_perc }}%</td>
                            <td>{{ row.time_avg }}</td>
                            <td>{{ row.time_max }}</td>
                            <td>{{ row.time_med }}</td>
                            <td>{{ row.time_perc }}%</td>
                            <td>{{ row.time_sum }}</td>
                        </tr>
                        {% endfor %}
                    </tbody>
                </table>
            </body>
            </html>
            """
        )

        html_content = template.render(data=data)

        with open(file_path, "w", encoding="utf-8") as file:
            file.write(html_content)
