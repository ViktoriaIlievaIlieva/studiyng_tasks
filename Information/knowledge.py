# Comments start with a hashtag. 
# Comments are not run or considered a valid program.

# x is called a variable
# x is assigned to the number 5
x = 5

# Value can be changed
x = 3

# Values can be used for calculation of other values
y = x + 3

# Value can be changes as a result of a calculation with itself too
x = x + 2

# This is common so there is a shortcut
x += 2

# At this point we did a few operations to x
# x = 5
# x = 3
# |x = x + 2| -> |x = 3 + 2| -> |x = 5|
# |x += 2| -> |x = x + 2| -> |x = 5 + 2| -> |x = 7|


# print is a function. Functions are recognized by the normal brackets: ()
# It will show anything that is written within the brackets inside the terminal
# In this case that will take the variable x and see what value it has. It was assigned 7 so the computer will show 7 in the terminal.
print(x)

# There are a few types of values
# booleans: can be True or False
x = True
x = False

# boolean operations include
y = False
z = True

# both y and z have to be True for x to be assigned True
x = y and z

# either y or z has to be True for x to be assigned True
x = y or z

# equality or inequality - y and z can also be numbers or strings here. x will be assigned with a boolean value of True or False
x = y == z
x = y != z

# numbers: split into integers (whole/round numbers) and floats (real/decimal numbers)
x = 1 # integer
x = 1.1 # float

# number operations include
x = 1 + 2
x = 2 - 3
x = 5 / 2
x = 5 * 2
x = 5 % 2 # will assign the remainder of the operation which in this case is 1

# strings: text. Because the code you are writing is also text - strings are written inside quotes: "this is a string"
x = "this is a string"

# operations include
x = x + " and it can be extended"

# You can convert between the types
x = int("5")
x = float("5.5")
x = str(5)
x = bool(1)

# lists: multiple elements. Can be created with square brackets: []
x = []
# Values can also be given inside the square brackets with comas between
x = [1, 3, 2]

# Values can be different types
x = [1, "2"]

# Elements in lists are accessed through the variable name and square brackets put together. In the square brackets the number of the element is provided starting from 0
print(x[0]) # Prints 1 to the terminal

# There are functions related to lists like:

# Get the amount of elements
len(x)

# Add new element
x.append(3)

# Remove an element
del x[2]

# Conditional statements only execute code if some condition has the value of True
# The code that is executed only if the condition is true is written one tab to the right and is called a block
# There can be multiple lines in the block
x = True
if x:
    print("x is True")

# if statements can have an else or an elif addition
# else is used when you want to write code for the opposite case
# elif if you want to add a condition that will ONLY be checked if the previous conditions were False
y = False
if y:
    print("y is True")
elif x:
    print("y is False and x is True")
else:
    print("y is False and x is False")


# Loops are useful for repeating actions

# while statement is a loop that will repeat while a condition is True. This is similar to if
x = 0
while x < 5:
    x = x + 1
    print(x)

# can be useful for going through a list
l = [5, 6, 1, 3]
i = 0
while i < len(l):
    item_in_list = l[i]
    print(item_in_list)

    i = i + 1

# for statement is a loop that will take a list of elements and go through each one assigning it to a variable
# it is useful to shorten the while loop that is written above

for item_in_list in l:
    print(item_in_list)

# To ask for values when the program is run use the function input. In the brackets of input you can have a string that will be presented when asked for the value
x = input("Give me a value: ")