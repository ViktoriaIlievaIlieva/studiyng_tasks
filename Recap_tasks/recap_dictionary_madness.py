# Create a program that asks the user for a command. When a command finishes he is asked for a new one.
# The program should quit when the user types "quit" as a command
# Using the dictionaries:
# Create an array (list) which will store tasks, where a task has: title, description and due date
# Implement a command "add" for adding a new task to the list (ask the user for data)
# Implement a command "list" which shows all the tasks
# Implement a command "remove" which removes a task from the list (ask the user which task)
# Implement a command "show by date" which asks for a date and then shows only the tasks for that date.
# quit

keep_loop = True
list_with_tasks = []

while keep_loop:
    user_command = input("Choose command: \n a. Add \n b. List \n c. Remove \n d. Show due date \n e. Quit \n")
    if user_command == "add":

        new_title = input(" Insert title of the new task : ")
        new_description = input ("Insert description of the new task: ")
        new_due_date = input ("Insert due date of the new task?:  ")

        dictionary_with_tasks = {}
        dictionary_with_tasks ["title"] =  new_title
        dictionary_with_tasks["description"] = new_description
        dictionary_with_tasks["due_date"] = new_due_date


        list_with_tasks.append(dictionary_with_tasks)

    elif user_command == "list":
        print (list_with_tasks)

    elif user_command == "remove":
        task_for_removal = int (input ("Insert the number of the task you want to remove? : "))
        index = 0
        while index < len(list_with_tasks):
            if index == task_for_removal:
                list_with_tasks.pop(index)
            index = index + 1

    elif user_command == "show due date":
        data_of_desired_task = int (input("The date of which task do you want? : "))
        for value_is_dict in list_with_tasks:
            if value_is_dict ["due_date"] == data_of_desired_task:
                print (value_is_dict)

    elif user_command == "quit":
        keep_loop = False

# да  се върна на реда 42 - 47 и да видя дебъга



