# ⦁	Билети за кино
# Вашата задача е да напишете програма, която да изчислява процента на билетите за всеки тип от продадените билети:
# студентски(student), стандартен(standard) и детски(kid), за всички прожекции.
# Трябва да изчислите и колко процента от залата е запълнена за всяка една прожекция.
# Вход
# Входът е поредица от цели числа и текст:
# ⦁	На първия ред до получаване на командата "Finish" - име на филма – текст
# ⦁	На втори ред – свободните места в салона за всяка прожекция – цяло число [1 … 100]
# ⦁	За всеки филм, се чете по един ред до изчерпване на свободните места в залата или до получаване на командата "End":
# ⦁	Типа на закупения билет - текст ("student", "standard", "kid")
# Изход
# На конзолата трябва да се печатат следните редове:
# ⦁	След всеки филм да се отпечата, колко процента от кино залата е пълна
# "{името на филма} - {процент запълненост на залата}% full."
# ⦁	При получаване на командата "Finish" да се отпечатат четири реда:
# ⦁	"Total tickets: {общият брой закупени билети за всички филми}"
# ⦁	"{процент на студентските билети}% student tickets."
# ⦁	"{процент на стандартните билети}% standard tickets."
# ⦁	"{процент на детските билети}% kids tickets."

all_bought_tickets: int = 0
student_tickets: int = 0
standard_tickets: int = 0
kid_tickets: int = 0

film_name: str = input()
while film_name != "Finish":
    free_places: int = int(input())

    all_places: int = 0

    ticket_type: str = input()
    while ticket_type != "End":
        if ticket_type == "student":
            student_tickets += 1

        elif ticket_type == "standard":
            standard_tickets += 1

        elif ticket_type == "kid":
            kid_tickets += 1

        all_places += 1

        if free_places > all_places:
            ticket_type: str = input()
        else:
            break

    all_bought_tickets += all_places


    percent_salon: float = all_places / free_places * 100
    print(f"{film_name} - {percent_salon:.2f}% full.")
    film_name: str = input()

print(f"Total tickets: {all_bought_tickets}")

percentage_students: float = student_tickets / all_bought_tickets * 100
print(f"{percentage_students:.2f}% student tickets.")
percentage_standard: float = standard_tickets / all_bought_tickets * 100
print(f"{percentage_standard:.2f}% standard tickets.")
percentage_kids: float = kid_tickets / all_bought_tickets * 100
print(f"{percentage_kids:.2f}% kids tickets.")

