# In task 27 you created a file person.py

# In that file add a function person_from_dictionary() OUTSIDE the class - done
# The function should take a dictionary variable in its brackets and creates a person
# The function should trust that the dictionary has the keys "first_name", "last_name", "password", "email"
# The function should return the Person it created

# import the person.py file here - done
# read the file people.json and convert it to python types from text - done
# it will contain a list of dictionaries - done

# pass each dictionary from the people.json file to the function person_from_dictionary from the person file
# create a new list from the return values of the person_from_dictionary function

# print the fullname of all the people

import person
import json

json_people_file = open ("people.json", "r")
json_people_file_content = json_people_file.read()
json_people_file.close()

py_dict_with_people = json.loads (json_people_file_content)

list_with_person_from_dictionary_function = []

for dictionary in py_dict_with_people:
    this_user = person.person_from_dictionary(dictionary)
    list_with_person_from_dictionary_function.append(this_user)

for index in list_with_person_from_dictionary_function:
        print (index.get_fullname())
