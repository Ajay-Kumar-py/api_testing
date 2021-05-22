

import requests

payload = {
    "name": "new_api",
    "job": "new_test"
}
resp = requests.patch("https://reqres.in/api/users/2",data=payload)
print(resp)
print(resp.json())
assert resp.json()['job'] == 'new_test'