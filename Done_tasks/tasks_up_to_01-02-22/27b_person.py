# Create a python file called person.py and in that file:
# - Add a class named Person
# - The class named Person should have attributes for first_name, last_name, email and take them from the constructor
# - Add a function get_fullname to class Person that RETURNs the: first_name + " " + last_name


# IN THIS FILE
# import the person file
# create a new variable called person_test of the person.Person custom type (aka Person class) with first name "Hristo" and last name "Iliev" and an empty email
# take input from the user for the email field
# modify the person_test's email field
# print the full name of the person_test variable by getting it through the get_fullname() function

import person
person_test = person.Person( "Hristo","Iliev", "" )

person_test.email = input (" Insert email: ")

person_information = person_test.get_fullname()

print (person_information)
print (person_test.email)
# DONE
