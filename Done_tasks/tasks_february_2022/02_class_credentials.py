# Note: All class attributes will be taken from the constructor

# Create a class Credentials with attributes (types are just for your information):
# username : string
# password : string

# Create a function called evaluate in the class Credentials
# it takes two variables for username and password and checks them against the ones in the class
# returning True if they match and False if they don't

# Create a class User with attributes:
# full_name : string
# email : string
# credentials : Credentials

# Create a function called evaluate in the class User
# it takes two variables for username and password and calls the evaluate function on the credentials attribute
# returns the result that was received from the credential's evaluate function

# Create three variables of type User
# Run until the user enters correct credentials:
#     Ask for username and password
#     Evaluate what the user entered with the existing users
#     if correct print "logged in"

class Credentials:
    def __init__(self, true_username, true_password):
        self.username = true_username  # viki
        self.password = true_password  # example

    def evaluate (self, inserted_username, inserted_password):
        if inserted_username == self.username and inserted_password == self.password:
            return True
        else:
            return False


class User:

    def __init__(self, true_full_name, true_email, true_credentials):
        self.full_name = true_full_name
        self.email = true_email
        self.credentials = true_credentials

    def check_credentials (self, inserted_username, inserted_password):
        result = self.credentials.evaluate(inserted_username, inserted_password)
        return result


user_1 = User ("viktoria", "viki@mail.bg", Credentials("viki", "example"))
user_2 = User ("hristo", "ico@mail.bg", Credentials("ico", "example"))

users: list[User] = []
users.append(user_1)
users.append(user_2)

not_logged_in: bool = True

while not_logged_in:
    inserted_username = input("Insert username: ")  # lolo
    inserted_password = input("Insert password: ")  # tata

    for user in users:
        matching = user.check_credentials(inserted_username, inserted_password)
        if matching:
            not_logged_in = False


print("logged in")

