# Create an empty list
# Repeat 100 times: generate a random number between 1 and 100 and insert into the list

# Вариант 1
import random

empty_list: list[int] = []

index = 0
while index < 100:
    random_number: int = random.randint(1, 100)
    empty_list.append(random_number)
    index = index + 1
print(empty_list)


# Вариант 2

randomlist: list[int] = []
for index in range(0, 100):
    n: int = random.randint(1, 100)
    randomlist.append(n)
    print(randomlist)

len_of_list: int = len(randomlist)
print(len_of_list)

# DONE
