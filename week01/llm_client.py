import requests

def ask(prompt, model="qwen3.5:4b", temperature=0.7):
    payload = {
        "model": model,
        "messages": [{"role": "user", "content": prompt}],
        "stream": False,
        "think": False,
        "options": {"temperature": temperature},
    }
    r = requests.post("http://localhost:11434/api/chat", json=payload, timeout=300)
    r.raise_for_status()
    return r.json()["message"]["content"]


    
def chat_raw(prompt, model="qwen3.5:4b", **options):
    
    payload = {
        "model": model,
        "messages": [{"role": "user", "content": prompt}],
        "stream": False,
        "think": False,
        "options": options,
    }
    r = requests.post("http://localhost:11434/api/chat", json=payload, timeout=300)
    r.raise_for_status()
    return r.json()


def chat_messages(messages, model="qwen3.5:4b", **options):
    payload = {
        "model": model,
        "messages": messages,
        "stream": False,
        "think": False,
        "options": options,
    }
    r = requests.post("http://localhost:11434/api/chat", json=payload, timeout=300)
    r.raise_for_status()
    return r.json()["message"]["content"].strip()


if __name__ == "__main__":
    print(ask("Explain what a token is in the context of large language models, in one sentence..", temperature=0))
    
    
         