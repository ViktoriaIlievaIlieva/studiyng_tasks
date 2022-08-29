# ⦁	Най-малко число
# Напишете програма, която до получаване на командата "Stop", чете цели числа, въведени от потребителя,
# намира най-малкото измежду тях и го принтира. Въвежда се по едно число на ред.

smallest_number = 9223372036854775807

number: str = input()
while number != "Stop":
    num: int = int(number)
    if num < smallest_number:
        smallest_number = num
    number: str = input()

print(smallest_number)

