# ⦁	7. Пазаруване
# Петър иска да купи N видеокарти, M процесора и P на брой рам памет. Ако броя на видеокартите е по-голям от този на
# процесорите получава 15% отстъпка от крайната сметка. Важат следните цени:
# ⦁	Видеокарта – 250 лв./бр.
# ⦁	Процесор – 35% от цената на закупените видеокарти/бр.
# ⦁	Рам памет – 10% от цената на закупените видеокарти/бр.
# Да се изчисли нужната сума за закупуване на материалите и да се пресметне дали бюджета ще му стигне.
# Вход
# Входът се състои от четири реда:
# ⦁	Бюджетът на Петър - реално число в интервала [1.0…100000.0]
# ⦁	Броят видеокарти - цяло число в интервала [1…100]
# ⦁	Броят процесори - цяло число в интервала [1…100]
# ⦁	Броят рам памет - цяло число в интервала [1…100]
# Изход
# На конзолата се отпечатва 1 ред, който трябва да изглежда по следния начин:
# ⦁	Ако бюджета е достатъчен:
# "You have {остатъчен бюджет} leva left!"
# ⦁	Ако сумата надхвърля бюджета:
# "Not enough money! You need {нужна сума} leva more!"
# Резултатът да се форматира до втория знак след десетичната запетая.

budget: float = float(input())
num_video_cards: int = int(input())
num_processors: int = int(input())
num_ram: int = int(input())

video_card: int = 250
price_video_cards: int = video_card * num_video_cards

processor: float = price_video_cards * 0.35
price_processor: float = processor * num_processors

ram: float = price_video_cards * 0.10
price_ram: float = ram * num_ram

final_price = price_ram + price_video_cards + price_processor

if num_video_cards > num_processors:
    final_price -= final_price * 0.15

dif: float = abs(final_price - budget)

if final_price <= budget:
    print(f"You have {dif:.2f} leva left!")
else:
    print(f"Not enough money! You need {dif:.2f} leva more!")

# DONE
