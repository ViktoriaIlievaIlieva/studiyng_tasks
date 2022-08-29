# Реколта
# От лозе с площ X квадратни метри се заделя 40% от реколтата за производство на вино.
# От 1 кв.м лозе се изкарват Y килограма грозде.
# За 1 литър вино са нужни 2,5 кг. грозде.
# Желаното количество вино за продан е Z литра.

# Напишете програма, която пресмята колко вино може да се произведе и дали това количество е достатъчно.
# Ако е достатъчно, остатъкът се разделя по равно между работниците на лозето.

# Вход
# Входът се чете от конзолата и се състои от точно 4 реда:
# 1ви ред: X кв.м е лозето – цяло число в интервала [10 … 5000]
# 2ри ред: Y грозде за един кв.м – реално число в интервала [0.00 … 10.00]
# 3ти ред: Z нужни литри вино – цяло число в интервала [10 … 600]
# 4ти ред: брой работници – цяло число в интервала [1 … 20]

# Изход- на конзолата трябва да се отпечата следното:

# Ако произведеното вино е по-малко от нужното:
# “It will be a tough winter! More {недостигащо вино} liters wine needed.”
# Резултатът трябва да е закръглен към по-ниско цяло число

# Ако произведеното вино е колкото или повече от нужното:
# “Good harvest this year! Total wine: {общо вино} liters.”
# Резултатът трябва да е закръглен към по-ниско цяло число
# “{Оставащо вино} liters left -> {вино за 1 работник} liters per person.”
# И двата резултата трябва да са закръглени към по-високото цяло число

import math

vine_square_meters: int = int(input())
kg_grape_on_1_square_meter: float = float(input())
needed_liters_wine: float = float(input())
num_workers: int = int(input())

whole_harvests: float = vine_square_meters * kg_grape_on_1_square_meter
harvest_for_wine: float = ((whole_harvests / 100) * 40) / 2.5


if harvest_for_wine < needed_liters_wine:
    more_needed_wine: float = needed_liters_wine - harvest_for_wine
    print(f"It will be a tough winter! More {math.floor(more_needed_wine)} liters wine needed.")

elif harvest_for_wine >= needed_liters_wine:
    print(f"Good harvest this year! Total wine: {math.floor(harvest_for_wine)} liters.")
    left_wine: float = harvest_for_wine - needed_liters_wine
    wine_per_worker: float = left_wine / num_workers
    print(f"{math.ceil(left_wine)} liters left -> {math.ceil(wine_per_worker)} liters per person.")

# Example for abs() - ще изкара разликата между двете като положително число
# difference_in_wine може да замести едновременно more_needed_wine и left_wine
#
# difference_in_wine = math.abs(harvest_for_wine - needed_liters_wine)
