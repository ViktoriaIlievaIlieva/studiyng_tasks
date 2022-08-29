# You will create an exam app

# The questions are in a json file "exam.json"

# The file contains a list of dictionaries
# Each dictionary contains the keys:
# "question" - the value will contain the question itself
# "a" - the text for answer 'a'
# "b" - the text for answer 'b'
# "c" - the text for answer 'c'
# "correct" = the key for the correct answer

# Ask the user for new question
# Ask the user for answer a
# Ask the user for answer b
# Ask the user for answer c
# Ask the user for which one is the correct answer

# Create a dictionary with the new question
# Add the dictionary of the question created to the list of questions in "exam.json" and save the file still as json
# (without breaking its format)

user_new_question = input ("Insert a new question:")
user_new_answer_a = input("Insert answer \"a\":")
user_new_answer_b = input("Insert answer \"b\": ")
user_new_answer_c = input("Insert answer \"c\": ")
user_correct_answer = input ("Insert the letter af the correct answer: a, b or c: ")

new_question = {}
new_question["question"] = user_new_question
new_question["a"] = user_new_answer_a
new_question["b"] = user_new_answer_b
new_question["b"] = user_new_answer_c
new_question["correct"] = user_correct_answer

import json
file = open ("exam.json", "r")
file_content = file.read()
file.close()

python_list = json.loads(file_content)

python_list.append (new_question)

json_list_of_users = json.dumps(python_list)

file = open ("exam.json", "w")
file.write (json_list_of_users)
file.close()