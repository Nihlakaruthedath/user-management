import requests

url = 'http://127.0.0.1:5000/users'  # Your Flask endpoint
payload = {
    "name": "Nila",
    "email": "nila@example.com"
}

response = requests.post(url, json=payload)

print("Status Code:", response.status_code)
print("Response JSON:", response.json())
