import json
import os
import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.environ["GEMINI_API_KEY"]
MODEL = os.environ.get("GEMINI_MODEL", "gemini-2.5-flash")

URL = f"https://generativelanguage.googleapis.com/v1beta/models/{MODEL}:generateContent"

payload = {
    "contents": [
        {"parts": [{"text": "What is the capital of India? Answer in one sentence."}]}
    ]
}

response = requests.post(
    URL,
    headers={"x-goog-api-key": API_KEY, "Content-Type": "application/json"},
    json=payload,
    timeout=60,
)
print("HTTP status:", response.status_code)
print(json.dumps(response.json(), indent=2))






def get_models():
    
    try:
            
        r = requests.get(
            "https://generativelanguage.googleapis.com/v1beta/models",
            headers={"x-goog-api-key": os.environ["GEMINI_API_KEY"]},
            timeout=30,
        )
        print("HTTP status:", r.status_code)
        if r.ok:
            for m in r.json().get("models", []):
                if "generateContent" in m.get("supportedGenerationMethods", []):
                    print(m["name"])
        else:
            print(r.text)
            
        return True
            
    except Exception as Error:
        print(f"Error : {Error}")
        return False
    
    


