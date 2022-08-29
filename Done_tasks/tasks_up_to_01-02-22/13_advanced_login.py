# Write a login system that:
# 1. asks for username and password
# 2. checks that username equals "viki" and password equals "example"
# 3. If username is not correct - print "incorrect user" and return to step 1
# 4. If password is not correct - print "incorrect password" and return to step 1
# 5. If both username and password are correct - print "logged in" and exit the program
# (don't ask for username and password anymore)

correct_username: str = "viki"
correct_password: str = "example"

username: str = "neshto"
password: str = "neshto_2"

while correct_username != username or correct_password != password: 
    username: str = input("Insert username: ")
    password: str = input("Insert password: ")
    if correct_password != password and correct_username != username:
        print("Incorrect password and username")
    elif correct_username != username:
        print("Incorrect user name!")
    elif correct_password != password:
        print("Incorrect password!")
  
print(" Logged In! ")

# DONE
