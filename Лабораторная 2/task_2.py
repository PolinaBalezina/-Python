salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен
total_spend = 0
money_capital = salary * months - total_spend
# TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов
for months in range (months):
    total_spend += spend
    spend *= (1 + increase)
print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", money_capital)