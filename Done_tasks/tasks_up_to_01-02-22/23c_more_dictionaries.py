# TASK 1
# 1. print to the console the following exam question "Which doesn't belong?"
# 2. print the answer keys and their value on the next lines using the exam_answers dictionary
# 3. ask the user to give his answer "Enter answer:"
# 4. if he answered "d" or "love" print "correct"
# 5. else if the answer he gave is not in the keys or values ask him to point an answer in the list and return to step 3
# 6. else print "Incorrect"


exam_answers: dict = {
    "a": "mushroom",
    "b": "lemon",
    "c": "grass",
    "d": "love"
}

print("Which doesn't belong? ")
print(exam_answers)

not_given_valid_answer: bool = True

while not_given_valid_answer:
    answer: str = input("Enter answer: ")

    list_with_keys = exam_answers.keys()
    list_with_values = exam_answers.values()

    if answer == "d" or answer == "love":
        print("Correct")
        not_given_valid_answer = False
    elif not (answer in list_with_keys) and not (answer in list_with_values):
        not_given_valid_answer = True
    else:
        print("Incorrect")
        not_given_valid_answer = False

# TASK 2
# print to the console the following exam question "Write a sentance containing all the words:"
# print the answer keys and their value on the next lines using the exam_answers dictionary
# ask the user to give his answer "Enter sentance:"
# google how to split a string by spaces and use what you found to split the user sentance into words
# print "correct" if the user managed to write a sentance with all the words
# else print "incorrect"


# Split-ваме str с функцията  str.split( )
# txt = "welcome to the jungle"
# x = txt.split()
# print(x)

exam_answers: dict = {
    "a": "mushroom",
    "b": "lemon",
    "c": "grass",
    "d": "love"
}

list_with_values = exam_answers.values()

print("Write a sentence containing all the words:")
print(list_with_values)

answer: str = input("Write your answer: ")

split_answer: list[str] = answer.split()

all_words_included: bool = True

for value in list_with_values:
    if not value in split_answer:
        all_words_included = False
    if all_words_included == True:
        print("Correct! ")
    else:
        print("Incorrect! ")

# DONE
