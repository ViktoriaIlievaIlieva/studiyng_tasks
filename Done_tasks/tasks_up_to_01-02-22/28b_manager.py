
# Create a file named users_manager.py

# TASK 1
# IN users_manager.py: define the class User which has an __init__ constructor that doesn't take anything in the brackets except self
# but initializes three attributes for the class
#    - self.username that equals an empty string
#    - self.password that equals an empty string
#    - self.active that equals a boolean value of False

# TASK 2
# IN users_manager.py: create a class called UserManager which has an __init__ constructor that doesn't take anything in the brackets except self
# but initializes one attribute for the class:
#    - self.users that is an empty list


# TASK 3
# Define two functions INSIDE the UserManager class
#    - load(self)
#        - the function will open up "users.json" file for read and read the text
#        - the function will convert the text to python types (list of dictionaries)
#        - go through each dictionary and:
#           - create a User class from each dictionary by matching the User class
#           attributes with dictionary keys of the same name
#           - the function will append every newly created User class to its self.users
#           list


# TASK 4
#    - save(self)
#        - the function will create a temporary list
#        - the function will go through each element of the self.users list
#           - the function will create a dictionary and add values for an element
#           from the self.users list
#               by matching the attribute name to a key of the same name
#           - the function will add the dictionary to the new temporary list
#        - the function will convert the temporary list to a json string
# #        - the function will open up "users.json" file for write and write the json


# TASK 5
# IN THIS FILE import the users_manager file
# 1. create a new variable of UserManager type and call its .load() function
# 2. go through each element of the list of users of your UserManager variable and print only
# the username of the ones that are active
# 3. go through the first 3 elements and flip their active boolean value to the opposite one
# 4. call its .save() function


import users_manager

manager = users_manager.UserManager()

# Loading from file to manager.users
manager.load()

for some_user in manager.users:
    if some_user.active == True:
        print (some_user.username)

# Flipping the first 3 active values
index = 0
while index < 3:
    some_user = manager.users[index]
    flipped = not some_user.active
    some_user.active = flipped

    index = index + 1

# Saving  to file
manager.save()