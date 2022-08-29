# Draw a triangle in the console by printing dots (.).
# The triangle size must be taken from input from the user

# Example of a 5x5 triangle:
# .
# ..
# ...
# ....
# .....

dot: str = "."
max: str = input(" Insert number of rows ")
max: int = int(max)
number: int = 0
while number >= 0 and number < max: 
    number = number + 1
    print(dot)
    dot = dot + "."

# DONE
