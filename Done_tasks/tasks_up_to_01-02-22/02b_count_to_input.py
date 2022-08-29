# Create a program that asks for a positive number
# Then it prints the values from 0 to that number

positive_number: str = input("Insert a positive number: ")
positive_number: int = int(positive_number)

count_value: int = 0
while count_value >= 0 and count_value < positive_number: 
    count_value = count_value + 1
    print(count_value)

# DONE
