# Поспаливата котка Том
# Котката Том обича по цял ден да спи, за негово съжаление стопанинът му си играе с него винаги когато  има свободно
# време. За да се наспи добре, нормата за игра на Том е 30 000  минути в година. Времето за игра на Том зависи от
# почивните дни на стопанина му:
# Когато е на работа, стопанинът му си играе с него по 63 минути на ден.
# Когато почива, стопанинът му си играе с него  по 127 минути на ден.
# Напишете програма, която въвежда броя почивни дни и отпечатва дали Том може да се наспи добре и колко е разликата
# от нормата за текущата година, като приемем че годината има 365 дни.
# Пример: 20 почивни дни -> работните дни са 345 (365 – 20 = 245). Реалното време за игра е 24 275 минути
# (345 * 63 + 20 *127).  Разликата от нормата е 5 725 минути (30 000 – 24 275 = 5 725) или 95 часа и 25 минути.
# Вход
# Входът се чете от конзолата и се състои от едно число – броят почивни дни – цяло число в интервала [0...365]
# Изход
# На конзолата трябва да се отпечатат два реда.

# Ако времето за игра на Том е над нормата за текущата година:
#  На първия ред отпечатайте: “Tom will run away”
#  На втория ред отпечатайте разликата от нормата във формат:
# “{H} hours and {M} minutes more for play”

# Ако времето за игра на Том е под нормата за текущата година:
# На първия ред отпечатайте: “Tom sleeps well”
#  На втория ред отпечатайте разликата от нормата във формат:
# “{H} hours and {M} minutes less for play”

# нормата за игра на Том е 30 000  минути в година
# на работа, стопанинът му си играе с него по 63 минути на ден
# почива, стопанинът му си играе с него  по 127 минути на ден
# годината има 365 дни


number_rest_days: int = int(input())
best_play_time_for_year = 30000
min_work_days_play = 63
min_rest_days_play = 127
year = 365

time_for_play = (number_rest_days * min_rest_days_play) + ((365 - number_rest_days) * min_work_days_play)

if time_for_play > best_play_time_for_year:
    print("Tom will run away")
    different_hours = int((time_for_play - best_play_time_for_year) / 60)
    different_min = (time_for_play - best_play_time_for_year) % 60

    print(f"{different_hours} hours and {different_min} minutes more for play")

elif time_for_play < best_play_time_for_year:
    print("Tom sleeps well")
    different_hours = int((best_play_time_for_year - time_for_play) / 60)
    different_min = (best_play_time_for_year - time_for_play) % 60
    print(f"{different_hours} hours and {different_min} minutes less for play")

