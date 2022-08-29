# Write code inside the function try_login() so that the function:
# 1. Takes input form the user for username and password
# 2. Prints the "logged in" if the username and password match correct_username and correct_password

def try_login():
    correct_username: str = "viki"
    correct_password: str = "example"

    username: str = input(" Insert your username: \n ")
    password: str = input("Insert your password: \n ")

    if username == correct_username and password == correct_password:
        print("logged in")


try_login()

# DONE
