# Task 1: Create a variable for each of the following types: int, float, bool, string

text = "rose"
number = 7
float_number = 5,3
bool_variable =  True

# DONE

# Task 2: Create a program that stores two texts taken from input into two variables first_name and last_name then print those two variables
first_name = input ("What is your first name?")
last_name = input ("What is your last name?")
print (first_name)
print (last_name)

# DONE

# Task 3: Create variables like in the previous task but print those two variables added toggether on a single line with a space between them

print (first_name + " " + last_name)

# DONE

# Task 4: Can you create the same program as in the previous point but don't use any variables

print ( input (" Enter first name: ") + " " + input (" Enter last name: "))

# DONE

# Task 5: Copy the following code and without changing it (only adding after) switch the values between the two variables so that x equals the initial value of y and y equals the initial value of x and print both values
x = input("Enter x: ")
y = input("Enter y: ")

z = x
x = y
y = z

print ("X = ", x)
print ("Y = ", y)

# DONE