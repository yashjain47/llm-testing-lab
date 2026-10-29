from llm_client import chat_messages

# Call 1: no history
print("Without history:")
print(chat_messages([{"role": "user", "content": "What is my name?"}], temperature=0))

# Call 2: history included
history = [
    {"role": "user", "content": "My name is Yash."},
    {"role": "assistant", "content": "Nice to meet you, Yash."},
    {"role": "user", "content": "What is my name?"},
]
print("\nWith history:")
print(chat_messages(history, temperature=0))