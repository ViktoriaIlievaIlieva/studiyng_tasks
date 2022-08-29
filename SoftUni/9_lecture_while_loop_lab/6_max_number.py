# ⦁	Най-голямо число
# Напишете програма, която до получаване на командата "Stop", чете цели числа, въведени от потребителя,  намира
# най-голямото измежду тях и го принтира. Въвежда се по едно число на ред.

biggest_number = -9223372036854775807

number: str = input()
while number != "Stop":
    num: int = int(number)
    if num > biggest_number:
        biggest_number = num
    number: str = input()

print(biggest_number)
