import requests
import json
BASE_URL = 'http://127.0.0.1:8000/'
ENDPOINT = 'api/'

# def get_resourse(id=None):
#     p_data = {
#     'id':id,
#     }
#     resp = requests.get(BASE_URL+ENDPOINT,data = json.dumps(p_data))
#     print(resp.status_code)
#     print(resp.json())
# get_resourse(20)

# def get_all_resourse():
#     resp = requests.get(BASE_URL+ENDPOINT)
#     print(resp.status_code)
#     print(resp.json())
# get_all_resourse()

# def create_resource():
#     new_stu = {
#     'name':'vikas',
#     'rollno':1000,
#     'marks':100,
#     'addr':'nashik',
#     }
#     resp = requests.post(BASE_URL+ENDPOINT,data = json.dumps(new_stu))
#     print(resp.json())
#     print(resp.status_code)
# create_resource()

def update_resource(id=None):
    new_stu = {
    'id':id,
    'marks':65,
    'addr':'wardha'
    }
    resp = requests.put(BASE_URL+ENDPOINT,data = json.dumps(new_stu))
    print(resp.json())
    print(resp.status_code)
update_resource(input('enter some id: '))

# def delete_resource(id=None):
#     data= {
#     'id':id
#     }
#     resp = requests.delete(BASE_URL+ENDPOINT,data = json.dumps(data))
#     print(resp.json())
#     print(resp.status_code)
# delete_resource(input('enter some id: '))
