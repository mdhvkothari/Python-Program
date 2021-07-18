import requests
import json


def create():
    URL = "http://127.0.0.1:8000/stucreate/"

    data={
        "name":"Tes",
        "rollno":10,
        "city":"Delhi",
    }


    json_data = json.dumps(data)

    r = requests.post(url = URL,data = json_data)
    data = r.json()
    print(data)

# create()

#for update
def update():
    URL = "http://127.0.0.1:8000/stuupdate/"

    data={
        "id":6,
        "rollno":101,
        "city":"Delhi North",
    }


    json_data = json.dumps(data)

    r = requests.put(url = URL,data = json_data)
    data = r.json()
    print(data)

# update()

def delete():
    URL = "http://127.0.0.1:8000/studelete/"

    data={"id":6}


    json_data = json.dumps(data)

    r = requests.delete(url = URL,data = json_data)
    data = r.json()
    print(data)

# delete()
