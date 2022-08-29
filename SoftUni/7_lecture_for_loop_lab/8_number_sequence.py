# ⦁	Редица цели числа
# Напишете програма, която чете n на брой цели числа. Принтирайте най-голямото и най-малкото число сред въведените.

num_numbers: int = int(input())
biggest_num: int = - 9223372036854775807
lowest_num: int = 9223372036854775807
for value in range(0, num_numbers):
    number: int = int(input())
    if number >= biggest_num:
        biggest_num = number
    if number <= lowest_num:
        lowest_num = number

print(f"Max number: {biggest_num}")
print(f"Min number: {lowest_num}")

# DONE
