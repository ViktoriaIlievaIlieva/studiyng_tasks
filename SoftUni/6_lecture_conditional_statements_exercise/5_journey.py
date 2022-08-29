# ⦁	Пътешествие
# приема на входа бюджета и сезона, а на изхода да изкарва къде ще почива програмистът и колко ще похарчи.
# Бюджетът определя дестинацията, а сезонът - колко от бюджета ще изхарчи. Ако е лято ще почива на къмпинг, а зимата
# в хотел. Ако е в Европа, независимо от сезона, ще почива в хотел. Всеки къмпинг или хотел, според дестинацията, има
# собствена цена, която отговаря на даден процент от бюджета:
# ⦁	При 100 лв. или по-малко - някъде в България:
# ⦁	Лято - 30% от бюджета;
# ⦁	Зима - 70% от бюджета.
# ⦁	При 1000 лв. или по малко - някъде на Балканите:
# ⦁	Лято - 40% от бюджета;
# ⦁	Зима - 80% от бюджета.
# ⦁	При повече от 1000 лв. - някъде из Европа:
# ⦁	При пътуване из Европа, независимо от сезона, ще похарчи 90% от бюджета.
# Вход
# Входът се чете от конзолата и се състои от два реда, въведени от потребителя:
# ⦁	Бюджет - реално число;
# ⦁	Един от двата възможни сезона - "summer” или "winter”.
# Изход
# На конзолата трябва да се отпечатат два реда:
# ⦁	 "Somewhere in [дестинация]" измежду "Bulgaria", "Balkans" и "Europe"
# ⦁	"{Вид почивка} - {Похарчена сума}":
# ⦁	Почивката може да е между "Camp" и "Hotel"
# ⦁	Сумата трябва да бъде форматирана с точност до вторият знак след десетичната запетая

budget: float = float(input())
season: str = str(input())
destination: str = ""
place: str = ""
spend: float = 0

if season == "summer":
    if budget <= 100:
        spend = budget * 0.3
        destination = "Bulgaria"
    elif 101 <= budget <= 1000:
        spend = budget * 0.4
        destination = "Balkans"
    elif budget > 1000:
        spend = budget * 0.9
        destination = "Europe"

elif season == "winter":
    if budget <= 100:
        spend = budget * 0.7
        destination = "Bulgaria"
    elif 101 <= budget <= 1000:
        spend = budget * 0.8
        destination = "Balkans"
    elif budget > 1000:
        spend = budget * 0.9
        destination = "Europe"

if season == "summer" and destination != "Europe":
    place = "Camp"
elif season == "winter" or destination == "Europe":
    place = "Hotel"

print(f"Somewhere in {destination}")
print(f"{place} - {spend:.2f}")

# DONE
