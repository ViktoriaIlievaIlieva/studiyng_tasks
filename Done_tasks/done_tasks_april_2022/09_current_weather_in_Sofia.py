# Task 4

# Using the documentation on https://openweathermap.org/api make a program that prints out the current weather in Sofia.
# For example, it should print: "Clear - +12 degrees"
# Use the following API key "1b57540945bf7c2713abaf1c400d95f8"

import requests

lat: str = "42.6977"
lon: str = "23.3219"
api_key: str = "1b57540945bf7c2713abaf1c400d95f8"

url: str = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}"

# sending get request and saving the response as response object
request = requests.get(url)

# extracting data in json format
data: dict = request.json()
print(f"The weather in {data['name']} - {data['weather'][0]['description']} - {data['main']['temp']} F")

