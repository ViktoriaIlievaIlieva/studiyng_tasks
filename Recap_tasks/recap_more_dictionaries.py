# Create a program that asks the user for a command. When a command finishes he is asked for a new one.
# The program should quit when the user types "quit" as a command

# We need to create an 'english dictionary' program
# For this we will have a dictionary and:
# If the user enters the command "add" we ask him for a word and a description of that word and add it to the dictionary
#   (the word should be the key)
# If the user enters the command "search" we ask him for a word and print "No such word" if the word doesn't exist in the dictionary
#   and the description if the word does exist


wanted_command = True

english_dictionary = {}


while wanted_command:
    command_1 = input (" Insert command: \n Add \n Search \n Quit")
    if command_1 == "add":
        new_word = input ("Insert new word: ")
        new_word_description = input (" Insert description for the new word: ")
        english_dictionary [new_word] = new_word_description


    elif command_1 == "search":
        search_word = input ("Insert word that you want to find: ")
        words_in_dict = english_dictionary.keys()
        if search_word in words_in_dict:
            print (english_dictionary[search_word])
        else:
            print ("No such word ")

        # search_word = input("Insert word that you want to find: ")
        # found_word = False
        # for value in english_dictionary:
        #     if value == search_word:
        #         found_word = True
        #
        # if found_word:
        #     print (english_dictionary[search_word])
        # else:
        #     print("No such word")


    elif command_1 == "quit":
        wanted_command = False


# DONE
