import json
import jsonpath
import requests
import requests

url = "https://reqres.in/api/users"

data = {
    "name": "Arun",
    "job": "QA Engineer Automation"
}

json_data = json.dumps(data)
response = requests.post(url, data=json_data)

print(response.status_code)
print(response.content)

if response.status_code == 201:
    json_response = response.json()
    ids = jsonpath.jsonpath(json_response, "$..id")
    print(ids)
