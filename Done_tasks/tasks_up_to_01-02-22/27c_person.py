# Use person.py from the previous task:
# - add attribute for password but don't take it through the __init__ function just make it equal to an empty string
# - Add a function evaluate_credentials(self, email, password) to Person that takes email and password, compares them
#    with the Person's attributes of the same name and RETURNs True if they match and False if they don't

# IN THIS FILE
# import the person file
# - create a new variable called 'user' of the person.Person custom type (aka Person class)
#     with first name "Viktoria" and last name "Ilieva" and email "admin@abv.bg"
# - set a password "pass"

# - ask for an email
# - ask for password
# - use the function evaluate_credentials on the user variable by passing it the email and password that were provided from input
#   and save the result in a variable
# - if the credentials were correct then print "logged in"

import person

user = person.Person ("Viktoria", "Ilieva", "admin@abv.bg")

user.password = "pass"

email = input (" Insert email: ")
password = input ("Insert password: ")

credentials = user.evaluate_credentials(email, password)
print (credentials)
