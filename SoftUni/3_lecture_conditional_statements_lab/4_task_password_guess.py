# Познай паролата
# Да се напише програма, която чете парола (текст), въведена от потребителя и проверява дали въведената парола съвпада
# с фразата "s3cr3t!P@ssw0rd". При съвпадение да се изведе "Welcome". При несъвпадение да се изведе "Wrong password!".

correct_pass: str = "s3cr3t!P@ssw0rd"
password: str = input()

if password == correct_pass:
    print("Welcome")
else:
    print("Wrong password!")

# variant

print("Welcome" if password == correct_pass else "Wrong password!")
