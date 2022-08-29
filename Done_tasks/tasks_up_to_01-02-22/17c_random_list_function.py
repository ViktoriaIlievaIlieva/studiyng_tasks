# Define a function that creates an empty list
# then adds 10 random numbers from 1 to 100 in the list
# returns the list

# Use the function 3 times to create 3 different random lists and print them out


import random


def create_random_list() -> list[int]:
    empty_list: list[int] = []
    index = 0
    while index < 10:
        random_number: int = random.randint(1, 100)
        empty_list.append(random_number)
        index = index + 1
    return empty_list


random_list1: list[int] = create_random_list()
print(random_list1)
random_list1: list[int] = create_random_list()
print(random_list1)
random_list1: list[int] = create_random_list()
print(random_list1)


# Done 
