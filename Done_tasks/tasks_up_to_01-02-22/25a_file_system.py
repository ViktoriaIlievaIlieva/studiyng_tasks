import os

# TASK 1 - Припомни си как се ползва терминала
# cd - change directory - след cd следва път до новата папка, ако подаваш път с ./ значи от текущата директория
# ls - извежда списък със всички файлове или папки в текущата директория
# python ./00a_hello.py - ще изпълни файла 00a_hello.py от текущата директория

# DONE

# TASK 2 - Find out what os.getcwd() does and print its result. Describe it. 
# (Working Directory is the directory from which we start the program)

# ANSWER - We can get the present working directory using the getcwd() method of the os module.
# This method returns the current working directory in the form of a string. We can also use the getcwdb() method
# to get it as bytes object.

current_dir: str = os.getcwd()
print(current_dir)

# DONE

# описание - предполагам, че ми изписва къде точно се изпълнява фойла, който принтирам

# TASK 3 - Find out what os.chdir() does. Describe it. Use it. Print os.getcwd() again.
# (Comment the code from this task when finished so that it doesn't break other tasks)

# ANSWER - Changing Directory
# We can change the current working directory by using the chdir() method.
# The new path that we want to change into must be supplied as a string to this method. We can use both the
# forward-slash / or the backward-slash \ to separate the path elements.
# It is safer to use an escape sequence when using the backward slash.

os.chdir("./challenges_2021")
current_dir = os.getcwd()
print(current_dir)

# DONE

# TASK 4 - Find out what os.listdir() does. Describe it.
# Call the os.getcwd() function again - this time don't print it, just save it to a variable.
# Call os.listdir() with the variable returned from os.getcwd() and save its result into a variable too
# Print the last variable

# ANSWER : All files and subdirectories inside a directory can be retrieved using the listdir() method.

# This method takes in a path and returns a list of subdirectories and files in that path. If no path is specified,
# it returns the list of subdirectories and files from the current working directory

# https://www.programiz.com/python-programming/directory

current_dir = os.getcwd()
directory_list: list[str] = os.listdir(current_dir)
print(directory_list)

# DONE

# TASK 5 - os.system("ls") can be used to execute commands in terminal
# use os system to execute the following command - "python ./00a_hello.py"

os.system("dir")
os.system("python ./00a_hello.py")

# DONE

# TASK 6 - Take the code from task 5 and modify it so that:
# you ask the user for a python file
# you execute the file that the user provided using python


user_file: str = input("Choose a file:")
os.system("python ./" + user_file)

# DONE

# TASK 7 - Take the code from task 6 and modify it so that:
# if the file doesn't exist - print "File not Found"
# else the file is executed

current_dir = os.getcwd()
directory_list = os.listdir(current_dir)

user_file: str = input("Choose a file:")

if not user_file in directory_list:
    print("File not Found")
else:
    os.system("python ./" + user_file)

# DONE
