import requests
0
endpoint = "http://127.0.0.1:8000/api/products/"

data = {
    'title' : " product new 4",
    "content" : 'hi im 4',
}

get_response = requests.get( endpoint, json=data ) # HTTP request
print('list=', get_response.json())
get_response = requests.post( endpoint, json=data ) # HTTP request
print('create=', get_response.json())
