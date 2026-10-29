import json
import requests


url = "http://localhost:11434/api/chat"

payload = {
    "model" : "qwen3.5:4b",
    "messages" : [
        {"role": "user", "content" : "what is the capital of India? answer in one sentence."}
        ],
    "stream": False,
    "think": False 
}

response = requests.post(url, json=payload, timeout=300)
print(f"HTTP Status Code : {response.status_code}")

print(json.dumps(response.json(), indent=2))