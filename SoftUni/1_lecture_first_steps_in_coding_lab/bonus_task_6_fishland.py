#Георги ще има гости вечерта и решава да ги нагости с паламуд, сафрид и миди. Затова отива на рибната борса, за да си
# купи по няколко килограма. Oт конзолата се въвеждат цените в лева на скумрията и цацата.
# Също количеството на паламуд, сафрид и миди в килограми. Колко пари ще са му необходими, за да плати сметката си, ако цените на борсата са:
# ⦁	Паламуд – 60% по-скъп от скумрията
# ⦁	Сафрид – 80% по-скъп от цацата
# ⦁	Миди – 7.50 лв. за килограм
# Вход - от конзолата се четат 5 числа:
# ⦁	Първи ред – цена на скумрията на килограм. Реално число в интервала [0.00…40.00]
# ⦁	Втори ред – цена на цацата на килограм. Реално число в интервала [0.00…30.00]
# ⦁	Трети ред – килограма паламуд. Реално число в интервала [0.00…50.00]
# ⦁	Четвърти ред – килограма сафрид. Реално число в интервала [0.00… 70.00]
# ⦁	Пети ред – килограма миди. Цяло число в интервала [0 ... 100]
# Изход
# Да се отпечата на конзолата едно число с плаваща запетая: колко пари ще са нужни на Георги, за да си плати сметката.
# Числото трябва да е форматирано до вторият знак след десетичната запетая (1.2457 -> 1.25).

price_skumria = float (input())
price_caca = float (input())

kg_palmud = float (input())
kg_safrid = float (input())
kg_midi = int (input())

price_palamud = price_skumria/ 100 * 60 + price_skumria
price_safrid = price_caca /  100 * 80 + price_caca
price_midi = 7.50

final_cost = kg_palmud * price_palamud + kg_safrid * price_safrid + kg_midi * price_midi
print (format (final_cost, ".2f"))