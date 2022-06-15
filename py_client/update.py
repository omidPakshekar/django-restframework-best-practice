import requests

endpoint = "http://127.0.0.1:8000/api/products/2/update/"


data = {
    'title' : 'update data',
    'price' : 1291
}

get_response = requests.put(endpoint, json=data) # HTTP request
print('json=', get_response.json())
