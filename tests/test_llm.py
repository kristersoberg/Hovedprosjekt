import requests
import json

response = requests.post(
    "http://localhost:11434/v1/chat/completions",
    json={
        "model": "llama3.1:8b",
        "messages": [{"role": "user", "content": "Say hello in one sentence"}]
    }
)

print(response.status_code)
print(response.json())