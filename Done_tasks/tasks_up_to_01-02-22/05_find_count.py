# Find out how many times the number 2 repeats inside this list

list_of_number: list[int] = [2, 3, 4, 5, 2, 9, 22, 132, 5, 5, 2, 9, 22, 132, 5, 2, 11, 2, 3, 4, 5, 7, 9, 22, 142, 6, 5,
                             2, 9, 22, 112, 5, 2, 11, 2, 3, 4, 5, 2, 9, 22, 132, 5, 5, 2, 9, 22, 132, 5, 2, 11, 2, 3,
                             422, 5, 74, 9, 22, 172, 6, 5, 2, 9, 22, 112, 5, 2, 11]

count: int = 0
for value_in_list in list_of_number:
    if value_in_list == 2:
        count = count + 1
print(count)

# DONE
