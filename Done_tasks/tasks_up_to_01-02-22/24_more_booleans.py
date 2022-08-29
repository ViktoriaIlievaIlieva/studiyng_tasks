# TASK 1
# Create a function that takes a single number in its brackets
# The function generates a new random number
# The function then compares the number from brackets with the random number and:
# - RETURNs True if the number is equal or higher than the random number
# - RETURNs False if the number is lower than the random number

import random


def start(number: int) -> bool:
    random_number: int = random.randint(1, 100)
    if number >= random_number:
        return True
    elif number < random_number:
        return False

# DONE

# TASK 2
# Ask for a number from input
# Call the function that you created passing the number from input and save the result in a boolean variable
# is_higher_or_equal
# TASK 3
# If the number was lower than the random number print "No luck this time"


number: int = int(input("Choose a  number: "))

is_higher_or_equal: bool = start(number)
if is_higher_or_equal == False:
    print("No luck this time")

# DONE

# TASK 4
# Google how to check if a year is leap year
# Ask for the user to input an year
# Make a boolean variable is_a_leap_year containing True if the year that the user entered is a leap year and
# False otherwise

import calendar

year: int = int(input("Insert an year: "))

is_a_leap_year: bool = calendar.isleap(year)

if is_a_leap_year == True:
    print("The year is leap")
elif is_a_leap_year == False:
    print("The year is not leap")

# DONE

# TASK 5
# If the number was lower but it is a leap year - print "But its a leap year so you win half a star"
# If the number is higher or equal and is a leap year - print "Wow you won... and its a leap year so you have 2 stars"
# If the number is higher but it is not a leap year - print "You won! Here is a star"

if is_higher_or_equal == False and is_a_leap_year == True:
    print("But its a leap year so you win half a star")
elif is_higher_or_equal == True and is_a_leap_year == True:
    print("Wow you won... and its a leap year so you have 2 stars")
elif is_higher_or_equal == True and is_a_leap_year == False:
    print("You won! Here is a star")

# DONE
