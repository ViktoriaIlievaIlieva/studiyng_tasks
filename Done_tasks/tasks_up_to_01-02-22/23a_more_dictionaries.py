
# (NEW FOR LISTS)
# --------------------------------------------------------------------

list_of_numbers = [1, 2, 3, 4, 5]

number = int(input("Enter number:"))

# check if number is in list
#         ->
if number in list_of_numbers:
    print("number is in list")

# is a boolean similar to how == works
is_in_list_variable = number in list_of_numbers 
print(is_in_list_variable)

# DO NOT CONFUSE WITH HOW FOR-LOOP WORKS
# (PYTHON CAN BE CONFUSING)

#   take each element from 
#   list and put in number
#          <-
for number in list_of_numbers:
    print(number)

# --------------------------------------------------------------------

user = {"username": "viki", "password": "pass"}

# TASK 1
# Find out what user.values() function will do and describe it
# Find out what user.keys() function will do and describe it

#answer user.values() function

#The values() method returns a view object. The view object contains the values of the dictionary, as a list.
#The view object will reflect any changes done to the dictionary, see example below.
# syntax: dictionary.values()

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.values()

car["year"] = 2018

print(x)

#answer user.key() function

#The keys() method returns a view object. The view object contains the keys of the dictionary, as a list.
#The view object will reflect any changes done to the dictionary, see example below.

#Syntax: dictionary.keys()

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.keys()

car["color"] = "white"

print(x)

#С value ще ни изпише списък със стойностите запазени в речника 
#С key ще ни изпише списък с Key (ключовете) в речника 


# TASK 2
# ask for input from the user
# print "key exists" if the value the user entered is in the list of keys
# print "value exists" if the value the user entered is in the list of values

user = {"username": "viki", "password": "pass"}

user_value = input (" Insert your value: ")

x = user.keys()
y = user.values()

if user_value in y:
    print ("Value exists")

elif user_value in x:
    print ("Key exists")

else:
    print ("The value doesn`t exist")


# Done
