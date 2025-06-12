import requests

res = requests.post("http://127.0.0.1:5000/chat", json={
    "prompt": "Explain what a button is."
})

print("Status:", res.status_code)
print("Response:", res.json())
