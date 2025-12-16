import json


def task() -> float:
    # Открываем и читаем JSON файл
    with open('input.json', 'r', encoding='utf-8') as file:
        data = json.load(file)

    # Вычисляем сумму произведений score * weight для каждого словаря
    total = 0.0
    for item in data:
        score = item.get('score', 0)
        weight = item.get('weight', 0)
        total += score * weight

    # Округляем до 3 знаков после запятой
    return round(total, 3)


print(task())