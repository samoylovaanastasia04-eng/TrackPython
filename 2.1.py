import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    # Считываем содержимое CSV файла
    with open(INPUT_FILENAME, 'r', encoding='utf-8') as csv_file:
        # Читаем все строки
        lines = csv_file.read().strip().split('\n')

        # Извлекаем заголовки из первой строки
        headers = [header.strip() for header in lines[0].split(',')]

        # Создаем список для хранения словарей
        data = []

        # Обрабатываем каждую строку данных (начиная со второй строки)
        for line in lines[1:]:
            # Пропускаем пустые строки
            if not line.strip():
                continue

            # Разбиваем строку на значения по запятой и убираем лишние пробелы
            values = [value.strip() for value in line.split(',')]

            # Создаем словарь для текущей строки, сопоставляя заголовки и значения
            row_dict = {}
            # Используем минимальное количество пар, чтобы избежать IndexError
            min_length = min(len(headers), len(values))
            for i in range(min_length):
                row_dict[headers[i]] = values[i]

            # Добавляем словарь в общий список
            data.append(row_dict)

    # Записываем данные в JSON файл с отступами
    with open(OUTPUT_FILENAME, 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, indent=4, ensure_ascii=False)


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")