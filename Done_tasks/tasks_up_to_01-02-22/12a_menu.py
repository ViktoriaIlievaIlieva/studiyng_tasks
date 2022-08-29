# Print a menu to the user and ask for his input
# Let the user choose between 1/ Hi, 2/ Hello and 3/ Howdy and then ask him for his name
# Print the greeting he chose and then his name combined


name: str = input("Hi, What is your name? ")
greeting: str = input(" Choose the number of one of the greetings: \n 1. Hi,\n 2. Hello, \n 3. Howdy, ")
greeting: int = int(greeting)

if greeting == 1:
    print(" Hi, ", name)
elif greeting == 2:
    print("Hello, ", name)
elif greeting == 3:
    print("Howdy, ", name)


# DONE

  