import requests
import json

response = requests.post(
    "http://192.168.56.1:1234/v1/chat/completions",
    json={
        "model": "meta-llama-3.1-8b-instruct",
        "messages": [{"role": "user", "content": "Say hello in one sentence"}]
    }
)

print(response.status_code)
print(response.json())