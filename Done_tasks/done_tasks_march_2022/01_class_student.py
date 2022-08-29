# Create a class Student with attributes:
# name : string
# grades : list of float numbers

# Note: The constructor of Student should only take name in its brackets and always initialize grades to an empty list

# Create a function in Student called add_grade
# The function should take one variable (that will be a float) and check if it is between 2 and 6 (including 2 and 6)
# If the value is between 2 and 6 add it to the grades list attribute

# Create a function will_pass in Student
# The function doesn't take any variables
# returns True if there are no grades in the list or the average grade is above or equal to 3

# Create a function called output in Student
# The function doesn't take any variables
# prints the name and then the grades attributes
# also prints "will pass" if his average grade score is above or equal to 3
# or "will not pass" if the average is lower than 3

# Create a program that asks the user for a command. When a command finishes he is asked for a new one.
# The program should quit when the user types "quit" as a command

# Create an empty list that will be a list of students

# Add the command "add student" that will ask for a student name and create a new student and add it to the list
# Add the command "add grade" that will ask for a student name and a grade (float) and add a grade to that student
# Add the command "list" that prints the name, grades, and wether the student will pass for all students.
import json


class Student:

    def __init__(self, name):
        self.name = name
        self.grades = []

    def add_grade(self, number):
        if 2 <= number <= 6:
            self.grades.append(number)

    def will_pass(self):
        sum_score = 0
        count = 0
        average = 0
        if len(self.grades) == 0:
            return False
        for value in self.grades:
            sum_score += value
            count += 1
        average = sum_score / count
        if average >= 3:
            return True
        else:
            return False

    def output(self):
        print(self.name)
        print(self.grades)
        will_pass_answer = self.will_pass()
        if will_pass_answer:
            print("will pass")
        else:
            print("will not pass")

    def to_dictionary(self):
        """
        This function returns a dictionary from the variable
        """
        student_dictionary = {
            "name": self.name,
            "grades": self.grades,
        }
        return student_dictionary

    def from_dictionary(self, student_dictionary):
        self.name = student_dictionary["name"]
        self.grades = student_dictionary["grades"]

menu_text = """
Insert command:
                Add students
                Add grade
                List:
                Save:
                Load:
                Quit:
"""
command = input(menu_text)

list_with_students: list[Student] = []

while command != "quit":
    if command == "add student":
        student_name = input("Name of the student: ")
        student = Student(student_name)
        list_with_students.append(student)

    elif command == "add grade":

        student_name: str = input("What is the name of the student? :")
        student_grade = float(input("What is his grade?: "))

        for person in list_with_students:  # ----> person = class
            if person.name == student_name:  # -----> person.name = the specific name atribute in the class == person
                person.add_grade(student_grade)

    elif command == "list":
        for person in list_with_students:
            person.output()

    elif command == "save":

        list_for_save: list[dict] = []
        for student in list_with_students:
            student_dictionary = student.to_dictionary()
            list_for_save.append(student_dictionary)

        json_text_with_students = json.dumps(list_for_save)
        file = open("01_class_student.json", "w")
        file.write(json_text_with_students)
        file.close()

    elif command == "load":
        file = open("01_class_student.json", "r")
        file_with_saved_data: str = file.read()
        file.close()

        saved_data: list[dict] = json.loads(file_with_saved_data)

        for saved_student_dictionary in saved_data:
            student = Student("")
            student.from_dictionary(saved_student_dictionary)
            list_with_students.append(student)

    command = input(menu_text)






