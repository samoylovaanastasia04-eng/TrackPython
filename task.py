def find_common_participants(group1, group2, sep=','):

    participants1 = group1.split(sep)
    participants2 = group2.split(sep)


    set1 = set(participants1)
    set2 = set(participants2)


    common_participants = set1.intersection(set2)


    return sorted(list(common_participants))


#
participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"


common = find_common_participants(participants_first_group, participants_second_group, sep="|")
print(f"Общие участники (разделитель '|'): {common}")


group1_comma = "Иванов,Петров,Сидоров"
group2_comma = "Петров,Сидоров,Смирнов"
common_comma = find_common_participants(group1_comma, group2_comma)
print(f"Общие участники (разделитель ','): {common_comma}")

# Дополнительный тест
group3 = "Анна,Борис,Виктор,Галина"
group4 = "Виктор,Галина,Дмитрий,Елена"
common_extra = find_common_participants(group3, group4)
print(f"Общие участники (дополнительный тест): {common_extra}")