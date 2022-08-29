# Задача 3. Калкулатор за екскурзии
# Туристическа агенция предлага екскурзии на различни цени, според сезона и броя на хората.
# Напишете програма, която да изчислява цената, според данните от таблицата:
# 	                Пролет (spring)	            Лято (summer)	        Есен (autumn)	                Зима (winter)
#   До 5 човека	    50.00 лв. на човек	        48.50 лв. на човек	    60.00 лв. на човек	            86.00 лв. на човек
#   Над 5 човека	48.00 лв. на човек	        45.00 лв. на човек	    49.50 лв. на човек	            85.00 лв. на човек

# В зависимост от сезона, може да има отстъпка или оскъпяване на цената, съответно:
# При "summer" -> 15% отстъпка
# При "winter" -> 8% оскъпяване

# Вход:
# Първи ред – брой хора – цяло число в интервала [1 … 20]
# Втори ред – сезон – текст с възможности - "spring", "summer", "autumn" или "winter"

# Изход:
#    На конзолата се отпечатва 1 ред:
#  •   Цената за екскурзията, форматирана до втория знак след десетичния разделител, в следния формат: "{цената} leva."

num_people = int(input())
season = input()
price = 0

if season == "spring":
    if num_people <= 5:
        price = num_people * 50
    elif num_people > 5:
        price = num_people * 48
elif season == "summer":
    if num_people <= 5:
        price = num_people * 48.50
    elif num_people > 5:
        price = num_people * 45

    price = price - (price * 0.15)

elif season == "autumn":
    if num_people <= 5:
        price = num_people * 60
    elif num_people > 5:
        price = num_people * 49.50
elif season == "winter":
    if num_people <= 5:
        price = num_people * 86
    elif num_people > 5:
        price = num_people * 85

    price = price + (price * 0.08)

print(f"{price:.2f} leva.")


# Done - 100/100
