import requests
import json

url = "https://reqres.in/api/users/2"

response = requests.get(url)
json_value = json.loads(response.text)
json_data = json.dumps(json_value)
with open("single_user.json", "w") as file:
    file.write(json_data)

with open("single_user.json", "r") as file:
    read_data = file.read()
    print(read_data)
