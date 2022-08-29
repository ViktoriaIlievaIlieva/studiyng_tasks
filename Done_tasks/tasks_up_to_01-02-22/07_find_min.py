# Find and print the real lowest value in the following list:

list_of_values: list[int] = [1, 2, 3, 5, 15125, 125, 125, 0 , -3, 123 , 23123, -214, -231, -233, -221, 124, 332, 5125,
                             -5215, 5125, -5, 0, 123212, 12321421, -41242214, 125, -1255125, -5125125, -35325, -3525235]

min_value_so_far: int = list_of_values[0]

for value in list_of_values:
    if value < min_value_so_far:
        min_value_so_far = value
print(min_value_so_far)

# DONE
