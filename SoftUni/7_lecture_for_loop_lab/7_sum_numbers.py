# ⦁	Сумиране на числа
# Да се напише програма, която чете n-на брой цели числа, въведени от потребителя и ги сумира.
# ⦁	От първия ред на входа се въвежда броят числа n.
# ⦁	От следващите n реда се въвежда по едно цяло число.
# Програмата трябва да прочете числата, да ги сумира и да отпечата сумата им.

num_numbers: int = int(input())
number_sum: int = 0

for value in range(0, num_numbers):
    number: int = int(input())
    number_sum += number

print(number_sum)

# DONE
