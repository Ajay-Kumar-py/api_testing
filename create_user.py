
import requests

payload = {
    "name": "mukesh",
    "job": "engineer"
}
resp = requests.post("https://reqres.in/api/users",data=payload)
print(resp)
print(resp.json())
assert resp.json()['job'] == 'engineer'