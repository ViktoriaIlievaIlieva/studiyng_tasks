# Съединяване на текст и числа
# Напишете програма, която прочита от конзолата име, фамилия, възраст и град и печата следното съобщение:
# "You are <firstName> <lastName>, a <age>-years old person from <town>."

name = input ()
family_name = input ()
age = int (input ())
city = input ()

print (f"You are {name} {family_name}, a {age}-years old person from {city}.")

