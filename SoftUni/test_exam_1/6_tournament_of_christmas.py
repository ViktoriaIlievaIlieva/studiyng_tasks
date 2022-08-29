# Задача 6. Коледен турнир
# Напишете програма, която проследява представянето на вашия отбор на благотворителен коледен турнир.
# Всеки ден получавате имена на игри до команда "Finish".
# Със спечелването на всяка една игра печелите по 20лв. за благотворителност.
# Трябва да изчислите колко пари сте спечелили на края на деня.
# Ако имате повече спечелени игри, отколкото загубени – вие сте победители този ден и увеличавате парите от него с 10%.
# При приключване на турнира ако през повечето дни сте били победители печелите турнира и увеличавате всичките
# спечелени пари с 20%.
# Никога няма да имате равен брой спечелени и загубени игри.
# Вход
# Първоначално от конзолата се прочита броя дни на турнира – цяло число в интервала [1… 20]
# До получаване на командата "Finish" се чете:
# Спорт  – текст
# За всеки спорт се прочита:
# Резултат  – текст с възможности: "win" или "lose"
# Изход
# Накрая се отпечатва един ред:
# Ако сте спечелили турнира:
#      	"You won the tournament! Total raised money: {спечелените пари}"
# Ако сте загубили на турнира:
# "You lost the tournament! Total raised money: {спечелените пари}"
# Парите да бъдат форматирани до втората цифра след десетичния знак.


num_days: int = int(input())
total_money: float = 0
won_days: int = 0
lost_days: int = 0

for days in range(0, num_days):

    won_games_for_the_day: int = 0
    lost_games_for_the_day: int = 0
    daily_won_money: int = 0

    sport: str = input()
    while sport != "Finish":
        result: str = input()

        if result == "win":
            total_money += 20
            daily_won_money += 20
            won_games_for_the_day += 1
        else:
            lost_games_for_the_day += 1
        sport: str = input()

    if won_games_for_the_day > lost_games_for_the_day:
        won_days += 1
        daily_bonus = daily_won_money / 100 * 10
        total_money += daily_bonus
    else:
        lost_days += 1


if lost_days < won_days:
    total_money = total_money + (total_money * 0.20)
    print(f"You won the tournament! Total raised money: {total_money:.2f}")
else:
    print(f"You lost the tournament! Total raised money: {total_money:.2f}")




