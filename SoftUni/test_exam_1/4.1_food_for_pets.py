# ⦁	Задача 4. Храна за домашни любимци
# Ани има два домашни любимеца - куче и котка. Напишете програма, която изготвя статистика за храната на домашните
# любимци за определен брой дни.
# Всеки ден кучето и котката изяждат различно количество от общата им храна.
# На всеки трети ден получават награда - бисквитки. Количеството на бисквитките е 10% от общо изядената храна за деня.
# Вашата програма трябва да отпечатва статистика за количеството бисквитки, които са изяли, колко процента от
#  първоначалното количество обща храна са изяли и колко процента от изядената храна е изяло кучето и колко е изяла котката.
# Вход
# Първоначално се чете един ред:
# ⦁	Брой дни – цяло число в диапазона [1…30]
# ⦁	Общо количество храна – реално число в диапазона [0.00…10000.00]
# След това за всеки ден се чете:
# ⦁	Количество изядена храна от кучето – цяло число в диапазона [10…500]
# ⦁	Количество изядена храна от котката – цяло число в диапазона [10…500]
# Изход
# На конзолата да се отпечатват четири реда:
# ⦁	"Total eaten biscuits: {количество изядени бисквитки}gr."
# ⦁	"{процент изядена храна}% of the food has been eaten."
# ⦁	"{процент изядена храна от кучето}% eaten from the dog."
# ⦁	"{процент изядена храна от котката}% eaten from the cat."
# Количеството изядени бисквитки трябва да бъде закръглено до най – близкото цяло число, а процентът храна трябва да
# бъде форматиран до втората цифра след десетичния знак.

import math

num_days: int = int(input())
food: float = float(input())
daily_food: float = 0
biscuits: float = 0
eaten_food_all: float = 0
eaten_food_dog: float = 0
eaten_food_cat: float = 0
all_biscuits: float = 0


for day in range(1, num_days + 1):
    dog_food: int = int(input())
    cat_food: int = int(input())
    daily_food: int = dog_food + cat_food
    if day % 3 == 0:
        biscuits: float = daily_food * 0.10
        all_biscuits += biscuits
    eaten_food_dog += dog_food
    eaten_food_cat += cat_food
    eaten_food_all += dog_food + cat_food

print(f"Total eaten biscuits: {math.floor(all_biscuits)}gr.")

percentage_eaten_food: float = (eaten_food_all / food) * 100

print(f"{percentage_eaten_food:.2f}% of the food has been eaten.")

percentage_eaten_food_dog: float = (eaten_food_dog / eaten_food_all) * 100

print(f"{percentage_eaten_food_dog:.2f}% eaten from the dog.")

percentage_eaten_food_cat: float = (eaten_food_cat / eaten_food_all) * 100

print(f"{percentage_eaten_food_cat:.2f}% eaten from the cat.")
