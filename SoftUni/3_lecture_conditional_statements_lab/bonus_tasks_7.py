# Магазин за цветя
# Мария иска да купи подарък на сина си. Тя работи в магазин за цветя. В магазина идва поръчка за цветя.
# Напишете програма, която пресмята сумата от поръчката и дали печалбата е достатъчна за подаръка. Цветята имат следните цени:
#
# Магнолии – 3.25 лева
# Зюмбюли – 4 лева
# Рози – 3.50 лева
# Кактуси – 8 лева
# От общата сума, Мария трябва да плати 5% данъци.
#
#
# Вход
# Входът се чете от конзолата и се състои от 5 реда:
# Брой магнолии – цяло число в интервала [0 … 50]
# Брой зюмбюли – цяло число в интервала [0 … 50]
# Брой рози – цяло число в интервала [0 … 50]
# Брой кактуси – цяло число в интервала [0 … 50]
# Цена на подаръка – реално число в интервала [0.00 … 500.00]
# Изход
# На конзолата трябва да се отпечата един ред.

# Ако парите СА стигнали: "She is left with {останали} leva." – сумата трябва да е закръглена към по-малко цяло число (пр. 1.90 -> 1).

# Ако парите НЕ достигат: "She will have to borrow {останали} leva." – сумата трябва да е закръглена към по-голямо цяло число (пр. 1.10 -> 2).

import math

num_magnolias: int = int(input())
num_hyacinth: int = int(input())
num_roses: int = int(input())
num_cactus: int = int(input())
value_gift: float = float(input())

order: float = num_magnolias * 3.25 + num_hyacinth * 4 + num_roses * 3.50 + num_cactus * 8

order_after_tax: float = order - ((order/100) * 5)

if order_after_tax >= value_gift:
    difference: float = math.floor(order_after_tax - value_gift)
    print(f"She is left with {difference} leva.")

else:
    difference: float = math.ceil(value_gift - order_after_tax)
    print(f"She will have to borrow {difference} leva.")



