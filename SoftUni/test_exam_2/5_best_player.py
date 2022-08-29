# Най-добър играч
# Пепи иска да напишете програма, чрез която да разбере кой е най-добрият играч от световното първенство.
# Информацията, която получавате ще бъде играч и колко гола е отбелязал. От вас се иска да отпечатате кой е играчът
# с най-много голове и дали е направил хет-трик. Хет-трик е, когато футболистът е вкарал 3 или повече гола.
# Ако футболистът е вкарал 10 или повече гола, програмата трябва да спре.
# Вход:
# От конзолата се четат по два реда до въвеждане на команда "END":
# Име на играч – текст
# Брой вкарани голове  – цяло положително число в интервала [1 … 10000]
# Изход:
# На конзолата да се отпечатат 2 реда :
# На първия ред:
#             "{име на играч} is the best player!"
# На втория ред :
#  Ако най-добрият футболист е направил хеттрик:
#                    "He has scored {брой голове} goals and made a hat-trick !!!"
# Ако най-добрият футболист не е направил хеттрик:
#                    "He has scored {брой голове} goals."

name_best_player: str = ""
number_best_goals: int = 0


name_player: str = input()
while name_player != "END":
    number_goals: int = int(input())
    if number_goals > number_best_goals:
        number_best_goals = number_goals
        name_best_player = name_player
    if number_goals >= 10:
        break
    else:
        name_player: str = input()

if number_goals >= 3:
    print(f"{name_best_player} is the best player!")
    print(f"He has scored {number_best_goals} goals and made a hat-trick !!!")

else:
    print(f"{name_best_player} is the best player!")
    print(f"He has scored {number_best_goals} goals.")


