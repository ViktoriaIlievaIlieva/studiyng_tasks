# ⦁	Сумиране на гласните букви
# Да се напише програма, която чете текст (стринг), въведен от потребителя, и изчислява и отпечатва сумата от
# стойностите на гласните букви според таблицата по-долу:

# буква	    a	e	i	o	u
# стойност	1	2	3	4	5

string: str = input()
suma: int = 0

a: int = 1
e: int = 2
i: int = 3
o: int = 4
u: int = 5

for value in string:
    if value == "a":
        suma += a
    elif value == "e":
        suma += e
    elif value == "i":
        suma += i
    elif value == "o":
        suma += o
    elif value == "u":
        suma += u

print(suma)

# DONE
