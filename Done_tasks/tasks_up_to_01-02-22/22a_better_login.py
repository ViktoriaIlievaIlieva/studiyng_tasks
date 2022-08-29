# This is a bigger task: Follow the comments
# Finish the code in this function so that it creates a dictionary variable called user with two keys:
# "username" that will hold the value of username
# "password" taht will hold the value of password
# Write code that will ask you for username and password if they match with any user dictionary in the list_of_users list
# then you print "logged in"
# else you ask them to try again


def create_user(username: str, password: str) -> dict:
    user: dict = {"username": username, "password": password}
    return user


admin_user1 = create_user("admin", "admin")
admin_user2 = create_user("viki", "example")
admin_user3 = create_user("ico", "ico123")

list_of_users: list[dict] = []
list_of_users.append(admin_user1)
list_of_users.append(admin_user2)
list_of_users.append(admin_user3)


username: str = input("What is your name?: ")
password: str = input(" What s your password?: ")

is_logged_in: bool = False

for user in list_of_users:
    if username == user["username"] and password == user["password"]:
        is_logged_in = True
    print("You are logged in! ")
    
if not is_logged_in:
    print("Try again")

# not е оператор обръща bool преди да започне if-а, въпреки че е в него

# DONE
