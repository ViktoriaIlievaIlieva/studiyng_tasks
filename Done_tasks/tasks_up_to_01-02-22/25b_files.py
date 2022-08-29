# sourcery skip: ensure-file-closed
# You've seen how to open files before
# The function is called open("filenime.txt", "r")
# Last time I showed you: with open("day1.txt", "r") as file:

# Today I will show you how to use it normally

file = open("test.py", "r")
file.close()  # IMPORTANT!

# Така... файл е променлива. Типа на променливата се нарича stream. (Както имаш типове int, float, string, list, dictionary...)

# Stream типа се използва за всякакви външни за програмата ти неща
# Така приложенията комуникират помежду си - например когато напишеш print() всъщност принт взима текста ти и го пише към Stream
# Друго приложение (терминалът) чете този Stream получавайки твоя текст
# Stream-а най-точно представлява канал за комуникация

# Файловете са stream защото ти отваряш канал за комуникация с хард диска ти, за да четеш или предаваш информация
# Много е важно да ги затваряш след като са отворени

file = open("22a_better_login.py", "r")
file_content: str = file.read()
file.close()
print(file_content)

file = open("22a_better_login.py", "r")
lines: list[str] = file.readlines()
file.close()
print(lines)

# "w" will delete everything in the file and open it for writing. 
# If the file doesn't exits it will create one
file = open("text.txt", "w")
file.write("I hate cold")
file.close()



# TASK 1
# Write a program that reads input from the user and saves it into a file called "last_input.txt"

user_input: str = input(" Write something: ")
file = open("last_input.txt", "w")
file.write(user_input)
file.close()

# DONE

# TASK 2 
# Write a program that asks the user for a file and then prints the contents of that file

user_file: str = input(" Choose a file: ")
file = open(user_file, "r")
file_content: str = file.read()
file.close()
print(file_content)

# DONE

# TASK 3
# Find a function that will help you read a line and not the whole file
# Open "00a_hello.py" and read only the first line and close it
# print it to the console

file = open("00a_hello.py", "r")
file_content: list[str] = file.readlines()
print(file_content[0])
file.close()

# DONE

# TASK 4
# Ask the user to point an existing file
# Ask the user to give you a new file name
# read the contents from the first file
# create a new file with the second filename and write the contents there

user_file: str = input(" Point an existing a file: ")
new_file_name: str = input(" Point new file name: ")
file = open(user_file, "r")
file_content: str = file.read()
file.close()
file_2 = open(new_file_name, "w")
file_2.write(file_content)
file.close()

# DONE
