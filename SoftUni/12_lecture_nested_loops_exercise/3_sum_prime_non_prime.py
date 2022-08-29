# ⦁	Суми прости и непрости числа
# Напишете програма, която чете от конзолата цели числа, докато не се получи команда "stop".
# Да се намери сумата на всички въведени прости и сумата на всички въведени непрости числа.
# Тъй като по дефиниция от математиката отрицателните числа не могат да бъдат прости, ако на входа се
# подаде отрицателно число, да се изведе следното съобщение "Number is negative.". В този случай въведено число се
# игнорира и не се прибавя към нито една от двете суми, а програмата продължава своето изпълнение, очаквайки
# въвеждане на следващо число.
# На изхода да се отпечатат на два реда двете намерени суми в следния формат:
# ⦁	"Sum of all prime numbers is: {prime numbers sum}"
# ⦁	"Sum of all non prime numbers is: {nonprime numbers sum}"

suma_prime: int = 0
suma_non_prime: int = 0

number: str = input()

while number != "stop":
    count: int = 0

    if int(number) < 0:
        print("Number is negative.")

    else:

        for index in range(1, int(number)):
            if int(number) % index == 0:
                count += 1

        if count > 1:
            suma_non_prime += int(number)
        else:
            suma_prime += int(number)

    number: str = input()

print(f"Sum of all prime numbers is: {suma_prime}")
print(f"Sum of all non prime numbers is: {suma_non_prime}")
