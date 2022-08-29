# Да се напише програма, която чете 2 * n-на брой цели числа, подадени от потребителя, и проверява дали сумата на
# първите n числа (лява сума) е равна на сумата на вторите n числа (дясна сума). При равенство печата
# " Yes, sum = " + сумата; иначе печата " No, diff = " + разликата.
# Разликата се изчислява като положително число (по абсолютна стойност).

num: int = int(input())
sum_1: int = 0
sum_2: int = 0

for _ in range(0, num):
    number_1: int = int(input())
    sum_1 += number_1

for _ in range(0, num):
    number_2: int = int(input())
    sum_2 += number_2

diff: int = abs(sum_1 - sum_2)

if sum_1 == sum_2:
    print(f" Yes, sum = {sum_1}")
else:
    print(f" No, diff = {diff}")

# DONE
