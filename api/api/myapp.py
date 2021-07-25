import requests
import json


def create():
    URL = "http://127.0.0.1:8000/stucreate/"

    data={
        "name":"model",
        "rollno":100,
        "city":"Delhi",
    }


    json_data = json.dumps(data)

    r = requests.post(url = URL,data = json_data).json()
    # data = r.json()
    print(r)

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

def validate_example():
    URL = "http://127.0.0.1:8000/stuvalidationexample/"

    data={
        "name":"rohit",
        "rollno":199,
        "city":"noida",
    }


    json_data = json.dumps(data)
    r = requests.post(url = URL,data = json_data).json()
    # data = r.json()

    print(r)

# validate_example()