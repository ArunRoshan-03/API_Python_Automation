import json

import requests

url = "https://reqres.in/api/login"

with open("C:\\Users\\arunroshan.r\\Desktop\\data.json", 'r') as file:
    data_json = file.read()
    data = json.loads(data_json)

with open("C:\\Users\\arunroshan.r\\Desktop\\header.json", 'r') as file:
    header_str = file.read()

    headers = json.loads(header_str)

response = requests.post(url, json=data, headers=headers)
print(response.content)
