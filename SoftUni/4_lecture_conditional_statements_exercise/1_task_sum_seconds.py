# ⦁	Сумиране на секунди
# Трима спортни състезатели финишират за някакъв брой секунди (между 1 и 50). Да се напише програма, която чете
# времената на състезателите в секунди, въведени от потребителя и пресмята сумарното им време във формат
# "минути:секунди". Секундите да се изведат с водеща нула (2  "02", 7  "07", 35  "35").

import math

first_person: int = int(input())
second_person: int = int(input())
third_person: int = int(input())

minutes: float = (first_person + second_person + third_person) / 60
seconds: float = (first_person + second_person + third_person) % 60

if seconds >= 10:
    print(f"{math.floor(minutes)}:{seconds}")
else:
    print(f"{math.floor(minutes)}:0{seconds}")

# решение с един принт
print(f"{math.floor(minutes)}:{seconds:02d}")

# DONE
