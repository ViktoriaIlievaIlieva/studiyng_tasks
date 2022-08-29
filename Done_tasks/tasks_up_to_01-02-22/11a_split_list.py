# Similar to the previous task I want to see inofrmation about my grades
# I want to know which of my grades were lower than the semester grade 

# task: 
# 1. find the semester grade
# 2. copy all grades that are lower than the semester grade to the second list called bad grades

literature_grades = [3.33, 2.51, 4, 4.31, 3.14, 4.12, 3]

sum_of_grades: float = sum(literature_grades)
number_of_grades: int = len(literature_grades)
final_grade: float = sum_of_grades / number_of_grades
print(final_grade)

list_with_low_grades: list[float] = []
for low_grade in literature_grades:
    if low_grade < final_grade:
        list_with_low_grades.append(low_grade)
print(list_with_low_grades)


# DONE
  