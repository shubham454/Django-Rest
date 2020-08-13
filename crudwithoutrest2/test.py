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
# get_resourse(1)
def create_resourse():
    data = {
    'eno':700,
    'ename':'ashwary',
    'esal':700,
    'eaddr':'newyork'
    }
    resp = requests.post(BASE_URL+ENDPOINT,data = json.dumps(data))
    print(resp.json())
    print(resp.status_code)
# create_resourse()
def delete_resourse(id=None):
    data = {
    'id':id
    }
    resp = requests.delete(BASE_URL+ENDPOINT,data = json.dumps(data))
    print(resp.json())
    print(resp.status_code)
# delete_resourse(4)
def update_resourse(id=None):
    data = {
    'id':id,
    'ename':'katrina',
    'eaddr':'london'
    }
    resp = requests.put(BASE_URL+ENDPOINT,data = json.dumps(data))
    print(resp.json())
    print(resp.status_code)
update_resourse(30)
