import json
import requests
BASE_URL = 'http://127.0.0.1:8000/'
ENDPOINT = 'api/'
def get_resourse(id=None):
    data = {
    'id':id
    }
    resp = requests.get(BASE_URL+ENDPOINT,data = json.dumps(data))
    print(resp.json())
    print(resp.status_code)

def create_resourse():
    data = {
    'eno':600,
    'ename':'sunny',
    'esal':60000,
    'eaddr':'newyork'
    }
    resp = requests.post(BASE_URL+ENDPOINT,data = json.dumps(data))
    print(resp.json())
    print(resp.status_code)

def delete_resourse(id=None):
    data = {
    'id':id
    }
    resp = requests.delete(BASE_URL+ENDPOINT,data = json.dumps(data))
    print(resp.json())
    print(resp.status_code)

def update_resourse(id=None):
    data = {
    'id':id,
    'ename':'katrina',
    'eaddr':'london'
    }
    resp = requests.put(BASE_URL+ENDPOINT,data = json.dumps(data))
    print(resp.json())
    print(resp.status_code)

# create_resourse()
get_resourse(1)
# delete_resourse(3)
# update_resourse(3)
