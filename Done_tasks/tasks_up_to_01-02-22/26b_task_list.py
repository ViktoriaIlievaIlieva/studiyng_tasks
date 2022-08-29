# Write a program
# That reads the whole file "state.json"
# Converts the text taken from state.json to python types
#
# state.json will have a list of tasks to do
# a task has a due_date and description and will be a dictionary
#
# print the tasks to the user each on a new line in the format: <due date>: <description>
#
# Ask the user if he wants to add a new task
# if the anser is "yes":
#   - Ask for a new task date and also description
#   - Add the task to the list of tasks
#
# In the end no matter what the user chose for adding
# Convert the list of tasks back to json
# Open the file state.json and write the new list of tasks

import json

file = open("state.json", "r")
file_content_json_file = file.read()
file.close()


python_list = json.loads(file_content_json_file)


for index in python_list:
    print(index["due_date"] + ": " + index["description"])

new_task_question: str = input(" Do you want to add a new task? Yes or no? ")
if new_task_question == "yes":
    new_task_description: str = input(" Insert new task: ")
    new_task_due_date: str = input(" Insert new due date: ")

    new_dictionary: dict = {}
    new_dictionary["due_date"] = new_task_due_date
    new_dictionary["description"] = new_task_description
    python_list.append(new_dictionary)
else:
    print(" You are done")

json_list: str = json.dumps(python_list)

file = open("state.json ", "w")
file.write(json_list)
file.close()

# DONE
