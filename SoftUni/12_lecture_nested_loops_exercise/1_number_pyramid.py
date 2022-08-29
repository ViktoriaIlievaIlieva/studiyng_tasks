# ⦁	Пирамида от числа
# Напишете програма, която чете цяло число n, въведено от потребителя, и отпечатва пирамида от числа като в примерите:

number: int = int(input())

current_num: int = 1
is_current_bigger_than_number: bool = False

for row in range(0, number + 1):
    for col in range(0, row + 1):
        if current_num > number:
            is_current_bigger_than_number = True
            break
        print(str(current_num) + " ", end="")
        current_num += 1
    if is_current_bigger_than_number:
        break
    print()






