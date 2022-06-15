import requests

endpoint = "http://127.0.0.1:8000/api/products/"

data = {
    'title' : " product new 2",
    "content" : 'hi im 2',
}

get_response = requests.post( endpoint, json=data ) # HTTP request
print('json=', get_response.json())
