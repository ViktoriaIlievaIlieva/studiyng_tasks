# Find how to make a beep sound from code
# Find out how to make the program "sleep" for 3 seconds and then beep

# melody.json contains information on how to play a beep melody
# the file is a list of dictionaries each of which having a command and a values keys
# if the command is "Beep" there will be two values in a list - frequency and duration
# if the command is "Sleep" there will be only one value the duration to sleep in milliseconds (1 second = 1000 milliseconds)
#
# Play the melody by following the commands
import time
import winsound
# frequency = 2500  # Set Frequency To 2500 Hertz
# duration = 1000  # Set Duration To 1000 ms == 1 second
# winsound.Beep(frequency, duration)

import json
file = open("melody.json", "r")
file_content: str = file.read()
file.close()

list_with_json_dict: dict = json.loads(file_content)

frequency: int = 0
duration: int = 0

for dictionary in list_with_json_dict:
    if dictionary["command"] == "Beep":
        list_with_values: list = dictionary["values"]
        frequency = list_with_values[0]
        duration = list_with_values[1]
        winsound.Beep(frequency, duration)

    elif dictionary["command"] == "Sleep":
        duration = dictionary["values"] / 1000
        time.sleep(duration)


# Done




