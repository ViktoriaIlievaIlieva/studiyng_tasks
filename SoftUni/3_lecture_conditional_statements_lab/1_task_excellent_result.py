# Отлична оценка
# Първата задача от тази тема е да се напише конзолна програма, която чете оценка (реално число),
# въведена от потребителя и отпечатва "Excellent!", ако оценката е 5.50 или по-висока.

grade: float = float(input())
if grade >= 5.50:
    print("Excellent!")

# Variant 2

print("Excellent!" if grade >= 5.50 else "")
