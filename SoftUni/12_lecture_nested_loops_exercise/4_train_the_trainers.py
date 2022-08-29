# ⦁	Train the Trainers
# Курсът "Train the trainers" е към края си и финалното оценяване наближава. Вашата задача е да помогнете на журито,
# което ще оценява презентациите, като напишете програма, в която да изчислява средната оценка от представянето на
# всяка една презентация от даден студент, а накрая - средния успех от всички тях.
# От конзолата на първият ред се прочита броят на хората в журито n - цяло число.
# След това на отделен ред се прочита името на презентацията – текст.
# За всяка една презентация на нов ред се четат n - на брой оценки - реално число.
# След изчисляване на средната оценка за конкретна презентация, на конзолата се печата:
#  "{името на презентацията} - {средна оценка}."
# След получаване на команда "Finish", на конзолата се печата "Student's final assessment is {среден успех от всички
# презентации}." и програмата приключва.
# Всички оценки трябва да бъдат форматирани до втория знак след десетичната запетая.


numbers_jury: int = int(input())

all_scores: float = 0
count: int = 0

name_presentation: str = input()
while name_presentation != "Finish":
    count += 1
    project_score: float = 0
    for _ in range(0, numbers_jury):
        score: float = float(input())
        project_score += score
    final_project_score = project_score / numbers_jury
    all_scores += final_project_score
    print(f"{name_presentation} - {final_project_score:.2f}.")
    name_presentation = input()

final_score: float = all_scores / count


print(f"Student's final assessment is {final_score:.2f}.")

