# Create a program that asks the user for a command. When a command finishes he is asked for a new one.
# The program should quit when the user types "quit" when he's asked for a command
# Create a command called "read" - the user gets asked for a file and the program reads and prints that file content.
# Implement a command called "copy" - the user gets asked for a file and a new file and copies the first file content to the second.
# Implement a command called "create" - the user gets asked for text and then for a file. Creates the file by saving the user text in it.
# Implement a command called "help" - prints what other commands are available and a short description of what they do


command = True

while command:
    user_command = input(" Choose a command: \n a. read \n b. copy \n c. create \n d. help \n e. quit \n answer : ")
    if user_command == "read":
        user_path = input("Insert name of the file you want to read ? : ")
        file = open (user_path, "r")
        file_content = file.read()
        file.close()
        print (file_content)

    elif user_command == "copy":
        user_path = input("Insert name of the file you want to read ? : ")
        file = open(user_path, "r")
        file_content = file.read()
        file.close()

        file_2 = open ("recap_copied_file_kum_zad_recap_file_madness.py", "w")
        file_2.write(file_content)
        file_2.close()

    elif user_command == "create":
        users_new_file_name = input("Choose a file name: ")
        users_text = input (" Insert your file text: ")
        file_3 = open (users_new_file_name, "w")
        file_3.write(users_text)
        file_3.close()

    elif user_command == "help":
        print ( "The command called \"read\" allows you to choose a file and see its content. \n The command \"copy\" allows you to copy one file into another. \n The command \"create\" allows you to  create a new file - including its name and content. \n the command \"quit\" allows you to stop the program.")

    elif user_command == "quit":
        command = False



