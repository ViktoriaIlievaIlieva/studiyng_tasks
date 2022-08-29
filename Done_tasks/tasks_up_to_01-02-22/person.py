
# PART OF TASK 27B_PERSON

# - Add a class named Person
# - The class named Person should have attributes for first_name, last_name, email and take them from the constructor
# - Add a function get_fullname to class Person that RETURNs the: first_name + " " + last_name

class Person:

    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = ""


    def get_fullname (self):
        person_get_fullname = self.first_name + " " + self.last_name
        return person_get_fullname

    def evaluate_credentials (self, email, password):
        if self.email == email and self.password == password :
            return True
        else:
            return False

def person_from_dictionary (dictionary):

    first_name = dictionary["first_name"]
    last_name = dictionary["last_name"]
    email = dictionary["email"]

    user = Person(first_name, last_name, email)

    user.password = dictionary["password"]

    return user
