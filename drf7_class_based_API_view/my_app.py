import requests
import json


URL = "http://127.0.0.1:8000/student_api/"

headers = {'content-Type': "application/json"}

# creating a GET method
def get_data(id = None):
    data = {}
    if id is not None:
        data = {'id':id}

    json_data = json.dumps(data)
    r = requests.get(url = URL, headers = headers, data = json_data)
    final_data = r.json()

    print(final_data)


# calling the GET function without pk
get_data()

# calling the GET function with pk
# get_data(1)




# creating a POST method
def post_data():
    data = {
        "name":"rasel",
        "roll":99,
        "city":"mohakhali"
    }

    json_data = json.dumps(data)

    r = requests.post(url = URL, headers = headers, data = json_data)

    final_data = r.json()

    print(final_data)


# calling the POST function
# post_data()




# creating a UPDATE method
def update_data(id):
    data = {
        "id": id,
        "name": "saiful islam",
        "roll": 105,
        "city": "Baridhara DOHS"
    }

    json_data = json.dumps(data)

    r = requests.put(url = URL, headers = headers, data = json_data)

    final_data = r.json()

    print(final_data)


# calling the UPDATE function
# update_data(3)




# creating a DELETE method
def delete_data(id):
    data = {'id':id}

    json_data = json.dumps(data)
    r = requests.delete(url = URL, headers = headers, data = json_data)
    final_data = r.json()

    print(final_data)


# calling the DELETE function
# delete_data(3)


