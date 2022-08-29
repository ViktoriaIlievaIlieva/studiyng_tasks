# 1. Create an empty list
# 2. Use append to add the values 1, 2 and 3 to it
# 3. Print the values of the list separately on a new line 

list_with_numbers: list[int] = []
list_with_numbers.append(1)
list_with_numbers.append(2)
list_with_numbers.append(3)

for value_in_list in list_with_numbers:
    print(value_in_list)

# DONE
