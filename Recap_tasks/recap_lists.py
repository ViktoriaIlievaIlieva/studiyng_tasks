# Task 1: Create an empty list. Ask the user 3 times for input and add each input in the list. Print the whole list variable.

empty_list = []

index = 0
while index < 3:
    user_number = int (input ("Choose number: "))
    empty_list.append(user_number)
    index = index + 1

print (empty_list)

# DONE

# Task 2: Create a list with the following values 1, 5, 6, 13, 42. We'll make a weird reverse toto and this list
# is our lucky numbers in 5/49. Ask the user for five numbers and check wether each number the user entered is in
# the list of lucky numbers. Count the numbers that the user got right and print how many he got.

list_1 = [1, 5, 6, 13, 42]

count = 0
users_numbers = []

index = 0
while index < 5:
    user_input = int( input ("Enter number: "))
    if user_input in list_1:
        if not user_input in users_numbers:
            count = count + 1
            users_numbers.append(user_input)
    index = index + 1

print ("You have guessed: ", count)

# DONE

# Task 3: Create a list with the following values 1, 5, 6, 13, 42, 5, 2, 5, 11, 5. Remove all numbers 5 from the list
# and print it again.

list_with_numbers = [1, 5, 6, 13, 42, 5, 2, 5, 11, 5]

for index in list_with_numbers:
    if index == 5:
        list_with_numbers.remove(index)

print (list_with_numbers)

#  DONE