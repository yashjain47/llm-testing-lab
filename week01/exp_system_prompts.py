from llm_client import chat_messages

QUESTION = "What is a token in the context of large language models?"

SYSTEMS = {
    "none": None,
    "eli10": "You explain things to a 10-year-old. Use one short sentence and one everyday example.",
    "strict_json": 'You are an API. Reply ONLY with JSON in the form {"answer": "<one sentence>"}. No other text.',
    "pirate": "You are a pirate. Always talk like a pirate, in one sentence.",
}

for name, system in SYSTEMS.items():
    messages = []
    if system:
        messages.append({"role": "system", "content": system})
    messages.append({"role": "user", "content": QUESTION})
    print(f"--- {name}")
    print(chat_messages(messages, temperature=0))
    print()