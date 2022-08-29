# Task 3

# Find out how to make a POST request using requests. Make a post request to https://httpbin.org/anything -
# it will return a json summarizing what your request looked like on the server.

import requests

# defining the api-endpoint
url = "https://pastebin.com/api/api_post.php"

# your API key here
API_KEY = "IHpZkaqobF8wOdj4f9oKS_7DAD1YXnm1"

# your source code here
source_code = '''
print("Hello, world!")
a = 1
b = 2
print(a + b)
'''

# data to be sent to api
data = {'api_dev_key': API_KEY, 'api_option': 'paste', 'api_paste_code': source_code, 'api_paste_format': 'python'}

# sending post request and saving response as response object
response = requests.post(url, data=data)

# extracting response text
pastebin_url = response.text
print(pastebin_url)


