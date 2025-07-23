#this is the test case for DELETE 

import requests
import uuid

BASE_URL= "http://127.0.0.1:5000"

def test_delete_user_valid():
    unique_email= f'{uuid.uuid4()}@example.com'
    payload={"name": "karumanna", "email":unique_email}
    response_create=requests.post(f'{BASE_URL}/users', json=payload)
    assert response_create.status_code in [200, 201]

    id_returned = response_create.json()["id"]

    response= requests.delete(f"{BASE_URL}/users/{id_returned}")
    assert response.status_code == 200
    


def test_delete_not_valid_user():
    response= requests.delete(f"{BASE_URL}/users/99999")
    assert response.status_code == 404
    assert response.json()["error"]=="user not found"