# ⦁	Подготовка за изпит
# Напишете програма, в която Марин решава задачи от изпити, докато не получи съобщение "Enough" от лектора си.
# При всяка решена задача той получава оценка. Програмата трябва да приключи прочитането на данни при команда "Enough"
# или ако Марин получи определения брой незадоволителни оценки. Незадоволителна е всяка оценка, която е по-малка или
# равна на 4.
# Вход
# ⦁	На първи ред - брой незадоволителни оценки - цяло число;
# ⦁	След това многократно се четат по два реда:
# ⦁	Име на задача – текст;
# ⦁	Оценка - цяло число в интервала [2…6]
# Изход
# ⦁	Ако Марин стигне до командата "Enough", отпечатайте на 3 реда:
# ⦁	"Average score: {средна оценка}"
# ⦁	"Number of problems: {броя на всички задачи}"
# ⦁	"Last problem: {името на последната задача}"
# ⦁	Ако получи определеният брой незадоволителни оценки:
# ⦁	"You need a break, {брой незадоволителни оценки} poor grades."
# Средната оценка да бъде форматирана до втория знак след десетичната запетая.

num_bad_grades: int = int(input())

all_grades: int = 0
num_tasks: int = 0
current_bad_grades: int = 0
previous_task: str = ""

name_task: str = input()
while name_task != "Enough":
    grade = input()
    if int(grade) <= 4:
        current_bad_grades += 1
        if current_bad_grades == num_bad_grades:
            print(f"You need a break, {current_bad_grades} poor grades.")
            break
    all_grades += int(grade)
    num_tasks += 1
    previous_task = name_task
    name_task: str = input()


if name_task == "Enough":
    average: float = all_grades / num_tasks
    print(f"Average score: {average:.2f}")
    print(f"Number of problems: {num_tasks}")
    print(f"Last problem: {previous_task}")

# DONE
