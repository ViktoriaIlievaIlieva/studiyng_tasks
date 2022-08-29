# Make a basic calculator for the operations: + , - , *, /
# 1. Ask the user for first number
# 2. Ask the user for the operation
# 3. Ask the user for the second number
# 5. Check which operation was written and execute it
# 6. Print the result

first_number: str = input("Insert first number: ")
operation: str = input(" Choose an operation - 1, 2, 3 or 4: \n 1. add \n 2. substract \n 3. multiply \n 4. divide \n ")
second_number: str = input("Insert second number: ")

operation: int = int(operation)
first_number: int = int(first_number)
second_number: int = int(second_number)

add: int = first_number + second_number
substract: int = first_number - second_number
multiply: int = first_number * second_number
divide: float = first_number / second_number

if operation == 1:
    print(add)
elif operation == 2:
    print(substract)
elif operation == 3:
    print(multiply)
elif operation == 4:
    print(divide)

# DONE
  