import requests

print("Starting test...")

url = "http://127.0.0.1:5000/predict"

data = {
    "Age": 30,
    "Gender": "Male",
    "LastLogin": 7,
    "HeavyUser": True,
    "LoginBucket": "15-30"
}

response = requests.post(url, json=data)

print("Response received!")
print("Response content:", response.text)
