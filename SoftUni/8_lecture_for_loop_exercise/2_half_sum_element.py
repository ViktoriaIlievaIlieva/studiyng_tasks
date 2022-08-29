# Елемент, равен на сумата на останалите
# Да се напише програма, която чете n-на брой цели числа, въведени от потребителя,и проверява дали сред тях съществува
# число, което е равно на сумата на всички останали.
# ⦁	Ако има такъв елемент печата "Yes" и на нов ред "Sum = "  + неговата стойност
# ⦁	Ако няма такъв елемент печата "No" и на нов ред "Diff = " + разликата между най-големия елемент и сумата на
# останалите (по абсолютна стойност)


num_numbers: int = int(input())
highest_number: int = - 9223372036854775807
suma: int = 0

for value in range(0, num_numbers):
    number: int = int(input())
    suma += number
    if number > highest_number:
        highest_number = number

suma -= highest_number

diff: int = abs(suma - highest_number)

if highest_number == suma:
    print("Yes")
    print(f"Sum = {suma}")

else:
    print("No")
    print(f"Diff = {diff}")

# DONE
