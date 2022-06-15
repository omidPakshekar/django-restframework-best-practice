import requests

endpoint = "http://127.0.0.1:8000/api/products/2/"

# get_response = requests.get(endpoint, params={'abc' : 123}, json={'query':"hello world"}) # HTTP request
get_response = requests.get( endpoint ) # HTTP request
print('json=', get_response.json())
