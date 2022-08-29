# Задача 4. Топки
# В кутия имаме неопределен брой топки с различни цветове, които ни носят различен брой точки.
# Задачата ни е да извадим Х бр. топки, които ще бъдат въведени от конзолата, като се има в предвид, че всеки различен
# цвят влияе на точките ни по следния начин:
# Ако топката е “red” точките ни се повишават с 5.
# Ако топката е “orange” точките ни се повишават с 10.
# Ако топката е “yellow” точките ни се повишават с 15.
# Ако топката е “white” точките ни се повишават с 20.
# Ако топката е “black” точките ни се делят на 2, като закръгляме към по-малкото цяло число.
# Ако топката е с какъвто и да е цвят, различен от по-горните, точките не се манипулират и програмата продължава да
# работи.
# Вход:
# От конзолата се чете 1 цяло число N, което е броят на топките в диапазон (0-1000).
# След това се четат N на брой цветове.
# Изход:
# Отпечатват се следните редове:
# "Total points: {всичките събрани точки}"
# "Red balls: {броят червени топки}"
# "Orange balls: {броят оранжеви топки}"
# "Yellow balls: {броят жълти топки}"
# "White balls: {броят бели топки}"
# "Other colors picked: {броят на избраните топки извън зададените цветове}"
# "Divides from black balls: {броят на пътите, в които точките са били разделяни на 2}"
import math

num_balls: int = int(input())

red: int = 0
orange: int = 0
yellow: int = 0
white: int = 0
black: int = 0
other: int = 0
count: int = 0
score: int = 0


for _ in range(0, num_balls):
    type_ball: str = input()
    if type_ball == "red":
        score += 5
        red += 1
    elif type_ball == "orange":
        score += 10
        orange += 1
    elif type_ball == "yellow":
        score += 15
        yellow += 1
    elif type_ball == "white":
        score += 20
        white += 1
    elif type_ball == "black":
        score /= 2
        count += 1
        black += 1
    else:
        other += 1

print(f"Total points: {math.floor(score)}")
print(f"Red balls: {red}")
print(f"Orange balls: {orange}")
print(f"Yellow balls: {yellow}")
print(f"White balls: {white}")
print(f"Other colors picked: {other}")
print(f"Divides from black balls: {count}")