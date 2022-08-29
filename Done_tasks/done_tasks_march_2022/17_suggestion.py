# TASK -
# Create a program that accepts commands and waits for the command "quit" to exit.
# The program should have a list of books and each book has information about its title and whereabouts
# - Create a command for adding a book to the list - "add"
# - Create a command for removing a book from the list by its number in the list - "remove"
# - Create a command for printing out all the books - "list"

# Use 'thefuzz' library to compare the user input command with the actual command name and execute the command
# if the score (similarity ration) is greater than 80
# (thefuzz - provides functions for "fuzzy" comparison of text - meaning a typo wouldn't result in a fail)

from thefuzz import fuzz

class Library:

    def __init__(self):
        self.library: list = []

    def add(self, title, whereabouts):
        dictionary = {"title": title, "whereabouts": whereabouts}
        self.library.append(dictionary)

    def remove(self, number):
        self.library.pop(number)

    def print_list(self):
        for book in self.library:
            print(book["title"], end=",")
            print(book["whereabouts"])


library = Library()

command: str = input("Insert command: ")


while fuzz.ratio(command, "quit") <= 80:
    if fuzz.ratio(command, "add") >= 80:
        title = input("Input book name: ")
        whereabouts = input("Insert book whereabouts: ")
        library.add(title, whereabouts)

    elif fuzz.ratio(command, "remove") >= 80:
        num_book_remove = int(input("Insert number of book you want to remove: "))
        library.remove(num_book_remove)

    elif fuzz.ratio(command, "list") >= 80:
        library.print_list()

    command = input("Insert command: ")

# done