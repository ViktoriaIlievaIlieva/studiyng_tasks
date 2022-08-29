# ⦁	Еднакви суми на четни и нечетни позиции
# Напишете програма, която чете от конзолата две шестцифрени цели числа.
# Винаги първото въведено число ще бъде по-малко от второто.
# На конзолата да се отпечатат на 1, ред разделени с интервал, всички числа, които се намират между двете,
# прочетени от конзолата числа и отговарят на условието сумата от цифрите на четни и нечетни позиции да са равни.
# Ако няма числа, отговарящи на условието на конзолата не се извежда резултат.

number_1: int = int(input())
number_2: int = int(input())

for number in range(number_1, number_2 + 1):
    list_with_sep_numbers: list = [int(a) for a in str(number)]
    odd_num: int = 0
    even_num: int = 0
    index = 0
    while index < len(list_with_sep_numbers):
        if index % 2 == 0:
            even_num += list_with_sep_numbers[index]
        else:
            odd_num += list_with_sep_numbers[index]
        index += 1
    if odd_num == even_num:
        print(number, end=" ")



#-------------------

number_1: int = int(input())
number_2: int = int(input())

for number in range(number_1, number_2 + 1):
    num_to_str: str = str(number)
    odd_num: int = 0
    even_num: int = 0
    for index, digit in enumerate(num_to_str):
        if index % 2 == 0:
            even_num += int(digit)
        else:
            odd_num += int(digit)


    if odd_num == even_num:
        print(number, end=" ")

# ------------------------------

list_test = [1, 2, 3, 4]

list_test_str = [str(number) for number in list_test]

list_test_str = []
for number in list_test:
    list_test_str.append(str(number))


# ------------------------------

list_test = [1, 2, 3, 4]

list_test_str = [number for number in list_test if number % 2 == 0]

list_test_str = []
for number in list_test:
    if number % 2 == 0:
        list_test_str.append(number)


