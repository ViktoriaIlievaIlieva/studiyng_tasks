# Калкулатор депозити
# Напишете програма, която изчислява каква сума ще получите в края на депозитния период при определен лихвен процент.
# Използвайте следната формула:  сума = депозирана сума  + срок на депозита * ((депозирана сума * годишен лихвен процент ) / 12)
#Вход - От конзолата се четат 3 реда:
# Депозирана сума – реално число в интервала [100.00 … 10000.00]
# Срок на депозита (в месеци) – цяло число в интервала [1…12]
# Годишен лихвен процент – реално число в интервала [0.00 …100.00]
# Изход
# Да се отпечата на конзолата сумата в края на срока.

deposit = float(input())
deposit_length = int(input())
percentage = float(input())
interest_percentage = percentage /100
price = deposit + deposit_length * ((deposit * interest_percentage) / 12)

print(price)


