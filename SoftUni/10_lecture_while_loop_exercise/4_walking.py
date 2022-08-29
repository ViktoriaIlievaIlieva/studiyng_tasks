# ⦁	Стъпки
# Габи иска да започне здравословен начин на живот и си е поставила за цел да върви 10 000 стъпки всеки ден.
# Някои дни обаче е много уморена от работа и ще иска да се прибере преди да постигне целта си.
# Напишете програма, която чете от конзолата по колко стъпки изминава тя всеки път като излиза през деня
# и когато постигне целта си да се изписва "Goal reached! Good job!" и колко стъпки повече е извървяла
# "{разликата между стъпките} steps over the goal!"
# Ако иска да се прибере преди това, тя ще въведе командата "Going home" и ще въведе стъпките, които е извървяла
# докато се прибира. След което, ако не е успяла да постигне целта си, на конзолата трябва да се изпише:
# "{разликата между стъпките} more steps to reach goal."

not_done = True
all_steps = 0

steps = input()
while not_done:
    if steps != "Going home":
        all_steps += int(steps)
        if all_steps < 10000:
            steps = input()
        elif all_steps >= 10000:
            not_done = False

    elif steps == "Going home":
        steps = int(input())
        all_steps += steps
        not_done = False

diff: int = abs(10000 - all_steps)

if all_steps < 10000:
    print(f"{diff} more steps to reach goal.")
elif all_steps >= 10000:
    print("Goal reached! Good job!")
    print(f"{diff} steps over the goal!")



















