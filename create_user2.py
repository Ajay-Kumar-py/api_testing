import requests
import json

mydata=open('data.json','r').read()

resp = requests.post("https://reqres.in/api/users",data=json.loads(mydata))
print(resp)
print(resp.json())
assert resp.json()['job'] == 'engineer'