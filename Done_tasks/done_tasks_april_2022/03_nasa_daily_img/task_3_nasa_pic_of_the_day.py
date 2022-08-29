# Using this API print the title of today's picture as well as its description. Also download and save the picture.
# TASK 2 - NASA provides a "picture of the day" API.
# LIMIT: 50 request per day / 30 per hour
import requests

nasa_password: str = "cXgWeLJ3MJYMpENdZBY725O3erhNQIVU5cyD0lsL"
daily_nasa_picture_url = f"https://api.nasa.gov/planetary/apod?api_key={nasa_password}"

server_response: requests.Response = requests.get(daily_nasa_picture_url)
json_data: dict = server_response.json()
print(json_data["title"])
print(json_data["explanation"])

server_response: requests.Response = requests.get(json_data["url"])
if server_response.ok:

    content = server_response.content

    file = open("nasa_img.jpg", "wb")
    file.write(content)
    file.close()
