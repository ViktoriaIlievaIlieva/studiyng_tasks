# Задача 2. Моминско парти
# Михаела държи сама да организира и заплати моминското си парти.
# Тя планува плащането да стане с приходите от онлайн магазина й.
# Да се напише програма, която пресмята печалбата от продажбите й.
# Цени на различните артикули:
# Любовно послание - 0.60 лв.
# Восъчна роза - 7.20 лв.
# Ключодържател - 3.60 лв.
# Карикатура - 18.20 лв.
# Късмет изненада - 22 лв.
# Ако поръчаните артикули са 25 или повече магазинът прави отстъпка 35% от общата цена.
# От спечелените пари Михаела трябва да предвиди и 10% разход за хостинг.
# Да се пресметне дали парите ще й стигнат да си плати моминското парти.
# Вход
# От конзолата се четат 6 реда:
# Цена на моминското парти - реално число в интервала [1.00 … 10000.00]
# Брой любовни послания - цяло число в интервала [0… 1000]
# Брой восъчни рози - цяло число в интервала [0 … 1000]
# Брой ключодържатели - цяло число в интервала [0 … 1000]
# Брой карикатури - цяло число в интервала [0 … 1000]
# Брой късмети изненада - цяло число в интервала [0 … 1000]
# Изход
# На конзолата се отпечатва:
# Ако парите са достатъчни се отпечатва:
# "Yes! {оставащите пари} lv left."
# Ако парите НЕ са достатъчни се отпечатва:
# "Not enough money! {недостигащите пари} lv needed."
# Резултатът трябва да се форматира до втория знак след десетичната запетая.


price_party = float(input())
num_love_dedications = int(input())
num_roses = int(input())
num_key_chains = int(input())
num_painting = int(input())
num_charms = int(input())


money_love_dedications = num_love_dedications * 0.60
money_roses = num_roses * 7.20
money_key_chains = num_key_chains * 3.60
money_paintings = num_painting * 18.20
money_charms = num_charms * 22

all_money = money_roses + money_love_dedications + money_key_chains + money_paintings + money_charms
num_all_products = num_love_dedications + num_roses + num_key_chains + num_painting + num_charms

if num_all_products >= 25:
    all_money = all_money - (all_money * 0.35)

all_money = all_money - (all_money * 0.10)

diff = abs(all_money - price_party)

if all_money >= price_party:
    print(f"Yes! {diff:.2f} lv left.")
else:
    print(f"Not enough money! {diff:.2f} lv needed.")


# Done - 100/100

