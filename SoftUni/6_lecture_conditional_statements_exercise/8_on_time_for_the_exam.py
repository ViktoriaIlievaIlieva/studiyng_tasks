# ⦁	Навреме за изпит
# Студент трябва да отиде на изпит в определен час (например в 9:30 часа). Той идва в изпитната зала в даден час на
# пристигане (например 9:40). Счита се, че студентът е дошъл навреме, ако е пристигнал в часа на изпита или до половин
# час преди това. Ако е пристигнал по-рано повече от 30 минути, той е подранил. Ако е дошъл след часа на изпита, той е
# закъснял. Напишете програма, която прочита време на изпит и време на пристигане и отпечатва дали студентът е дошъл
# навреме, дали е подранил или е закъснял и с колко часа или минути е подранил или закъснял.
# Вход
# От конзолата се четат 4 цели числа (по едно на ред), въведени от потребителя:
# ⦁	Първият ред съдържа час на изпита - цяло число от 0 до 23;
# ⦁	Вторият ред съдържа минута на изпита - цяло число от 0 до 59;
# ⦁	Третият ред съдържа час на пристигане - цяло число от 0 до 23;
# ⦁	Четвъртият ред съдържа минута на пристигане - цяло число от 0 до 59.
# Изход
# На първия ред отпечатайте:
# ⦁	"Late", ако студентът пристига по-късно от часа на изпита;
# ⦁	"On time", ако студентът пристига точно в часа на изпита или до 30 минути по-рано;
# ⦁	"Early", ако студентът пристига повече от 30 минути преди часа на изпита.

# Ако студентът пристига с поне минута разлика от часа на изпита, отпечатайте на следващия ред:
# ⦁	"mm minutes before the start" за идване по-рано с по-малко от час;
# ⦁	"hh:mm hours before the start" за подраняване с 1 час или повече. Минутите винаги печатайте с 2 цифри, например "1:05”;
# ⦁	 "mm minutes after the start" за закъснение под час;
# ⦁	"hh:mm hours after the start" за закъснение от 1 час или повече. Минутите винаги печатайте с 2 цифри, например "1:03”.

exam_hour: int = int(input())
exam_min: int = int(input())
arrival_hour: int = int(input())
arrival_min: int = int(input())

time_exam: int = exam_hour * 60 + exam_min
time_arrival: int = arrival_hour * 60 + arrival_min

status = ""

if time_exam - 30 > time_arrival:
    status = "early"
    print("Early")

elif time_exam == time_arrival:
    print("On time")

elif time_exam - 30 <= time_arrival < time_exam:
    status = "on time"
    print("On time")

elif time_arrival > time_exam:
    status = "late"
    print("Late")

diff = abs(time_exam - time_arrival)
diff_hour: float = diff // 60
diff_min: float = diff % 60

if status == "early":
    if diff_hour > 0:
        print(f"{diff_hour}:{diff_min:02d} hours before the start")
    else:
        print(f"{diff_min} minutes before the start")

elif status == "on time":
    print(f"{diff_min} minutes before the start")

elif status == "late":
    if diff_hour > 0:
        print(f"{diff_hour}:{diff_min:02d} hours after the start")
    else:
        print(f"{diff_min} minutes after the start")

# DONE
