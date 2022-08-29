# Similar to the previous task I want to see inofrmation about my grades
# but I want to cheat and bump my semester grade up a bit

# task: 
# 1. find the semester grade
# 2. for each grade that is lower than the semester grade I want to increase its value by 1
# 3. calculate the new semester grade after the change and print it out

literature_grades: [float] = [3.33, 2.51, 4, 4.31, 3.14, 4.12, 3]

sum_of_grades: float = sum(literature_grades)
number_of_grades: int = len(literature_grades)
final_grade: float = sum_of_grades / number_of_grades
print(final_grade)

list_with_low_grades: list[float] = []
for low_grade in literature_grades:
    if low_grade < final_grade:
        low_grade = low_grade + 1
        list_with_low_grades.append(low_grade)
print(list_with_low_grades)

list_with_high_grades: list[float] = []
for high_grades in literature_grades:
    if high_grades > final_grade:
        list_with_high_grades.append(high_grades)

list_with_all_new_grades: list[float] = [*list_with_low_grades, *list_with_high_grades]

sum_of_all_new_grades: float = sum(list_with_all_new_grades)
number_of_all_new_gardes: int = len(list_with_all_new_grades)
cheat_score:  float = sum_of_all_new_grades / number_of_all_new_gardes
print(cheat_score)

# DONE
  