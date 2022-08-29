# This is a bigger task: Follow the comments
# 1. print "CTRL + C to exit"
# 2. In an endless loop:
#     - Write code that will ask you for username and password:
#         a/ if they match with any user dictionary in the list_of_users list then you print "logged in"
#         b/ else you print try again

# 3. Modify the code:
# After login the user gets a menu with two options 1/ add user, 2/ logout
# a/ if he chooses add user a he is asked for username and password the user is added to the list
# b/ if he chooses logout the system will get back to the login (if a new user has been added it should now be available
# for login)


def create_user(username: str, password: str) -> dict:
    user: dict = {"username": username, "password": password}
    return user


admin_user: dict = create_user("admin", "admin")

list_of_users: list[dict] = []
list_of_users.append(admin_user)

print("CTRL + C to exit")

while True:
    username: str = input("What is your name?: ")
    password: str = input(" What s your password?: ")
  
    is_logged_in: bool = False

    for user in list_of_users:
        if username == user["username"] and password == user["password"]:
            is_logged_in = True
            print("You are logged in! ")

        option: str = input("Choose an option: \n 1. Add user \n 2. Logout \n")
        if option == "add user":
            new_user_username: str = input(" Insert new user username? ")
            new_user_password: str = input(" Insert new user password? ")
      
            new_user: dict = create_user(new_user_username, new_user_password)
            list_of_users.append(new_user)

        elif option == "logout":
            is_logged_in = False

    if not is_logged_in:
        print("Try again")

   
# DONE
