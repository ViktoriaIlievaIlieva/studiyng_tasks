# Write code inside the function try_login() so that the function:
# 1. Takes input form the user for username and password
# 2. Prints the "logged in" if the username and password match correct_username and correct_password
# 3. Returns True if the username and password are correct and False if they are not

def try_login() -> bool:
    correct_username: str = "viki"
    correct_password: str = "example"

    username: str = input(" Insert your username: \n ")
    password: str = input("Insert your password: \n ")

    if username == correct_username and password == correct_password:
        print("logged in")
        return True
    else:
        return False


is_logged_in: bool = False
while not is_logged_in:
    is_logged_in = try_login()


# тук посл 3 реда ли трябва да пипна не разбирам  какво се иска. какво значи “# 3. Returns True if the username
# and password are correct and False if they are not"

# DONE
