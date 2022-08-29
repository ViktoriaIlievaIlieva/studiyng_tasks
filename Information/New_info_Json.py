# File format - if every file is a text file we can set rules in the way we structure these files
# so that they are easy to read either by a human or by a program

# JSON - JavaScript Object Notation
# File format used for storing or transfering common program data
# It is easy to read both by programs and humans (programmers)
#
# In our programs we studied the following types:
# int - a whole number => 1
# float - a number with a decimal point (or a fraction) => 1.1
# str - string which is a list of characters => "Hello, World"
# list - multiple elements (usually of the same type) => [1, 2, 3, 4, 5]
# bool - truthness => True, False
# dictionary - multiple elements that could be of different types and are named through the use of a key => { "a": 1, "b": "text", "c": 1.1 }

# In JSON format these could be saved to a file using the exact same notation:
# numbers go as numbers
# strings are in quotes
# lists start and end with [] and elements are separated with commas
# dictionaries start and end with {} - their elements start with a key in a string, then colon, then the value
# booleans are true or false

# The way we work with JSON files in python is by converting the text (string) when the file is read to python types (ints, lists, floats, dictionaries and strings)

# This string describes a dictionary in JSON but is not yet a dictionary in python
json_in_string = "{ \"a\": 1 }"

# To easily make a dictionary out of the string above we can use the library "json"
import json

# The function is called loads (load string)
python_dictionary = json.loads(json_in_string)
print(python_dictionary["a"])

# It can go both ways - we can have python types and save them to a JSON
list_of_users = []

user1 = { "username": "viki", "password": "pass" }

user2 = { "username": "ico", "password": "example" }

list_of_users.append(user1)
list_of_users.append(user2)

# json.dumps() - given a variable will create the JSON representation
json_list_of_users = json.dumps(list_of_users)
print(json_list_of_users)
