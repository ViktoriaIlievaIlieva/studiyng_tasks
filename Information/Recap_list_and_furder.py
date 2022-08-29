
#
# x: int = 5
#
# h = []
# h.append(5)
# h.append("asdf")
#
# h.insert(5, "stoinost")
#
# h.remove("stoinost")
#
# y = h[0] * 6
#
# p = [4, 5, 6]
# h.extend(p)
#
# my_dictionary: dict = {"new_key": 6}
#
#
# my_dictionary: dict = {"new_key": {"a": 5, "b": 6},
#                        "old_key": {"a": 5, "b": 6}}
#
# print(my_dictionary)
#
# b = my_dictionary["new_key"]["b"]
#
# if "new_key" in my_dictionary and "b" in my_dictionary["new_key"]:
#     b = my_dictionary["new_key"]["b"]
#
# family: dict = {}
# num_members = int(input("Enter count: "))
#
# for _ in range(0, num_members):
#     member = input("Enter name: ")
#     age = input("Enter age: ")
#     height = input("Enter height: ")
#     weight = input("Enter weight: ")
#
#     family_member = {
#         "age": age,
#         "height": height,
#         "weight": weight,
#     }
#
#     family[member] = family_member
#
# family: dict = {}
# num_members = int(input("Enter count: "))
#
# for _ in range(0, num_members):
#     member = input("Enter name: ")
#     age = input("Enter age: ")
#     height = input("Enter height: ")
#     weight = input("Enter weight: ")
#
#
# family = {
#     "names": {}
#
# }

health_test_viki = {"endokrinolog": "10.03.22", "eyes": "12.02.23", "hart": "15.06.24"}


for _ in range(0, 2):
    patient_name = input("Patient name:")
    age = int(input("Age: "))
    type_check_up = input("Type doctor: ")
    date = input(" Date: ")

    patient_record = {
        "name": patient_name,
        "age": age,
        "type_check_up": type_check_up,
        "date": date,
    }

print(patient_record)


weather_report: dict = {
    "sofia": {
        "morning": -5.0,
        "evening": 10.0
    },
}

for _ in range(0, 2):
    city_name = input("City name:")
    morning = float(input("Enter report for the morning: "))
    evening = float(input("Enter report for the evening: "))

    city_report = {
        "morning": morning,
        "evening": evening,
    }

    weather_report[city_name] = city_report

print(weather_report)


class Students:
    def __init__(self ):
        self.list_students = {"viki": [3,4,5], "ico": [4,4,5], "deni": [3,3,3]}

    def final_grades(self, student):
        grades = self.list_students[student]
        average_grade = sum(grades) / len(grades)
        print(average_grade)


students_variable = Students()
student = input("Name student")

students_variable.final_grades(student)


def final_grades(grade):
    grades = [grade]
    average_grade = sum(grades) / len(grades)
    return average_grade


for grade in range(2, 7):
    all_grades_average = final_grades(grade)




my_list: list = []
my_list_2: list = [1, 2, 3]

class User:
    def __init__(self):
        self.username = ""
        self.password = ""

    def print_user_data(self):
        print(f"{self.username} {self.password}")

user_1 = User()
user_1.username = "Alex"
user_1.print_user_data()

user_2 = User()
user_2.username = "Viki"
user_2.print_user_data()



