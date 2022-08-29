# ⦁	Парола
# Напишете програма, която първоначално прочита име и парола на потребителски профил. След това чете парола за вход.
# ⦁	при въвеждане на грешна парола: потребителя да се подкани да въведе нова парола.
# ⦁	при въвеждане на правилна парола: отпечатваме "Welcome {username}!".

name: str = input()
true_password = input()

insert_pass = input()
while insert_pass != true_password:
    insert_pass = input()

if insert_pass == true_password:
    print(f"Welcome {name}!")

# DONE
