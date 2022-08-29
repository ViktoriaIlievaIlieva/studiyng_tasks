# Task 1: Take input from the user by asking him if he wants tea. If that is what the user wants then
# print "Preparing tea right away". Otherwise ask him if he is a coffee person. If he is print "We have some coffee left.
# I will make it now.". Otherwise print "Well I will give you a glass of water".

drink = input ("Do you want tea? Yes or no?")
if drink == "yes":
    print ("Preparing tea right away")

elif drink == "no":
    drink_2 = input (" Are you a coffee person? ")
    if drink_2 == "yes":
        print ("We have some coffee left. I will make it now.")
    else:
        print ("Well I will give you a glass of water")

# DONE


# Task 2: Take input from the user by asking him for a number. If the number he provided is greater than 0 then ask
# him to write yes if the number is also lower than 100. Check if the user lied by comparing whether he inputted "yes"
# with the actual truth. If he answered "yes" and the value is lower than 100 then print "Fine".
# Otherwise print "Liar". If the number was lower or equal to 0 initially then print "I need a big number".

number = int (input (" Choose a number: "))
if number > 0:
    user_answer = input (" Is your number lower than a 100? Yes or No? ")
    if user_answer == "yes" and number < 100:
        print ("Fine")
    else:
        print ("Liar")
if number <= 0:
    print (" I need a bigger number")

# DONE
