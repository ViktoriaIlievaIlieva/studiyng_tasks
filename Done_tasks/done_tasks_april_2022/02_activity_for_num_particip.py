# TASK 1 - Take a number input from the user for number of participants and from the boredapi find
# an activity for that amount of people
import requests

num_people: int = int(input("Insert people who want to participate in the activity?"))
result: bool = True
while result:
    server_response: requests.Response = requests.get("https://www.boredapi.com/api/activity/")
    if server_response.ok:
        json_data: dict = server_response.json()
        if json_data["participants"] == num_people:
            result = False
            print(json_data)

# Done

