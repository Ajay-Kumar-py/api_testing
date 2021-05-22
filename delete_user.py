import requests

resp= requests.delete("https://reqres.in/api/users/2")

assert resp.status_code==204