# Define a function that creates an empty list
# the function takes a number and appends to the list as many random values from 1 to 100 as the value of
# the taken number
# and returns the list

# Use the function 3 times to create 3 different random lists (one with 5, 10 and 15 values) and print them out 

import random


def random_list(number: int) -> list[int]:
    empty_list: list[int] = []

    index: int = 0
    while index < number:
        random_number: int = random.randint(1, 100)
        empty_list.append(random_number)
        index = index + 1
    return empty_list


random_list_1: list[int] = random_list(5)
print(random_list_1)

random_list_1: list[int] = random_list(10)
print(random_list_1)

random_list_1: list[int] = random_list(15)
print(random_list_1)

# DONE
