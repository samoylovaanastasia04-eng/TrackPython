list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

# Определяем общее количество игроков
total_players = len(list_players)

# Разделяем на две равные команды
first_team = list_players[:total_players//2]
second_team = list_players[total_players//2:]

print(first_team)
print(second_team)