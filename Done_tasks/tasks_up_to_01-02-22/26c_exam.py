# You will create an exam app

# The questions are in a json file "exam.json"

# The file contains a list of dictionaries
# Each dictionary contains the keys:
# "question" - the value will contain the question itself
# "a" - the text for answer 'a'
# "b" - the text for answer 'b'
# "c" - the text for answer 'c'
# "correct" = the key for the correct answer

# Read the file with the questions
# Convert the file string into python types

# Write a program that generates a random number between 0 and the length of the list with questions
# Use the generated number to get that question dictionary from the list

# On a single line print just the question
# then print each answer with the letter for the answer before the text

# Ask the user to give the letter of the correct answer
# if the user gave the correct answer print "correct"
# else print "incorrect"

import random
import json

file_with_questions = open("exam.json", "r")
file_with_questions_content: str = file_with_questions.read()
file_with_questions.close()

list_with_questions:  list[dict] = json.loads(file_with_questions_content)

random_question_number: int = random.randint(0, len(list_with_questions))

question: dict = list_with_questions[random_question_number]
values_in_dictionary = question.values()


print(question["question"])
print("a: " + question["a"])
print("b: " + question["b"])
print("c: " + question["c"])

user_answer: str = input(" Write the letter with your answer:")
if user_answer == question["correct"]:
    print("Correct !!! ")
else:
    print("Incorrect! ")

# DONE
