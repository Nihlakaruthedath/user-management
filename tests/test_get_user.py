# this is the test case for GET

import requests

BASE_URL = 'http://127.0.0.1:5000'

def test_get_all_users():
    response = requests.get(f"{BASE_URL}/users")
    assert response.status_code == 200

    data = response.json()
    assert isinstance(data, list)
    assert len(data) >= 1  # Optional: checks that list is not empty


def test_get_user_by_id():
    response = requests.get(f"{BASE_URL}/users/1")
    assert response.status_code == 200
    data = response.json()

    # Validate required keys
    assert "id" in data
    assert "name" in data
    assert "email" in data



def test_get_user_not_found():
    response = requests.get(f'{BASE_URL}/users/10000')
    assert response.status_code == 404
    data = response.json()

    assert "error" in data
    assert data["error"] == 'user not found'