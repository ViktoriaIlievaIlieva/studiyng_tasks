# Write code to print the largest number in this list
# and don't write print(132)

list_of_numbers: list[int] = [2, 3, 4, 5, 2, 9, 22, 132, 5, 5, 2, 9, 22, 132, 5, 2, 11, 2, 3, 4, 5, 7, 9, 22, 142, 6,
                              5, 2, 9, 22, 112, 5, 2, 11, 2, 3, 4, 5, 2, 9, 22, 132, 5, 5, 2, 9, 22, 132, 5, 2, 11, 2,
                              3, 422, 5, 74, 9, 22, 172, 6, 5, 2, 9, 22, 112, 5, 2, 11]

max_value_so_far: int = list_of_numbers[0]

for value_in_list in list_of_numbers:
    if max_value_so_far < value_in_list:
        max_value_so_far = value_in_list
    
print(max_value_so_far)

# DONE
