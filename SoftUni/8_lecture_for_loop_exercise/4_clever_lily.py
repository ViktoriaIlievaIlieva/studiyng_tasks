# ⦁	Умната Лили
# Лили вече е на N години. За всеки свой рожден ден тя получава подарък.
# ⦁	За нечетните рождени дни (1, 3, 5...n) получава играчки.
# ⦁	За четните рождени дни (2, 4, 6...n) получава пари.
# За втория рожден ден получава 10.00 лв, като сумата се увеличава с 10.00 лв., за всеки следващ четен рожден ден
# (2 -> 10, 4 -> 20, 6 -> 30...и т.н.). През годините Лили тайно е спестявала парите. Братът на Лили, в годините,
# които тя получава пари, взима по 1.00 лев от тях. Лили продала играчките получени през годините, всяка за P лева и
# добавила сумата към спестените пари. С парите искала да си купи пералня за X лева. Напишете програма, която да
# пресмята, колко пари е събрала и дали ѝ стигат да си купи пералня.
# Вход
# Програмата прочита 3 числа, въведени от потребителя, на отделни редове:
# ⦁	Възрастта на Лили - цяло число в интервала [1...77]
# ⦁	Цената на пералнята - число в интервала [1.00...10 000.00]
# ⦁	Единична цена на играчка - цяло число в интервала [0...40]
# Изход
# Да се отпечата на конзолата един ред:
# ⦁	Ако парите на Лили са достатъчни:
# ⦁	"Yes! {N}" - където N е остатъка пари след покупката
# ⦁	Ако парите не са достатъчни:
# ⦁	"No! {М}" - където M е сумата, която не достига
# Числата N и M трябва да за форматирани до вторият знак след десетичната запетая.


lily_age: int = int(input())
price_machine: float = float(input())
price_toy: int = int(input())

toys: int = 0
money: float = 0
even_years: int = 0

for years in range(1, lily_age + 1):
    if years % 2 == 0 and years >= 0:
        even_years += 1
        money += (10 * even_years)
    else:
        toys += 1

money_toys: int = toys * price_toy
saved_money: float = (money_toys + money) - even_years

diff: float = abs(saved_money - price_machine)

if saved_money >= price_machine:
    print(f"Yes! {diff:.2f}")
else:
    print(f"No! {diff:.2f}")

# DONE
