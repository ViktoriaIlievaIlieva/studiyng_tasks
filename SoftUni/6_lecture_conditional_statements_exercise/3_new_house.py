# Марин и Нели си купуват къща недалеч от София. Нели толкова много обича цветята, че Ви убеждава да напишете програма,
# която да изчисли колко  ще им струва, за да засадят определен брой цветя и дали наличният бюджет ще им е достатъчен.
# Различните цветя са с различни цени:
# цвете	                Роза	Далия	Лале	Нарцис	    Гладиола
# Цена на брой в лева	5	    3.80	2.80	3	        2.50

# Съществуват следните отстъпки:
# ⦁	Ако Нели купи повече от 80 Рози - 10% отстъпка от крайната цена;
# ⦁	Ако Нели купи повече от 90  Далии - 15% отстъпка от крайната цена;
# ⦁	Ако Нели купи повече от 80 Лалета - 15% отстъпка от крайната цена;
# ⦁	Ако Нели купи по-малко от 120 Нарциса - цената се оскъпява с 15%;
# ⦁	Ако Нели Купи по-малко от 80 Гладиоли - цената се оскъпява с 20%.

# От конзолата се четат 3 реда:
# ⦁	Вид цветя - текст с възможности "Roses", "Dahlias", "Tulips", "Narcissus" или "Gladiolus";
# ⦁	Брой цветя - цяло число;
# ⦁	Бюджет - цяло число.

# Да се отпечата на конзолата на един ред:
# ⦁	Ако бюджетът им е достатъчен - "Hey, you have a great garden with {броя цвета} {вид цветя} and {останалата сума} leva left.";
# ⦁	Ако бюджета им е НЕ достатъчен - "Not enough money, you need {нужната сума} leva more.".
# Сумата да бъде форматирана до втория знак след десетичната запетая.


flower: str = input()
num_flower: int = int(input())
budget: int = int(input())
price: float = 0

if flower == "Roses":
    if num_flower > 80:
        price = (num_flower*5) - ((num_flower*5) * 0.1)
    elif num_flower <= 80:
        price = num_flower * 5

elif flower == "Dahlias":
    if num_flower > 90:
        price = (num_flower*3.80) - ((num_flower*3.80) * 0.15)
    elif num_flower <= 90:
        price = num_flower * 3.80

elif flower == "Tulips":
    if num_flower > 80:
        price = (num_flower*2.80) - ((num_flower*2.80) * 0.15)
    elif num_flower <= 80:
        price = num_flower * 2.80

elif flower == "Narcissus":
    if num_flower < 120:
        price = (num_flower*3) + ((num_flower*3) * 0.15)
    elif num_flower >= 120:
        price = num_flower * 3

elif flower == "Gladiolus":
    if num_flower < 80:
        price = (num_flower*2.50) + ((num_flower*2.50) * 0.20)
    elif num_flower >= 80:
        price = num_flower * 2.50

diff = abs(price - budget)

if price <= budget:
    print(f"Hey, you have a great garden with {num_flower} {flower} and {diff:.2f} leva left.")
else:
    print(f"Not enough money, you need {diff:.2f} leva more.")

# DONE
