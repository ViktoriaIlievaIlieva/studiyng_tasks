# Баркод Генератор
# Техниката в магазин за коледни украси се разваля. Артикулите, които съдържат четни числа в своя баркод не могат да
# бъдат маркирани от касиерите. Вашата задача е, да напишете програма, която генерира всички баркодове,
# които НЕ съдържат четни цифри в себе си.
# Вход:
# Две четирицифрени числа, които показват обхвата на баркодовете, които трябва да промените.
# Първи ред – четирицифрено число – началото на обхвата. Цяло число в интервала [1000…9999]
# Втори ред – четирицифрено число – края на обхвата. Цяло число в интервала [1000…9999]
# Изход:
# На конзолата трябва да се отпечатат всички "баркодове", които НЕ съдържат четна цифра в себе си, разделени с интервал.

first_num: int = int(input())
second_num: int = int(input())


for number in range(first_num, second_num + 1):
    condition: bool = True
    for num in str(number):
        if int(num) % 2 == 0:
            condition = False
    if condition:
        print(number, end=" ")

    
#_____________________________
first_number = input()
second_number = input()

for num_1 in range(int(first_number[0]), int(second_number[0]) + 1):
    for num_2 in range(int(first_number[1]), int(second_number[1]) + 1):
        for num_3 in range(int(first_number[2]), int(second_number[2]) + 1):
            for num_4 in range(int(first_number[3]), int(second_number[3]) + 1):

                if num_1 % 2 != 0 and num_2 % 2 != 0 and num_3 % 2 != 0 and num_4 % 2 != 0:
                    print(f"{num_1}{num_2}{num_3}{num_4}", end=" ")

