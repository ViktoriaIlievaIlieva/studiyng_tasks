# Резервоар за гориво -  част 2
# Напишете програма, която да изчислява, колко ще струва на един шофьор да напълни резервоара на автомобила си,
# като знаете – какъв тип гориво зарежда, каква е цената за литър гориво и дали разполага с карта за отстъпки.
# Цените на горивата са както следва:
# Бензин – 2.22 лева за един литър,
# Дизел – 2.33 лева за един литър
# Газ – 0.93 лева за литър
# Ако водача има карта за отстъпки,  той се възползва от следните намаления за литър гориво: 18 ст. за литър бензин,
# 12 ст. за литър дизел и 8 ст. за литър газ.

# Ако шофьора е заредил между 20 и 25 литра включително, той получава 8 процента отстъпка от крайната цена, при повече
# от 25 литра гориво, той получава 10 процента отстъпка от крайната цена.

# Вход
# Входът се чете от конзолата и се състои от 3 реда:
# Типа на горивото – текст с възможности: "Gas", "Gasoline" или "Diesel"
# Количество гориво – реално число в интервала [1.00 … 50.00]
# Притежание на клубна карта – текст с възможности: "Yes" или "No"

# Изход
# На конзолата трябва да се отпечата един ред.
# "{крайната цена на горивото} lv."
# Цената на горивото да бъде форматираната до втората цифра след десетичния знак.


type_fuel: str = input()
liters_in_fuel: float = float(input())
club_card: str = input()

gasoline = 2.22 * liters_in_fuel
gas = 0.93 * liters_in_fuel
diesel = 2.33 * liters_in_fuel
end_price = 0

if club_card == "Yes":
    if type_fuel == "Gas":
        end_price = gas - (0.08 * liters_in_fuel)

    elif type_fuel == "Gasoline":
        end_price = gasoline - (0.18 * liters_in_fuel)

    elif type_fuel == "Diesel":
        end_price = diesel - (0.12 * liters_in_fuel)
else:
    if type_fuel == "Gas":
        end_price = gas

    elif type_fuel == "Gasoline":
        end_price = gasoline

    elif type_fuel == "Diesel":
        end_price = diesel


if 20 <= liters_in_fuel <= 25:
    end_price = end_price - ((end_price/100) * 8)
    print(f"{end_price:.2f} lv.")
elif liters_in_fuel > 25:
    end_price = end_price - ((end_price/100) * 10)
    print(f"{end_price:.2f} lv.")
elif liters_in_fuel < 20:
    print(f"{end_price:.2f} lv.")

