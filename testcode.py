import requests

res = requests.post("http://127.0.0.1:5000/chat", json={
    "prompt": "Write a Python function to check if a number is prime.",
    "mode": "code"
})

print("Status Code:", res.status_code)
print("Response:", res.json())
