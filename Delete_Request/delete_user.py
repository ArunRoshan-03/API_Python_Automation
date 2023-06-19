import requests

url = r"https://reqres.in/api/users/2"

delete_response = requests.delete(url)
print(delete_response.content)
assert delete_response.status_code == 204

get_response = requests.get(url)
print(get_response.content)
assert get_response.status_code == 200

