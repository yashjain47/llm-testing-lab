from llm_client import chat_raw

PROMPT = "Explain what a token is in the context of large language models."

for limit in [10, 50, 300, 1000]:
    data = chat_raw(PROMPT, temperature=0, num_predict=limit)
    print(f"--- num_predict={limit}")
    print("done_reason:", data["done_reason"], "| eval_count:", data["eval_count"])
    print(data["message"]["content"])