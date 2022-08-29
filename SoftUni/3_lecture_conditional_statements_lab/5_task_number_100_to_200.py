# Число от 100 до 200
# Да се напише програма, която чете цяло число, въведено от потребителя и проверява дали е под 100, между 100 и 200 или
# над 200. Ако числото е:
# под 100 отпечатайте: "Less than 100"
# между 100 и 200 отпечатайте: "Between 100 and 200"
# над 200 отпечатайте: "Greater than 200"

x: int = int(input())
if x < 100:
    print("Less than 100")
elif 100 <= x <= 200:
    print("Between 100 and 200")
else:
    print("Greater than 200")


# variant 2

x: int = int(input())
print("Less than 100" if x < 100 else ("Between 100 and 200" if 100 <= x <= 200 else "Greater than 200"))

