# ⦁	Почивен или работен ден
# Напишете програма която, чете ден от седмицата (текст), на английски език - въведен от потребителя.Ако денят е
# работен отпечатва на конзолата - "Working day", ако е почивен - "Weekend". Ако се въведе текст различен от ден от
# седмицата да се отпечата - "Error".

work_days: list[str] = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

day: str = input()

if day == "Monday" or day == "Tuesday" or day == "Wednesday" or day == "Thursday" or day == "Friday":
    print("Working day")
elif day == "Saturday" or day == "Sunday":
    print("Weekend")
else:
    print("Error")

# -------------------------------------------------------------------------------------------------------

def is_working_day(day: str) -> bool:
    index: int = 0
    while index < len(work_days):
        if day == work_days[index]:
            return True
        index += 1
    return False


if is_working_day(day):
    print("Working day")
elif day == "Saturday" or day == "Sunday":
    print("Weekend")
else:
    print("Error")


