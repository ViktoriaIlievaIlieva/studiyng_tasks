# n = input()
#
# for number in range(1, int(n) + 1):
#     list_with_number = [int(num) for num in str(number)]
#     final_number = sum(list_with_number)
#     if final_number == 5 or final_number == 7 or final_number == 11:
#         print(f"{number} -> True")
#     else:
#         print(f"{number} -> False")

n = int(input())

for num in range(1, n + 1):
    sum_of_digits = 0
    digits = num

    while digits > 0:
        sum_of_digits += digits % 10
        digits = int(digits / 10)

    if (sum_of_digits == 5) or (sum_of_digits == 7) or (sum_of_digits == 11):
        print(f"{num} -> True")
    else:
        print(f'{num} -> False')