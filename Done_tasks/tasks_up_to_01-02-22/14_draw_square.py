# Print a square of dots with the size given by the user

# Example of 5x5 square:
# .....
# .....
# .....
# .....
# .....


dot: str = " "
number: int = 0
inserted_number: str = input(" Insert wanted size: ")
inserted_number: int = int(inserted_number)
while number >= 0 and number <= inserted_number:
    number = number + 1
    dot = "." * inserted_number
    print(dot)

# vs
# print (" ..... \n ..... \n ..... \n .....\n .....")

# DONE
