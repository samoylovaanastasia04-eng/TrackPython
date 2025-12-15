money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

months = 0
current_money = money_capital


while True:

    current_money += salary


    if current_money >= spend:

        current_money -= spend
        months += 1

        spend *= (1 + increase)
    else:
        break

print("Количество месяцев, которое можно протянуть без долгов:", months)