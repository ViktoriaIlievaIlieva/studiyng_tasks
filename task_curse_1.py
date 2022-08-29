sample_dict = {
    "mouth": "Mund",
    "finger": "Finger",
    "leg": "Bein",
    "hand": "Hand",
    "face": "Gesicht",
    "nose": "Nase"
}

word = input("Enter a word in English or EXIT: ")

while word != "EXIT":
    values = sample_dict.values()
    if word in values:
        print(f"Translation: {sample_dict[word]}")
    else:
        print("No match!")

    word = input("Enter a word in English or EXIT: ")

else:
    print("Bye!")
