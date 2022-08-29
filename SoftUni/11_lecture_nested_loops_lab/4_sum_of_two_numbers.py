# ⦁	Сума от две числа - Напишете програма която проверява всички възможни комбинации от двойка числа в интервала
# от две дадени числа. На изхода се отпечатва, коя поред е комбинацията чиито сбор от числата е равен на дадено
# магическо число. Ако няма нито една комбинация отговаряща на условието се отпечатва съобщение, че не е намерено.
# Вход
# Входът се чете от конзолата и се състои от три реда:
# ⦁	Първи ред – начало на интервала – цяло число в интервала [1...999]
# ⦁	Втори ред – край на интервала – цяло число в интервала [по-голямо от първото число...1000]
# ⦁	Трети ред – магическото число – цяло число в интервала [1...10000]
# Изход
# На конзолата трябва да се отпечата един ред, според резултата:
# ⦁	Ако е намерена комбинация чиито сбор на числата е равен на магическото число
# ⦁	"Combination N:{пореден номер} ({първото число} + {второ число} = {магическото число})"
# ⦁	Ако не е намерена комбинация отговаряща на условието
# ⦁	"{броят на всички комбинации} combinations - neither equals {магическото число}"


start: int = int(input())
end: int = int(input())
magic_num: int = int(input())
combination: int = 0
found: bool = False


for num_1 in range(start, end + 1):
    for num_2 in range(start, end + 1):
        combination += 1
        if num_1 + num_2 == magic_num:
            print(f"Combination N:{combination} ({num_1} + {num_2} = {magic_num})")
            found = True
            break
    if found:
        break

if not found:
    print(f"{combination} combinations - neither equals {magic_num}")


# ---------------------


start: int = int(input())
end: int = int(input())
magic_num: int = int(input())
combination: int = 0
found: bool = False


num_1 = start
while num_1 < end + 1 and not found:
    num_2 = start
    while num_2 < end + 1 and not found:

        if num_1 + num_2 == magic_num:
            print(f"Combination N:{combination} ({num_1} + {num_2} = {magic_num})")
            found = True

        num_2 += 1
    num_1 += 1

# ---------------------------


def find_combination(start: int, end: int, magic_num: int) -> bool:
    combination = 0

    for num_1 in range(start, end + 1):
        for num_2 in range(start, end + 1):
            combination += 1
            if num_1 + num_2 == magic_num:
                print(f"Combination N:{combination} ({num_1} + {num_2} = {magic_num})")
                return True

    return False


start: int = int(input())
end: int = int(input())
magic_num: int = int(input())

if not find_combination(start, end, magic_num):
    print(f"{combination} combinations - neither equals {magic_num}")