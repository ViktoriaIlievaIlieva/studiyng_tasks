# Задача 5. Товарене на багажи
# Напишете програма, която ви помага при товаренето на куфари в багажника на самолет. Всеки самолет има определен
# капацитет на багажника. До получаване на команда "End" ще получавате обем на куфар. Обемът на всеки трети куфар
# трябва да се увеличава с 10%, поради загубата на пространство при начина на подреждане. Ако свободното пространството
# в даден момент е по-малко от обема на куфар товаренето трябва да прекъсне.
# Вход
# Първоначално се чете един ред:
# Капацитетът на багажника – реално число в диапазона [100.0…6000.0]
# След това до получаване на команда "End" или до запълване на багажника, се чете по един ред:
# Обем на куфар – реално число в диапазона [100.0…6000.0]
# Изход
# На конзолата да се отпечатат следните редове според случая:
# При получаване на командата "End" се печата:
# "Congratulations! All suitcases are loaded!"
# Ако обемът на куфара е по-голям от оставащото пространство в багажника:
# "No more space!"
# Накрая винаги се отпечатва статистика – колко багажа са натоварени:
# "Statistic: {брой натоварени багажи} suitcases loaded."

capacity: float = float(input())
num_suitcases: int = 0
space_taken: float = 0

size_suitcase: str = input()
while size_suitcase != "End":
    num_suitcases += 1
    if num_suitcases % 3 == 0:
        size_third_suitcase: float = float(size_suitcase) + ((float(size_suitcase) / 100) * 10)
        space_taken += size_third_suitcase
    else:
        space_taken += float(size_suitcase)
    if space_taken > capacity:
        num_suitcases -= 1
        print("No more space!")
        break
    else:
        size_suitcase: str = input()

if space_taken <= capacity:
    print(f"Congratulations! All suitcases are loaded!")

print(f"Statistic: {num_suitcases} suitcases loaded.")
