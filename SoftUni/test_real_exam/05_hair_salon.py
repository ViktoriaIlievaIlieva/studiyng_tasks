# Фризьорски салон
# Тя всеки ден си поставя за цел да постигне определена печалба.
# Напишете програма, която изчислява дали е успяла да постигне целта за деня, като знаете следното:
# Деси ще приема клиенти докато не приключи работния ден. Ако постигне желания приход обаче, тя ще затвори салона.
# Когато клиент влезе ще може да си избере една от следните услуги:
# Подстригване (haircut):
# Мъжко (mens) - 15лв.
# Дамско (ladies) – 20лв.
# Детско (kids) – 10лв.
# Боядисване (color):
# Поддръжка (touch up) – 20лв.
# Пълно боядисване (full color) – 30лв.
# Вход:
# От конзолата първоначално се чете 1 ред:
# цел за деня – цяло число в интервала [1 … 5000]
# След това се четат поредица от редове до получаване на команда "closed" или докато Деси не постигне целта за деня
# – услугата, която иска клиентът – текст с възможности "haircut" и "color".
# При команда "haircut" ще се очаква да се въведе видът на подстригването – "mens", "ladies" или "kids".
# При команда "color" ще се очаква видът на боядисването – "touch up" или "full color".
# Изход:
# На конзолата се отпечатват 2 реда:
# На първия ред:
# Ако Деси е успяла да постигне целта за деня:
# "You have reached your target for the day!"
# Ако Деси не е успяла да постигне целта за деня:
# "Target not reached! You need {колко пари не и достигат, за да стигне целта}lv. more."
# На втория ред:
# 	"Earned money: {парите, които е спечелила за деня}lv."

money_goal = int(input())
earned_money = 0

service = input()
while service != "closed":
    specific_service = input()
    if service == "haircut":
        if specific_service == "mens":
            earned_money += 15
        elif specific_service == "ladies":
            earned_money += 20
        elif specific_service == "kids":
            earned_money += 10

    elif service == "color":
        if specific_service == "touch up":
            earned_money += 20
        elif specific_service == "full color":
            earned_money += 30
    if earned_money >= money_goal:
        break
    service = input()

diff = abs(money_goal - earned_money)

if earned_money >= money_goal:
    print(f"You have reached your target for the day!")
else:
    print(f"Target not reached! You need {diff}lv. more.")

print(f"Earned money: {earned_money}lv.")

# Done - 100/100
