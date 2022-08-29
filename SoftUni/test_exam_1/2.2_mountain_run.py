# Задача 2.  Скоростно изкачване
# Георги решава да подобри рекорда за най-бързо изкачване на връх Монблан. На конзолата се въвежда рекордът в секунди,
# който Георги трябва да подобри, разстоянието в метри, което трябва да изкачи и времето в секунди, за което той
# изкачва 1 метър. Да се напише програма, която изчислява дали се е справил със задачата, като се има предвид, че:
# наклона на терена го забавя на всеки 50 м. с 30 секунди. Да се изчисли времето в секунди, за което Георги ще изкачи
# разстоянието до върха и разликата спрямо рекорда.
# Когато се изчислява колко пъти Георги ще се забави в резултат на наклона на терена, резултатът трябва да се закръгли
# надолу до най-близкото цяло число.
# Вход
# От конзолата се четат 3 реда:
# Рекордът в секунди – реално число в интервала [0.00 … 100000.00]
# Разстоянието в метри – реално число в интервала [0.00 … 100000.00]
# Времето в секунди, за което изкачва 1 м. – реално число в интервала [0.00 … 1000.00]
# Изход
# Отпечатването на конзолата зависи от резултата:
# Ако Георги е подобрил рекорда отпечатваме:
# " Yes! The new record is {времето на Георги} seconds."
# Ако НЕ е подобрил рекорда отпечатваме:
# "No! He was {недостигащите секунди} seconds slower."
# Резултатът трябва да се форматира до втория знак след десетичната запетая.

import math

record_in_sec: float = float(input())
destination_in_meters: float = float(input())
time_in_sec_for_1_m: float = float(input())

initial_time: float = destination_in_meters * time_in_sec_for_1_m
num_slowdowns: int = (math.floor(destination_in_meters / 50) * 30)
final_time: float = initial_time + num_slowdowns

diff = abs(record_in_sec - final_time)

if final_time < record_in_sec:
    print(f"Yes! The new record is {final_time:.2f} seconds.")
else:
    print(f"No! He was {diff:.2f} seconds slower.")
