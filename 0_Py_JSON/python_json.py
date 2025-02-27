import json

python_data = {'name': 'sayed', 'roll':101}
print("python_data: ", python_data)

json_data = json.dumps(python_data)
print("json_data: ", json_data)

re_python_data = json.loads(json_data)
print("re_python_data: ", re_python_data)
