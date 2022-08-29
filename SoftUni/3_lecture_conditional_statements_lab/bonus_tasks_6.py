# Домашни любимци
# Марина обича да пътува. Тя има 3 домашни любимеца (куче, котка и костенурка). Когато заминава на пътешествие трябва
# да съобрази колко храна да им остави, за да не останат гладни. Напишете програма, която пресмята колко килограма
# храна ще изядат всички за времето, в което Марина отсъства и дали оставената храна от нея ще им е достатъчна.
# Всяко животно изяжда определено количество храна на ден.

# Вход
# От конзолата се четат пет реда:
# Първи ред – брой дни – цяло число в интервал [1…5000]
# Втори ред – оставена храна в килограми – цяло число в интервал [0…100000]
# Трети ред – храна на ден за кучето в килограми – реално число в интервал [0.00…100.00]
# Четвърти ред – храна на ден за котката в килограми– реално число в интервал [0.00…100.00]
# Пети ред – храна на ден за костенурката в грамове – реално число в интервал [0.00…10000.00]

# Изход
# На конзолата трябва да се отпечата на един ред:
# Ако оставената храна Е достатъчна:
# "{килограма остатък} kilos of food left."
# Резултатът трябва да е закръглен към
# по-ниското цяло число

# Ако оставената храна НЕ Е достатъчна:
# “{килограма недостигат} more kilos of food are needed.”
# Резултатът трябва да е закръглен към
# по-високото цяло число

import math

number_days: int = int(input())
left_food: int = int(input())
dog_food_per_day: float = float(input())
cat_food_per_day: float = float(input())
turtle_food_per_day: float = float(input())

dog_eats: float = dog_food_per_day * number_days
cat_eats: float = cat_food_per_day * number_days
turtle_eats: float = (turtle_food_per_day / 1000) * number_days

all_animals_eat: float = dog_eats + cat_eats + turtle_eats

if all_animals_eat <= left_food:
    difference: int = math.floor(left_food - all_animals_eat)
    print(f"{difference} kilos of food left.")

else:
    difference: int = math.ceil(all_animals_eat - left_food)
    print(f"{difference} more kilos of food are needed.")








