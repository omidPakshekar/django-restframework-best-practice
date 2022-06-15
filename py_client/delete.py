import requests

product_id = input("enter product id= ")
try:
    product_id = int(product_id)
except :
    product_id = None
    print(f'{product_id} not a valid id')
if product_id:
    endpoint = f"http://127.0.0.1:8000/api/products/{product_id}/delete/"

    # get_response = requests.get(endpoint, params={'abc' : 123}, json={'query':"hello world"}) # HTTP request
    get_response = requests.delete( endpoint ) # HTTP request
    print('json=', get_response.status_code, get_response.status_code==204)
