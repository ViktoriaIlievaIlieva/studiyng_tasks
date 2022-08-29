# Open questionaire.json and convert its contents to python types
# Its structure is a list of strings - questions

# Ask the user for his/her fullname
# Print each of the questions of the questionaire and ask for a grade from 1 to 5
# Create a new json file using the fullname of the user + ".json" for a filename
# Save his/her answers in json format (list of numbers)


import json

file = open ("questionaire.json", "r")
file_content = file.read()
file.close()

list_with_questions = json.loads(file_content)

list_user_answers = []
user_name = input ("What is your name?")
for question in list_with_questions:
    print (question)
    grade = int (input ("Answer with grade form 1 to 5: "))
    answer_of_question = {"user_grade": grade}
    list_user_answers.append(answer_of_question)

json_list_user_answers = json.dumps(list_user_answers)

new_file = open (user_name + ".json", "w")
new_file.write (json_list_user_answers)
new_file.close()

#-------------------------------------------------

file = open ("questionaire.json", "r")
file_content = file.read()
file.close()

list_with_questions = json.loads(file_content)

list_user_answers = []
user_name = input ("What is your name?")
for question in list_with_questions:
    print (question)
    grade = int (input ("Answer with grade form 1 to 5: "))
    list_user_answers.append(grade)

json_list_user_answers = json.dumps(list_user_answers)

new_file = open (user_name + ".json", "w")
new_file.write (json_list_user_answers)
new_file.close()

