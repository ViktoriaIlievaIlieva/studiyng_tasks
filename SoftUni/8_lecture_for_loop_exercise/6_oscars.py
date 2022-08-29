# ⦁	Оскари
# Поканени сте от академията да напишете софтуер, който да пресмята точките за актьор/актриса.
# Академията ще ви даде първоначални точки за актьора.
# След това всеки оценяващ ще дава своята оценка. Точките, които актьора получава се формират от:
# дължината на името на оценяващия умножено по точките, които дава делено на две.
# Ако резултатът в някой момент надхвърли 1250.5 програмата трябва да прекъсне и да се отпечата, че дадения актьор е
# получил номинация.
# Вход
# ⦁	Име на актьора - текст
# ⦁	Точки от академията - реално число в интервала [2.0... 450.5]
# ⦁	Брой оценяващи n - цяло число в интервала[1… 20]
# На следващите n-на брой реда:
# ⦁	Име на оценяващия - текст
# ⦁	Точки от оценяващия - реално число в интервала [1.0... 50.0]
# Изход
# Да се отпечата на конзолата един ред:
# ⦁	Ако точките са над 1250.5:
# "Congratulations, {име на актьора} got a nominee for leading role with {точки}!"
# ⦁	Ако точките не са достатъчни:
# 	"Sorry, {име на актьора} you need {нужни точки} more!"
# Резултатът да се форматирана до първата цифра след десетичния знак!

actor_name: str = input()
points_from_academy: float = float(input())
number_judges: int = int(input())

all_points: float = points_from_academy

for value in range(0, number_judges):
    name_judge: str = input()
    point_from_name: int = len(name_judge)

    points_from_judge: float = float(input())
    all_points += (point_from_name * points_from_judge) / 2

    if all_points > 1250.5:
        break

if all_points <= 1250.5:
    need_points: float = abs(1250.5 - all_points)
    print(f"Sorry, {actor_name} you need {need_points:.1f} more!")
else:
    print(f"Congratulations, {actor_name} got a nominee for leading role with {all_points:.1f}!")



