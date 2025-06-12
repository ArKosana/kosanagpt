import requests

res = requests.post("http://127.0.0.1:5000/chat", json={"prompt": "Hello, how are you?"})
print(res.status_code)
print(res.json())
