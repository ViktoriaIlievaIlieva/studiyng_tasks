# Draw a triangle of 50x50 in the console by printing dots (.). 

# Example of a 5x5 triangle:
# .
# ..
# ...
# ....
# .....


dot: str = ""
number: int = 0
while number >= 0 and number < 51:
    number = number + 1
    dot = dot + "."
    print(dot)

# DONE
