# По-голямото число
# Да се напише програма, която чете две цели числа въведени от потребителя и отпечатва по-голямото от двете.

x: int = int(input())
y: int = int(input())

if x > y:
    print(x)
else:
    print(y)

# variant 2

print(x if x > y else y)
