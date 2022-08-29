# Приход на агенция
# Напишете програма, която изчислява печалбата на агенция за продажба на самолетни билети.
# Агенцията продава самолетни билети на различни авиокомпании. Ще получите информация за броя продадени билети за
# възрастни и броя продадени детски билети. Нетната цена на билета за възрастен се определя от авиокомпанията,
# а детският билет е със 70% по-евтин. Агенцията добавя към нетната цена на всеки билет такса обслужване.
# Крайната печалба на Агенцията е 20% от общата цена на всички билети.
# Вход:
# От конзолата се четат 5 реда:
# Име на авиокомпанията - текст
# Брой билети за	 възрастни – цяло число в диапазона [1…400]
# Брой детски билети – цяло число в диапазона [25…120]
# Нетна цена на билет за възрастен – реално число в диапазона [100.0…1600.0]
# Цената на такса обслужване - реално число в диапазона [10.0…50.0]
# Изход:
# Да се отпечата на конзолата крайната печалбата от продажбите, в следния формат:
# "The profit of your agency from {име на авиокомпанията} tickets is {печалба за агенцията} lv."
# Цената на печалбата да бъде форматирана до втората цифра след десетичния знак.

name: str = input()
num_tickets_adults: int = int(input())
num_tickets_kids: int = int(input())

price_ticket_adult: float = float(input())
service_price: float = float(input())
price_ticket_kid: float = price_ticket_adult * 0.30

suma_tickets_adults: float = (num_tickets_adults * price_ticket_adult) + (num_tickets_adults * service_price)
suma_tickets_kids: float = (num_tickets_kids * price_ticket_kid) + (num_tickets_kids * service_price)

suma_all_tickets: float = suma_tickets_kids + suma_tickets_adults
profit: float = suma_all_tickets * 0.20

print(f"The profit of your agency from {name} tickets is {profit:.2f} lv.")



