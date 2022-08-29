#
# class Student:
#
#     def __init__(self, name):
#         self.name = name
#         self.grades = []
#
#     def add_grade(self, number):
#         if 2 <= number <= 6:
#             self.grades.append(number)

class Person:

    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_name(self, new_value):
        if len(new_value) > 0:
            self.__name = new_value

    def print_name(self):
        print(self.__name)


class Student(Person):

    def __init__(self, name):
        Person.__init__(self, name)
        self.grades = []

    def print_info(self):
        self.print_name()
        print(self.grades)


x = Student("Bob")
x.print_name()
x.set_name("")
x.get_name()

def my_function(person: Person):
    pass

my_function(x)