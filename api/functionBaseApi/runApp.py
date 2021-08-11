import requests
import json

URL = 'http://127.0.0.1:8000/stuinfo/'

def get_data(id = None):
    data = {}
    if id is not None:
        data = {'id':id}
    json_data = json.dumps(data)
    headers = {'content-Type':'application/json'}
    r = requests.get(url = URL,headers = headers,data = json_data)
    data = r.json()
    print(data)

# get_data()

def post_data():
    data = {
        'name':'post_name',
        'rollno':20,
        'city':'pst_city'
    }
    header = {'content-Type':'application/json'}
    json_data = json.dumps(data)
    r = requests.post(url=URL,data= json_data,headers = header)
    data = r.json()
    print(data)

# post_data()

def put_date():
    data = {
        'id':4,
        'name':'update_data',
        'rollno':10,
    }

    header = {'content-Type':'application/json'}
    json_data = json.dumps(data)
    r = requests.put(url=URL,data= json_data,headers = header)
    data = r.json()
    print(data)

# put_date()

def delete():
    data = {'id':4}
    header = {'content-Type':'application/json'}
    json_data = json.dumps(data)
    r = requests.delete(url=URL,data= json_data,headers = header)
    data = r.json()
    print(data)
delete()





