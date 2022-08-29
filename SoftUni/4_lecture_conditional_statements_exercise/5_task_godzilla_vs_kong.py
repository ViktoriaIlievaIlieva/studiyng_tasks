# ⦁	Годзила срещу Конг
# Снимките за дългоочаквания филм "Годзила срещу Конг" започват. Сценаристът Адам Уингард ви моли да напишете програма,
# която да изчисли, дали предвидените средства са достатъчни за снимането на филма. За снимките  ще бъдат нужни
# определен брой статисти, облекло за всеки един статист и декор.
# Известно е, че:
# ⦁	Декорът за филма е на стойност 10% от бюджета.
# ⦁	При повече от 150 статиста,  има отстъпка за облеклото на стойност 10%.
# Вход
# От конзолата се четат 3 реда:
# ⦁	Бюджет за филма – реално число в интервала [1.00 … 1000000.00]
# ⦁	Брой на статистите – цяло число в интервала [1 … 500]
# ⦁	Цена за облекло на един статист – реално число в интервала [1.00 … 1000.00]
# Изход
# На конзолата трябва да се отпечатат два реда:
# ⦁	Ако  парите за декора и дрехите са повече от бюджета:
# ⦁	"Not enough money!"
# ⦁	"Wingard needs {парите недостигащи за филма} leva more."
# ⦁	Ако парите за декора и дрехите са по малко или равни на бюджета:
# ⦁	"Action!"
# ⦁	"Wingard starts filming with {останалите пари} leva left."
# Резултатът трябва да е форматиран до втория знак след десетичната запетая.

film_budget: float = float(input())
number_stat: int = int(input())
price_for_cloths_per_stat: float = float(input())

sets: float = (film_budget/100) * 10

money_for_cloths: float = number_stat * price_for_cloths_per_stat

if number_stat > 150:
    money_for_cloths -= (money_for_cloths/100) * 10

cost = money_for_cloths + sets

dif: float = abs(film_budget - cost)

if film_budget >= cost:
    print("Action!")
    print(f"Wingard starts filming with {dif:.2f} leva left.")
else:
    print("Not enough money!")
    print(f"Wingard needs {dif:.2f} leva more.")

# DONE
