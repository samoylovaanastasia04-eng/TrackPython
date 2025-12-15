salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен


money_capital = 0
monthly_spend = spend


for month in range(months):

    deficit = monthly_spend - salary


    money_capital += deficit


    monthly_spend *= (1 + increase)


money_capital = round(money_capital)

print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", money_capital)