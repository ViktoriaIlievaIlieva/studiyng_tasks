# Задача 4. Изпит
# Напишете програма, която да пресмята статистика за оценки от изпит.
# В началото програмата получава броя на студентите явили се на изпита и за всеки студент неговата оценка.
# На края програмата трябва да отпечата процента студенти с оценка между 2.00 и 2.99, между 3.00 и 3.99,
# между 4.00 и 4.99, 5.00 или повече. Също така и средния успех на изпита.
# Вход:
# От конзолата се четат:
# На първия ред – броя на студентите явили се на изпит – цяло число в интервала [1...1000]
# За всеки един студент на отделен ред – оценката от изпита – реално число в интервала [2.00...6.00]
# Изход:
# Да се отпечатат на конзолата 5 реда, които съдържат следната информация:
# "Top students: {процент студенти с успех 5.00 или повече}%"
# "Between 4.00 and 4.99: {между 4.00 и 4.99 включително}%"
# "Between 3.00 and 3.99: {между 3.00 и 3.99 включително}%"
# "Fail: {по-малко от 3.00}%"
# "Average: {среден успех}"
# Всички числа трябва да са форматирани до втория знак след десетичната запетая.


num_students = int(input())
up_to_2_99 = 0
up_to_3_99 = 0
up_to_4_99 = 0
above_5 = 0
sum_grades = 0



student = 1
while student <= num_students:
    grade = float(input())
    sum_grades += grade
    if 2 <= grade <= 2.99:
        up_to_2_99 += 1
    elif 3 <= grade <= 3.99:
        up_to_3_99 += 1
    elif 4 <= grade <= 4.99:
        up_to_4_99 += 1
    elif grade >= 5:
        above_5 += 1
    student += 1

percentage_up_to_2_99 = (up_to_2_99 / num_students) * 100
percentage_up_to_3_99 = (up_to_3_99 / num_students) * 100
percentage_up_to_4_99 = (up_to_4_99 / num_students) * 100
percentage_above_5= (above_5 / num_students) * 100

average_grade = sum_grades / num_students

print(f"Top students: {percentage_above_5:.2f}%")
print(f"Between 4.00 and 4.99: {percentage_up_to_4_99:.2f}%")
print(f"Between 3.00 and 3.99: {percentage_up_to_3_99:.2f}%")
print(f"Fail: {percentage_up_to_2_99:.2f}%")
print(f"Average: {average_grade:.2f}")


# Done - 100/100
