# Create a class Class. The __init__ method should receive the name of the class.
# Each class should also have 2 empty lists - students and grades.
# Create a class attribute __students_count equal to 22.
# The class should also have 3 additional methods:
# add_student(name: str, grade: float) - adds the student and the grade in the two lists if there is free space in the
# class
# get_average_grade() - returns the average of all existing grades formatted to the second decimal point (as a number)
# __repr__ - returns the string (single line):
# "The students in {class_name}: {students}. Average grade: {average_grade}".
# The students must be separated by a comma and a space: ", ".

class Class:
    def __init__(self, name: str):
        self.name = name
        self.students: list = []
        self.grades: list = []
        self.__students_count: int = 22

    def add_student(self, name: str, grade: float):
        if self.__students_count > 0:
            self.students.append(name)
            self.grades.append(grade)
            self.__students_count -= 1

    def get_average_grade(self) -> float:
        average_grade: float = sum(self.grades) / len(self.grades)
        return average_grade


# вариант 1
    def __repr__(self) -> str:
        students = ""
        students += self.students[0]
        student = 1
        while 1 <= student < len(self.students):
            students = students + ", " + self.students[student]
            student += 1
        return f"The students in {self.name}: {students}. Average grade: {self.get_average_grade():.2f}"

# вариант 2
    def __repr__(self) -> str:
        students = ", ".join(self.students)
        return f"The students in {self.name}: {students}. Average grade: {self.get_average_grade():.2f}"



a_class = Class("11B")
a_class.add_student("Peter", 4.80)
a_class.add_student("George", 6.00)
a_class.add_student("Amy", 3.50)
print(a_class)