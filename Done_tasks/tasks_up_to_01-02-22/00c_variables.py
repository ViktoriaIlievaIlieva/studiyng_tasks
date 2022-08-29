# Section 1 - Numbers
# 1. Write two variables (x & y)
# 2. Do the mathematical operations (+, -, *, /, %) on them and store the results in five additional variables
# 3. Print each result

x: int = 10
y: int = 4

addition: int = x + y
print(addition)
substraction: int = x - y
print(substraction)
multiplication: int = x * y
print(multiplication)
division: float = x / y
print(division)
ostatuk: int = x % y
print(ostatuk)

# Section 2 - Strings
# 1. Create two separate string variables
# 2. Combine them together and store the result in a third variable
# 3. Google and find out how to write the " (quotes) character inside a string (considering that a string is surrounded
# by quotes)
# 4. Google and find out what a 'new line' character is and how to include a new line in the middle of the string
# 5. Write a SINGLE string that prints the following text to the console: 
# "Time is relative"
# Albert Enstein

x: str = "beautiful"
y: str = "rose"
z: str = (x + " " + y)
print(z)

text: str = "\"Time is relative\" \n Albert Enstein"
print(text)

# ^ option 1
# v option 2


text1: str = '"Time is relative" \n Albert Enstein'
print(text1)
# Section 3 - Booleans
# 1. Write a boolean variable called isFemale and give it the value of your gender
# 2. Write two boolean variables (a & b) one that is equal to True and one that is equal to False
# 3. Print the following result from the operations: (a and b), (a or b), (a and not b), (not a or not b)

isFemale: bool = True

a: bool = True
b: bool = False

print(a and b)
print(a or b)
print(a and not b)
print(not a or not b)

# DONE
