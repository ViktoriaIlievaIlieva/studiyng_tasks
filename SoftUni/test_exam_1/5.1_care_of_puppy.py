# . Грижи за кученце
# Ани намира кученце, за което ще се грижи, докато се намери някой да го осинови. То изяжда дневно определено
# количество храна. Да се напише програма, която проверява дали количеството храна, което е закупено за кученцето,
# ще е достатъчно докато кученцето бъде осиновено.
# Вход
# От конзолата се прочитат:
# Закупеното количество храна за кученцето в килограми – цяло число в интервала [1 …100]
# На всеки следващ ред до получаване на команда Adopted ще получавате колко грама изяжда кученцето на всяко хранене -
# цяло число в интервала [10 …1000]
# Изход
# На конзолата се отпечатва 1 ред:
# Ако количеството храна е достатъчно да се отпечата:
#  	"Food is enough! Leftovers: {останала храна} grams."
# Ако количеството храна не е достатъчно да се отпечата:
#  	"Food is not enough. You need {нужно количество храна} grams more."

bought_food: int = int(input())
bought_food_in_gr = bought_food * 1000
all_eaten_food: int = 0

eaten_food: str = input()
while eaten_food != "Adopted":
    all_eaten_food += int(eaten_food)
    eaten_food: str = input()

diff: int = abs(bought_food_in_gr - all_eaten_food)

if all_eaten_food <= bought_food_in_gr:
    print(f"Food is enough! Leftovers: {diff} grams.")
else:
    print(f"Food is not enough. You need {diff} grams more.")


