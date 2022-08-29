# Write a program that will ask you for username and password
# and print:
# 1. "logged in" if username equals correct_username and password equals correct_password
# 2. "try again" if they don't

correct_username: str = "viki"
correct_password: str = "example"

username: str = input("Insert username: ")
password: str = input("Insert password: ")

if username != correct_username or password != correct_password: 
    print("Try again")
else: 
    print("Logged in!")

# DONE
