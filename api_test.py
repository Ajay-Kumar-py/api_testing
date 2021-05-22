import pytest
import requests

resp= requests.get("https://reqres.in/api/users?page=2")
code = resp.status_code
assert code == 200, "code doesn't match"

json_resp = resp.json()
print(json_resp)

@pytest.mark.one
def test_json_resp():
    assert json_resp['total']==12
@pytest.mark.two
def test_json_resp_1():
    assert json_resp['total_pages'] == 2, "mismatch ib total pges"
