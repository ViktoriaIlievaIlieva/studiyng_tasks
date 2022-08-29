
# list_of_numbers = [1, 2, 3, 2, 6, 2, 4, 7, 10, 3, 18, 42, 33, 21, 22, 2]

# Task 1
# Print the VALUES in the list

print("Task 1:")


list_of_numbers: list[int] = [1, 2, 3, 2, 6, 2, 4, 7, 10, 3, 18, 42, 33, 21, 22, 2]
for value in list_of_numbers:
    print(value)


# Task 2
# Print the VALUES starting from the second POSITION and ending just before the last POSITION (do not include
# the first or last POSITIONS)

print("Task 2:")


list_of_numbers: list[int] = [1, 2, 3, 2, 6, 2, 4, 7, 10, 3, 18, 42, 33, 21, 22, 2]
index = 1 
while index < len(list_of_numbers) - 1:
    print(list_of_numbers[index])
    index = index + 1


# Task 3
# Count how many times the VALUE of 2 is repeated in the list

print("Task 3:")


list_of_numbers: list[int] = [1, 2, 3, 2, 6, 2, 4, 7, 10, 3, 18, 42, 33, 21, 22, 2]
count_of_2: int = 0
index: int = 0
while index < len(list_of_numbers):
    if list_of_numbers[index] == 2:
        count_of_2 = count_of_2 + 1
        index = index + 1

print(count_of_2)
 

# Task 4
# Split the even and odd VALUES from the list in two separate lists

print("Task 4")


list_of_odd_values: list[int] = []
list_of_even_values: list[int] = []

list_of_numbers: list[int] = [1, 2, 3, 2, 6, 2, 4, 7, 10, 3, 18, 42, 33, 21, 22, 2]

index: int = 0
while index < len(list_of_numbers):
    if list_of_numbers[index] % 2 == 0:
        list_of_even_values.append(list_of_numbers[index])
    else:
        list_of_odd_values.append(list_of_numbers[index])
    index = index + 1

print("List of odd numbers:", list_of_odd_values)
print("List of even numbers:", list_of_even_values)


# Task 5
# Split the even and odd POSITIONS from the list in two separate lists

print("Task 5")


list_of_odd_values: list[int] = []
list_of_even_values: list[int] = []

list_of_numbers: list[int] = [1, 2, 3, 2, 6, 2, 4, 7, 10, 3, 18, 42, 33, 21, 22, 2]

index: int = 0
while index < len(list_of_numbers):
    if index % 2 == 0:
        list_of_even_values.append(list_of_numbers[index])
    else:
        list_of_odd_values.append(list_of_numbers[index])
    index = index + 1

print("List with numbers on the odd positions", list_of_odd_values)
print("List with numbers on the even positions", list_of_even_values)


# Task 6
# Print 100 times the string "I hate loops"

print("Task 6")


numbers: range = range(1, 101)
index = 0
while index < len(numbers):
    print("I hate loops")
    index = index + 1


# Task 7
# Multiply all the values of the list together

print("Task 7")


list_of_numbers: list[int] = [1, 2, 3, 2, 6, 2, 4, 7, 10, 3, 18, 42, 33, 21, 22, 2]

result: int = 1

index: int = 0
while index < len(list_of_numbers): 
    result = result * list_of_numbers[index]
    index = index + 1
print("The result is:", result)


# Task 8
# HARD: Count how many times each VALUE from 0 to 4 is repeated in the list 'task_8_list' by incrementing the VALUE
# in 'counters_list' on the correspondin POSITION
# EXAMPLE: 
# The first element in task_8_list is '1'
# We then increment the 'count ers_list' value on position 1 which will result in [0, 1, 0, 0, 0] for the counters list

print("Task 8")


task_8_list: list[int] = [1, 2, 2, 1, 3, 0, 1, 3, 2, 3, 1, 2, 0, 4, 2, 1, 3, 0]
counters_list = [0, 0, 0, 0, 0]

index = 0
while index < len(task_8_list):
    if task_8_list[index] == 0:
        counters_list[0] = counters_list[0] + 1
    elif task_8_list[index] == 1:
        counters_list[1] = counters_list[1] + 1
    elif task_8_list[index] == 2:
        counters_list[2] = counters_list[2] + 1
    elif task_8_list[index] == 3:
        counters_list[3] = counters_list[3] + 1
    elif task_8_list[index] == 4:
        counters_list[4] = counters_list[4] + 1
    index = index + 1

print(counters_list)


# Task 9
# Go through each element of the list_of_numbers. 
# If the CURRENT element IS HIGHER than the one BEFORE it then ADD it to the result
# If the CURRENT element IS LOWER than the one BEFORE it then SUBSTRACT if from the result
# The first element is ADDED to the sum as there is no element to compare it with

print("Task 9 ")


list_of_numbers: list[int] = [1, 2, 3, 2, 6, 2, 4, 7, 10, 3, 18, 42, 33, 21, 22, 2]

index: int = 1
result: int = list_of_numbers[0]
while index < len(list_of_numbers):
    if list_of_numbers[index] > list_of_numbers[index-1]:
        result = result + list_of_numbers[index]
    elif list_of_numbers[index] < list_of_numbers[index-1]:
        result = result - list_of_numbers[index]
    index = index + 1

print(result)


# Task 1 to task 9 = DONE
