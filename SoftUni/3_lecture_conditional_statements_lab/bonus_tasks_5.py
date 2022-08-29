# Фирма
# Фирма получава заявка за изработването на проект, за който са необходими определен брой часове.
# Фирмата разполага с определен брой дни. През 10% от дните служителите са на обучение и не могат да работят по проекта.
# Един нормален работен ден във фирмата е 8 часа. Всеки служител може да работи по проекта в извънработно време
# по 2 часа на ден.
# Часовете трябва да са закръглени към по-ниско цяло число (Например –> 6.98 часа се закръглят на 6 часа).
# Напишете програма, която изчислява дали фирмата може да завърши проекта навреме и колко часа не достигат или остават.

# Вход
# Входът се чете от конзолата и съдържа точно 3 реда:
# На първия ред са необходимите часовете – цяло число в интервала [0 ... 200 000]
# На втория ред са дните, с които фирмата разполага – цяло число в интервала [0 ... 20 000]
# На третия ред е броят на служителите, работещи извънредно – цяло число в интервала [0 ... 200]

# Изход
# Да се отпечата на конзолата един ред:
# Ако времето е достатъчно:
# “Yes!{оставащите часове} hours left.”

# Ако  времето НЕ Е достатъчно:
# “Not enough time!{недостигащите часове} hours needed.“

import math

hours_needed_to_finish = int(input())
number_days: int = int(input())
number_workers: int = int(input())

education_days: float = (number_days / 100) * 10
work_days: float = number_days - education_days

work_hours: int = math.floor(work_days * 10 * number_workers)

difference_in_hours = abs(math.floor(work_hours - hours_needed_to_finish))

if hours_needed_to_finish <= work_hours:
    print(f"Yes!{difference_in_hours} hours left.")
else:
    print(f"Not enough time!{difference_in_hours} hours needed.")



# -----------------------------------------------------------------------

import math

hours_needed_to_finish = int(input())
number_days: int = int(input())
number_workers: int = int(input())

education_days: float = (number_days / 100) * 10
work_days: float = number_days - education_days

work_hours: int = math.floor(work_days * 8)
work_hours = work_hours + 2 * number_workers * number_days

difference_in_hours = abs(math.floor(work_hours - hours_needed_to_finish))

if hours_needed_to_finish <= work_hours:
    print(f"Yes!{difference_in_hours} hours left.")
else:
    print(f"Not enough time!{difference_in_hours} hours needed.")
