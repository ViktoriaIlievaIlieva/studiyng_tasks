# In school we calculated our end of the year grade by:
# summing all of our grades and after that dividing them by their number

# Example if on math I had: 3.45, 5.55, 4
# For the end of the year I would sum all of them: 3.45 + 4.55 + 4 = 12
# Then to get my semester grade I would also do: 12 / 3 = 4

# Vidas used to give us a lot of grades every year
# task: calculate and print my semester grade using a program

literature_grades: list[float] = [3.33, 2.51, 4, 4.31, 3.14, 4.12, 3]

sum_of_grades: float = sum(literature_grades)
number_of_grades: float = len(literature_grades)
final_grade: float = sum_of_grades / number_of_grades
print(final_grade)


# DONE
  