# ⦁	8. Обедна почивка
# По време на обедната почивка искате да изгледате епизод от своя любим сериал. Вашата задача е да напишете програма,
# с която ще разберете дали имате достатъчно време да изгледате епизода. По време на почивката отделяте време за обяд и
# време за отдих. Времето за обяд ще бъде 1/8 от времето за почивка, а времето за отдих ще бъде 1/4 от времето за почивка.
# Вход
# От конзолата се четат 3 реда:
# ⦁	Име на сериал – текст
# ⦁	Продължителност на епизод  – цяло число в диапазона [10… 90]
# ⦁	Продължителност на почивката  – цяло число в диапазона [10… 120]
# Изход
# На конзолата да се изпише един ред:
# ⦁	Ако времето е достатъчно да изгледате епизода:
# "You have enough time to watch {име на сериал} and left with {останало време} minutes free time."
# ⦁	Ако времето не Ви е достатъчно:
# "You don't have enough time to watch {име на сериал}, you need {нужно време} more minutes."
# Времето да се закръгли до най-близкото цяло число нагоре.

import math

name_series: str = input()
length_episode: int = int(input())
length_break: int = int(input())

lunch: float = length_break / 8
rest: float = length_break / 4
left_break: float = length_break - lunch - rest

dif: float = abs(left_break - length_episode)
dif = math.ceil(dif)

if length_episode <= left_break:
    print(f"You have enough time to watch {name_series} and left with {dif} minutes free time.")
else:
    print(f"You don't have enough time to watch {name_series}, you need {dif} more minutes.")

# DONE
