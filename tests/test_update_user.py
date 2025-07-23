import requests
import uuid

BASE_URL = 'http://127.0.0.1:5000'

def test_update_user_valid():
    #create new user 
    unique_email = f"test_{uuid.uuid4()}@example.com"
    payload= {"name": "testingput", "email":unique_email}
    response= requests.post(f"{BASE_URL}/users", json = payload)
    assert response.status_code in [200, 201]
    data= response.json()

    assert data["name"] == payload['name']
    assert data['email'] == payload['email']

    user_id= data["id"]

    #update the user with below payload
    update_payload= {"name":"testingupdate", "email":"testingupdate@email.com"}
    updated_response = requests.put(f"{BASE_URL}/users/{user_id}", json = update_payload)
    assert updated_response.status_code == 200
    
    data_updated= updated_response.json()
    assert data_updated["name"] == update_payload["name"]
    assert data_updated['email'] == update_payload['email']


def test_update_user_not_found():
    fake_id= 9999
    payload= {"name": "testingghostt", "email":"testingoastt@example.com"}
    response= requests.put(f"{BASE_URL}/users/{fake_id}", json=payload)
    assert response.status_code == 404 



def test_update_no_name():
    unique_email = f"test_{uuid.uuid4()}@example.com"
    payload= {"name": "testingput", "email":unique_email}
    response= requests.post(f"{BASE_URL}/users", json = payload)
    assert response.status_code in [200, 201]
    user_id = response.json()["id"]


    new_payload= {"email":unique_email}
    updated_response = requests.put(f"{BASE_URL}/users/{user_id}", json = new_payload)
    assert updated_response.status_code == 400



def test_update_no_email():
    unique_email = f"test_{uuid.uuid4()}@example.com"
    payload= {"name": "testingput", "email":unique_email}
    response= requests.post(f"{BASE_URL}/users", json = payload)
    assert response.status_code in [200, 201]
    user_id = response.json()["id"]


    new_payload= {"name":'ehihiil'}
    updated_response = requests.put(f"{BASE_URL}/users/{user_id}", json = new_payload)
    assert updated_response.status_code == 400


def test_update_no_payload():
    unique_email = f"test_{uuid.uuid4()}@example.com"
    payload= {"name": "testingput", "email":unique_email}
    response= requests.post(f"{BASE_URL}/users", json = payload)
    assert response.status_code in [200, 201]
    user_id = response.json()["id"]


    updated_response = requests.put(f"{BASE_URL}/users/{user_id}", json ={})
    assert updated_response.status_code == 400


def test_update_wrong_type():
    unique_email = f"test_{uuid.uuid4()}@example.com"
    payload= {"name": "testingput", "email":unique_email}
    response= requests.post(f"{BASE_URL}/users", json = payload)
    assert response.status_code in [200, 201]
    user_id = response.json()["id"]


    new_payload= "just_a_string"
    updated_response = requests.put(f"{BASE_URL}/users/{user_id}", json = new_payload)
    assert updated_response.status_code == 400