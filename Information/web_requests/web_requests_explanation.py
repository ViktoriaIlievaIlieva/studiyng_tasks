import requests


# Requests is a library that allows you to make web requests
# This task involves the GET request type

# Usually you ask regular servers like the ones that you open in your browser (chrome)
# but you use a special URL that returns JSON
# These special URLs are called an API (Application Programming Interface)

# Here is an example where we ask the site https://www.boredapi.com/
# to give us fun activities to do:

server_response: requests.Response = requests.get("https://www.boredapi.com/api/activity/")

# the server_response will be a special variable that will indicate whether the request succeeded
# you can use the attribute ok

if server_response.ok:
    json_data: dict = server_response.json()
    print(json_data)

# except JSON you can also download stuff like:

server_response: requests.Response = requests.get("https://www.nasa.gov/sites/default/files/thumbnails/image/curiosity_selfie.jpg")

if server_response.ok:
    content = server_response.content

    file = open("web_requests_explanation.jpg", "wb")
    file.write(content)
    file.close()




