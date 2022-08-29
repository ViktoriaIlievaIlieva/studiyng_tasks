# Define a function that is given a list and prints its values each on a new line
# Use the random list function from 17c to generate 3 lists and then use the new list printing function to print the
# lists

import random


def random_list(number: int) -> list[int]:
    empty_list: list[int] = []
    index = 0
    while index < number:
        random_number: int = random.randint(1, 100)
        empty_list.append(random_number)
        index = index + 1
    return empty_list


def list_new_lines(list_with_values: list[int]):
    for index in list_with_values:
        print(index)


my_random_list: list[int] = random_list(5)
list_new_lines(my_random_list)

my_random_list: list[int] = random_list(10)
list_new_lines(my_random_list)

my_random_list: list[int] = random_list(15)
list_new_lines(my_random_list)

# Done - да го видя пак като логика на 13.01.22

