# Functions

# 1. Create a function that takes one string variable and one integer variable in its brackets.
# The function creates a new resulting string variable
# that should be created from the string from the brackets repeated as many times as the integer in the brackets.
# The resulting string should then be returned

# Call the function and print the returned string by giving it a "*" and the number 5
# Call the function and print the returned string by giving it a "." and the number 3
# Call the function and print the returned string by giving it a "!?" and the number 4

# 2. Create a function that takes a string and an integer variables again
# This time the function should print a square using the value in the string
# by repeating the string from left to right and printing as many lines as the value of the number
# You MUST USE the function from task 1

# Call the function by giving it a "#" and the number 6


def viki_function (text, number):

    text_variable = text
    index = 0
    while index < number - 1:
        text_variable = text_variable + text
        index = index + 1
    return text_variable


call_1 = viki_function("*", 5)
print (call_1)

call_2 = viki_function(".", 3)
print (call_2)

call_3 = viki_function("!?", 4)
print (call_3)


def square (text, number):

    side_1 = viki_function(text, number)
    index = 0
    while index < number:
        print (side_1)
        index = index + 1


square("#", 6)
# DONE


# 3. Create a function that takes a list of float numbers in the brackets and returns the average of those numbers
# Ask the user to give you grades seperated with a space (using only one input).
# Split the grades and create a list with them.
# By using the function get the average grade and print the returned result.


def grades_average (list):
    number_of_grades = len (list)
    sum_of_grades = 0
    for index in list:
        sum_of_grades = sum_of_grades + float (index)
    average = sum_of_grades / number_of_grades
    return average

grades = input( "Insert your grades with space: ")
list_with_grades = grades.split()

print (grades_average(list_with_grades))


# DONE