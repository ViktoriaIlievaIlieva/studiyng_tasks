# Count from 0 to 100
# but:
# 1. if a number is divisible by 3 then print "fizz" instead
# 2. if a number is divisible by 5 then print "buzz" instead
# 3. if a number is divisible by both 3 and 5 write "fizzbuzz" instead


number: int = 0
while number >= 0 and number < 100:
    number = number + 1
    if number % 3 == 0 and number % 5 == 0:
        print("fizzbuzz")
    elif number % 5 == 0:
        print("buzz")
    elif number % 3 == 0:
        print("fizz")
    else:
        print(number)

# DONE
