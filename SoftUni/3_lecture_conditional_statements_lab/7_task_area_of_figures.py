# ⦁	Лица на фигури
# Да се напише програма, в която потребителят въвежда вида и размерите на геометрична фигура и пресмята лицето й.
# Фигурите са четири вида: квадрат (square), правоъгълник (rectangle), кръг (circle) и триъгълник (triangle). На първия
# ред на входа се чете вида на фигурата (текст със следните възможности: square, rectangle, circle или triangle).
# ⦁	Ако фигурата е квадрат (square): на следващия ред се чете едно дробно число - дължина на страната му
# ⦁	Ако фигурата е правоъгълник (rectangle): на следващите два реда четат две дробни числа - дължините на страните му
# ⦁	Ако фигурата е кръг (circle): на следващия ред чете едно дробно число - радиусът на кръга
# ⦁	Ако фигурата е триъгълник (triangle): на следващите два реда четат две дробни числа - дължината на страната му и
# дължината на височината към нея
# Резултатът да се закръгли до 3 цифри след десетичната запетая.

import math
result: float = 0

figure: str = input()
if figure == "square":
    x: float = float(input())
    result = x * x

elif figure == "rectangle":
    x: float = float(input())
    y: float = float(input())
    result = x * y

elif figure == "circle":
    r: float = float(input())
    result = r**2 * math.pi

elif figure == "triangle":
    x: float = float(input())
    h: float = float(input())
    result = h*x / 2

print(f"{result:.3f}")
