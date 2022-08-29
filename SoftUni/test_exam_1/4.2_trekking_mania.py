# Задача 4. Трекинг мания
# Катерачи от цяла България се събират на групи и набелязват следващите върхове за изкачване. Според размера на групата,
# катерачите ще изкачват различни върхове.
# Група до 5 човека– Мусала
# Група от 6 до 12 – Монблан
# Група от 13 до 25 – Килиманджаро
# Група от 26 до 40 – К2
# Група от 41 или повече – Еверест
# Да се напише програма, която изчислява процента на катерачите изкачващи всеки връх.
# Вход
# От конзолата се четат поредица от числа, всяко на отделен ред:
# На първия ред – броя на групите от катерачи – цяло число в интервала [1...1000]
# За всяка една група на отделен ред – броя на хората в групата – цяло число в интервала [1...1000]
# Изход
# Да се отпечатат на конзолата 5 реда, всеки от които съдържа процент между 0.00% и 100.00% с точност до втората цифра
# след десетичната запетая.
# Първи ред - процентът изкачващи Мусала
# Втори ред – процентът изкачващи Монблан
# Трети ред – процентът изкачващи Килиманджаро
# Четвърти ред – процентът изкачващи К2
# Пети ред – процентът изкачващи Еверест


num_groups: int = int(input())

all_climbers: float = 0

p1: float = 0
p2: float = 0
p3: float = 0
p4: float = 0
p5: float = 0

for group in range(0, num_groups):
    num_people_in_group: int = int(input())
    all_climbers += num_people_in_group
    if num_people_in_group <= 5:
        peek = "Musala"
        p1 += num_people_in_group
    elif 6 <= num_people_in_group <= 12:
        peek = "Mont Blanc"
        p2 += num_people_in_group
    elif 13 <= num_people_in_group <= 25:
        peek = "Kilimanjaro"
        p3 += num_people_in_group
    elif 26 <= num_people_in_group <= 40:
        peek = "K2"
        p4 += num_people_in_group
    elif num_people_in_group >= 41:
        peek = "Everest"
        p5 += num_people_in_group

p1 = (p1 / all_climbers) * 100
p2 = (p2 / all_climbers) * 100
p3 = (p3 / all_climbers) * 100
p4 = (p4 / all_climbers) * 100
p5 = (p5 / all_climbers) * 100

print(f"{p1:.2f}%")
print(f"{p2:.2f}%")
print(f"{p3:.2f}%")
print(f"{p4:.2f}%")
print(f"{p5:.2f}%")

