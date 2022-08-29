# Task 3

# Find out how to make a POST request using requests. Make a post request to https://httpbin.org/anything -
# it will return a json summarizing what your request looked like on the server.

import requests

url = 'https://httpbin.org/anything'
myobj = {'somekey': 'somevalue'}

x = requests.post(url, data = myobj)

print(x.text)