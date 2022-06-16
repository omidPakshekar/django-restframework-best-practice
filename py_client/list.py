from email import header
import requests
from getpass import getpass

auth_endpoint = "http://127.0.0.1:8000/api/auth/"
password = getpass()

auth_response = requests.post(auth_endpoint, json={'username' : 'omid', 'password' : password})
print('auth_response=', auth_response.json())


if auth_response.status_code == 200:
    token = auth_response.json()['token']    
    headers = {
        "Authorization" : f"Bearer {token}"
    }
    endpoint = "http://127.0.0.1:8000/api/products/"


    get_response = requests.get( endpoint, headers=headers) # HTTP request
    print('data=', get_response.json())





























