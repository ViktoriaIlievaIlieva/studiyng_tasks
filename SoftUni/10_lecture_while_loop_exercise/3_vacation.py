# ⦁	Почивка
# Джеси е решила да събира пари за екскурзия и иска от вас да ѝ помогнете да разбере дали ще успее да събере
# необходимата сума. Тя спестява или харчи част от парите си всеки ден. Ако иска да похарчи повече от наличните си
# пари, то тя ще похарчи колкото има и ще ѝ останат 0 лева.
# Вход
# От конзолата се четат:
# ⦁	Пари, нужни за екскурзията - реално число;
# ⦁	Налични пари - реално число.
# След това многократно се четат по два реда:
# ⦁	Вид действие – текст с две възможности: "spend" или "save";
# ⦁	Сумата, която ще спести/похарчи - реално число.
# Изход
# Програмата трябва да приключи при следните случаи:
# ⦁	Ако 5 последователни дни Джеси само харчи, на конзолата да се изпише:
# ⦁	"You can't save the money."
# ⦁	"{Общ брой изминали дни}"
# ⦁	Ако Джеси събере парите за почивката, на конзолата се изписва:
# ⦁	"You saved the money for {общ брой изминали дни} days."


money_for_trip: float = float(input())
current_money: float = float(input())

proces: bool = True
days: int = 0
spend_days: int = 0

while proces:
    action: str = input()
    suma: float = float(input())
    days += 1
    if action == "spend":
        if suma < current_money:
            current_money -= suma
        elif suma >= current_money:
            current_money = 0
        spend_days += 1
        if spend_days == 5:
            print("You can't save the money.")
            print(f"{days}")
            proces = False

    elif action == "save":
        current_money += suma
        spend_days = 0

    if current_money >= money_for_trip:
        print(f"You saved the money for {days} days.")
        proces = False

# DONE
