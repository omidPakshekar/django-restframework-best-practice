import requests

endpoint = "https://httpbin.org/status/200"
endpoint = "http://127.0.0.1:8000/api/"

# get_response = requests.get(endpoint, params={'abc' : 123}, json={'query':"hello world"}) # HTTP request
get_response = requests.post(endpoint, json={'tilte':"new title"}) # HTTP request

# print('text=', get_response.text) # print aw text response
# print('*'*10)
# print('status=', get_response.status_code)
print('json=', get_response.json())


# htpp request -> Html
# Rest API HTTP request -> JSON
# JAVAScript object notaion ~ python Dict
# print(get_response.json())
