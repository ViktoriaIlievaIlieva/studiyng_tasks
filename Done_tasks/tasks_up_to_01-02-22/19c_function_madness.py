import random

# Optional video about functions programs - https://www.youtube.com/watch?v=l26oaHV7D40
# SoftUni Book - Functions - https://python-book.softuni.bg/chapter-10-functions.html

# Task 1
# 1. Write code that prints 10 times "I hate functions" without using any loop
# 2. Create a function that executes that code
# 3. Call the function 10 times in a row so that you get printed out 100 times "I hate functions"

print("Task 1")


def i_hate_functions():
    print("I hate functions")
    print("I hate functions")
    print("I hate functions")
    print("I hate functions")
    print("I hate functions")
    print("I hate functions")
    print("I hate functions")
    print("I hate functions")
    print("I hate functions")
    print("I hate functions")


i_hate_functions()
i_hate_functions()
i_hate_functions()
i_hate_functions()
i_hate_functions()
i_hate_functions()
i_hate_functions()
i_hate_functions()
i_hate_functions()
i_hate_functions()

# DONE

# Task 2
# 1. Write code that asks you for a name and prints out: "Hello, " + name
# 2. Make a function and move ONLY the print statement in it
# 3. The print statement would still need the 'name' variable
# 4. Call the function by passing it the 'name' variable coming from the input
# 5. Call the function once more with a different name

print(" Task 2 ")


def hello(greeting):
    hi: str = "Hello,"
    print(hi + greeting)


greeting: str = input("What is your name?  ")

hello(greeting)

# DONE

# Task 3
# 1. Write a code that takes 2 numbers from input and then does the operations ADD, SUBTRACT, MULTIPLY and DIVIDE
# beteween those 2 numbers and prints the result of each operation
# 2. Make a function and move everything EXCEPT the lines where you take the numbers from input
# 3. The function would still need to take two numbers
# 4. Call the function 2 times - once passing it the numbers normally and second passing it the second number first
# and the first number second

print(" Task 3 ")

first_number: str = input(" Insert first number: ")
second_number: str = input(" Insert second number: ")

a: int = int(first_number)
b: int = int(second_number)


def calculator(a: int, b: int):
    action: str = input(" Insert desired action: add, substract, divide or multiply:  ")
    if action == "add":
        result: int = a + b
    elif action == "substract":
        result: int = a - b
    elif action == "divide":
        result: float = a / b
    elif action == "multiply":
        result: int = a * b

    print(result)


calculator(a, b)
calculator(b, a)

# DONE

# Task 4
# 1. Create a function
# 2. The function will take one variable in its brackets - call it number
# 3. The function code should print as many dots on one line as the value of the number
# 4. Write a loop that prints a triangle (similar to 08a_draw_triangle) by looping through the numbers from 1 to 10
# and passing that number to the function for drawing dots

print(" Task 4 ")


def print_dots(number: int):
    dot: str = ""
    index: int = 0
    while index < number:
        dot = dot + "."
        index = index + 1
        print(dot)


index: int = 1
while index < 10:
    print_dots(index)
    index = index + 1

# DONE


# Task 5
# 1. Make this code in a function EXCEPT the print statement
# 2. The print statement will still need to print the result
# 3. Make the function RETURN the result and then call the function so that it prints the result

print(" Task 5 ")


def math() -> int:
    a: int = random.randint(1, 100)
    b: int = random.randint(1, 100)
    c: int = random.randint(1, 100)
    result: int = a + (b * b) - c
    return result


solution = math()
print(solution)


# Task 6
# 1. Write a function that RETURNs a random value between 1 and 100

print(" Task 6 ")


def random_number() -> int:
    a: int = random.randint(1, 100)
    return a


end_number: int = random_number()
print(end_number)


# Task 7
# 1. Write a function called ask_name that takes input from the user for his name and RETURNs it

print(" Task 7 ")


def ask_name() -> str:
    name: str = input(" What is your name?: ")
    return name


name_1: str = ask_name()
print(name_1)

# Task 8
# 1. Create a function that prints a header message "--- BEGIN ---"
# 2. Create a function that takes a list of strings and prints each of them on a new line
# 3. Create a function that prints a footer message "---  END  ---"
# 
# 4. Create another function that takes a list of strings and then:
# - prints a header by calling the header function
# - prints the body by calling the second function by passing it the list of strings
# - prints a footer by calling the footer function
#
# Call only the last function by passing it the list 'products'

print("Task 8")

products: list[str] = [
    "Apples - 2 x 1.00",
    "Rice - 1 x 2.00",
    "Bread - 1 x 1.70",
    "Water - 1 x 4.00",
]


def begging():
    print("--- BEGIN---")


def list_1(products: list[str]):
    for product in products:
        print(product)


def end():
    print("---END---")


def final(products: list[str]):
    begging()
    list_1(products)
    end()


final(products)

# Done
