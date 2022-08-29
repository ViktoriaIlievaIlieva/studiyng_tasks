# Лятно облекло
# Лятото е сезон с много променливо време и Виктор има нужда от вашата помощ. Напишете програма, която спрямо времето
# от денонощието и градусите да препоръча на Виктор какви дрехи да облече. Вашият приятел има различни планове за всеки
# етап от деня, които изискват и различен външен вид - може да ги видите от таблицата.
# От конзолата се четат точно два реда:
# ⦁	Градусите - цяло число;
# ⦁	Време от денонощието - текст с три възможности "Morning", "Afternoon" или "Evening".
#
# Като изход да се отпечата на конзолата на един ред: "It's {градуси} degrees, get your {облекло} and {обувки}."

degrees: int = int(input())
time: str = input()

shoes = ""
outfit = ""

if 10 <= degrees <= 18:

    if time == "Morning":
        shoes = "Sneakers"
        outfit = "Sweatshirt"

    elif time == "Afternoon":
        shoes = "Moccasins"
        outfit = "Shirt"

    elif time == "Evening":
        shoes = "Moccasins"
        outfit = "Shirt"

elif 18 < degrees <= 24:

    if time == "Morning":
        shoes = "Moccasins"
        outfit = "Shirt"

    elif time == "Afternoon":
        shoes = "Sandals"
        outfit = "T-Shirt"

    elif time == "Evening":
        shoes = "Moccasins"
        outfit = "Shirt"

elif degrees >= 25:

    if time == "Morning":
        shoes = "Sandals"
        outfit = "T-Shirt"

    elif time == "Afternoon":
        shoes = "Barefoot"
        outfit = "Swim Suit"

    elif time == "Evening":
        shoes = "Moccasins"
        outfit = "Shirt"

print(f"It's {degrees} degrees, get your {outfit} and {shoes}.")

# DONE
