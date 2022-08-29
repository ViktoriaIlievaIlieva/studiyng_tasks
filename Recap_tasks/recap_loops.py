#Task 1: Crate a program that repeatedly asks the user for commands. If the user writes "quit" then the program stops
# asking the user for commands and finishes.

index = True

while index:
    user_commands = input(" Enter a command. When you want to quit, write quit :")
    if user_commands != "quit":
        index = True
    else:
        index = False

# DONE

# Task 2: Add a command in the previous task such that when the user types hello the program prints the message "Hello, World!.

index = True

while index:
    user_commands = input(" Enter a command. When you want to quit, write quit :")
    if user_commands == "hello":
        print ("Hello, World!")
        index = True
    elif user_commands != "quit":
        index = True

    else:
        index = False

# DONE


# Task 3: Create a list with the values 1,5,2,6,11,13,12,42 remove from the list all values that when divided by 2
# have a remainder of 0 (aka even values). Print the list. Did you get any new errors? Which loop did you use?
# Did you manage to delete all values? Does it work with both loops? If you used while did you increment the position each
# time (even when you deleted an element)? What happens with the positions if you remove elements from the middle of the list?

list_with_values = [1,5,2,6,11,13,12,42]

index = 0
while index < len (list_with_values):
    if list_with_values [index] % 2 == 0:
        list_with_values.pop(index)
        index = index
    else:
        index = index + 1

print (list_with_values)

# DONE

# Task 4: Use the function random.randint after importing the random file using import random to generate a
# random number between 1 and 10. Store this as your initial value. Then call the function random.randint until
# you get the same value as the initial random value. Count how many times it took and print that count.

import random

value = random.randint(1,10)
count = 0
match = True
while match:
    value_2 = random.randint(1,10)
    if value_2 != value:
        count = count + 1
    else:
        match = False
        print (count)

# DONE