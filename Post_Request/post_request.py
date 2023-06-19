import json

import requests

url = "https://reqres.in/api/login"

data = {
    "email": "eve.holt@reqres.in",
    "password": "cityslicka"
}
headers = {
    "Content-Type": "application/json",
    "Authorization": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9"
                     ".eyJ1c2VyTmFtZSI6IkFydW5yb3NobiIsInBhc3N3b3JkIjoiQXRtZWNzQDEyMyIsImlhdCI6MTY3OTkzODA1OX0"
                     ".90tpkcL87AzWnjaF5IfS7FXCX08ePEp553bFeJaE5T0"
}
json_data = json.dumps(data)
response = requests.post(url, data=json_data, headers=headers)
print(response.status_code)
print(response.content)
