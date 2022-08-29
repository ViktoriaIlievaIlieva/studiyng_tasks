# Алуминиева дограма
# Фирма-производител на алуминиева дограма приема поръчки за изработката и монтаж със следния ценоразпис за един брой.
# Фирмата приема само поръчки на едро (над 10 бр.). В зависимост от поръчания брой дограми, фирмата прави различна
# отстъпка на своите клиенти.

# Фирмата предлага също и доставка на поръчките си срещу 60 лв.

# Размер	            Единична цена	            Отстъпка от цената
# 90X130	            110 лв.	                    Над 30 броя – 5%
#                                                   Над 60 броя – 8%

# 100X150	            140 лв.	                    Над 40 броя – 6%
#                                                   Над 80 броя – 10%

# 130X180	            190 лв.	                    Над 20 броя – 7%
#                                                   Над 50 броя – 12%

# 200X300	            250 лв.	                    Над 25 броя – 9%
#                                                   Над 50 броя – 14%

# Ако поръчката надвишава 99 броя  – върху крайната цена се начисляват допълнителни 4% отстъпка (след като се начисли
# цената за доставка, ако има такава).
# При поръчка под 10 бр. на конзолата да бъде изписано "Invalid order"

# Вход:
# Потребителят въвежда 3 реда:
# Брой дограми – цяло число в интервала [0..1000];
# Вид на дограмите – текст "90X130" или "100X150" или "130X180" или "200X300";
# Начин на получаване – текст
# С доставка - "With delivery"
# Без доставка - "Without delivery"

# Изход:
# Извежда се едно число – стойността на поръчката, в следния формат:
# "{Обща стойност на поръчката} BGN"
# Резултатът да се форматира до втори знак след десетичната запетая.

num_doors: int = int(input())
type_doors: str = input()
delivery: str = input()
price: float = 0

if num_doors < 10:
    print("Invalid order")

elif num_doors >= 10:
    if type_doors == "100X150":
        if 10 < num_doors <= 40:
            price = num_doors * 140
        elif 40 < num_doors <= 80:
            price = num_doors * 140
            price = price - (price * 0.06)
        elif num_doors > 80:
            price = num_doors * 140
            price = price - (price * 0.10)

    elif type_doors == "90X130":
        if 10 < num_doors <= 30:
            price = num_doors * 110
        elif 30 < num_doors <= 60:
            price = num_doors * 110
            price = price - (price * 0.05)
        elif num_doors > 60:
            price = num_doors * 110
            price = price - (price * 0.08)

    elif type_doors == "130X180":
        if 10 < num_doors <= 20:
            price = num_doors * 190
        elif 20 < num_doors <= 50:
            price = num_doors * 190
            price = price - (price * 0.07)
        elif num_doors > 50:
            price = num_doors * 190
            price = price - (price * 0.12)

    elif type_doors == "200X300":
        if 10 < num_doors <= 25:
            price = num_doors * 250
        elif 25 < num_doors <= 50:
            price = num_doors * 250
            price = price - (price * 0.09)
        elif num_doors > 50:
            price = num_doors * 250
            price = price - (price * 0.14)

    if delivery == "With delivery":
        price += 60

    if num_doors > 99:
        price = price - (price * 0.04)

    print(f"{price:.2f} BGN")

