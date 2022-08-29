# ⦁	Четна / нечетна сума
# Да се напише програма, която чете n-на брой цели числа, подадени от потребителя и проверява дали сумата от
# числата на четни позиции е равна на сумата на числата на нечетни позиции.
# ⦁	Ако сумите са равни да се отпечатат два реда: "Yes" и на нов ред "Sum = " + сумата;
# ⦁	Ако сумите не са равни да се отпечат два реда: "No" и на нов ред "Diff = " + разликата.
# Разликата се изчислява по абсолютна стойност.

num_number: int = int(input())
odd: int = 0
even: int = 0

for value in range(0, num_number):
    number: int = int(input())

    if value % 2 == 0:
        even += number
    else:
        odd += number

diff: int = abs(odd - even)

if even == odd:
    print("Yes")
    print(f"Sum = {odd}")
else:
    print("No")
    print(f"Diff = {diff}")

# DONE
