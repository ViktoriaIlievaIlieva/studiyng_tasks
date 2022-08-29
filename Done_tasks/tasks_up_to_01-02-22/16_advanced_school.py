# Story: The school wants to easily calculate grades
# Task: They want a script that:
# 1. Ask for an input for count of grades
# 2. Asks for input for grades so many times as the specified in step 1 number
# 3. Fills a list with those grades
# 4. Sums the grades
# 5. Divides the sum by the count of grades
# 6. Prints out the resulting semester grade


count_of_grades: str = input("How many grades you want to fill?  ")
count_of_grades: int = int(count_of_grades)
number: int = 0
list_with_grades: list[int] = []
while count_of_grades > 0 and number <= count_of_grades:
    grade: str = input("Insert grade: ")
    grade: int = int(grade)
    list_with_grades.append(grade)
    count_of_grades: int = count_of_grades - 1

sum_of_grades: int = sum(list_with_grades)
number_of_grades: int = len(list_with_grades)
semestur_result: float = sum_of_grades / number_of_grades
print(semestur_result)

# DONE
