#this is the test case for POST 

import requests
import uuid

BASE_URL = "http://127.0.0.1:5000"

def test_create_user_valid():
    unique_email = f"duplicate_{uuid.uuid4()}@example.com"
    payload = {"name":"Test QA",
               "email":unique_email}

    response = requests.post(f"{BASE_URL}/users", json=payload)

    assert response.status_code in [200, 201]

    data = response.json()
    print(data)

    assert data['name']== payload['name']
    assert data['email']== payload['email']


def test_create_user_missing_name():
    payload = {"email":"missigname@example.com"}

    response = requests.post(f"{BASE_URL}/users", json=payload)

    assert response.status_code == 400 or response.status_code == 422


def test_create_user_missing_email():

    payload = {"name": "missingemail"}

    response = requests.post(f"{BASE_URL}/users", json=payload)

    assert response.status_code == 400 or response.status_code == 422



def test_create_empty_payload():
    payload = {}

    response = requests.post(f"{BASE_URL}/users", json=payload)

    assert response.status_code == 400 or response.status_code == 422


def test_create_invalid_content_type():

    response = requests.post(f"{BASE_URL}/users", data=" no payload")

    assert response.status_code == 415


def test_create_duplicate_user():
    unique_email = f"duplicate_{uuid.uuid4()}@example.com"
    payload = {"name":"Duplicate QA",
               "email":unique_email}

    response1 = requests.post(f"{BASE_URL}/users", json=payload)

    assert response1.status_code in [200, 201]

    response2=requests.post(f"{BASE_URL}/users", json=payload)
    assert response2.status_code in [400, 409]




