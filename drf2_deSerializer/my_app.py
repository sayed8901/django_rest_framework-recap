import requests
import json


URL = "http://127.0.0.1:8000/stud_create/"

data = {
    'name' : 'Sohel',
    'roll' : 103,
    'city' : 'Narayanganj'
}

json_data = json.dumps(data)

r = requests.post(url=URL, data=json_data)

final_data = r.json()

print(final_data)
