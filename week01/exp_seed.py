from llm_client import chat_raw

PROMPT = "Write a one-sentence tagline for a coffee shop."

def run(label, **options):
    answers = [chat_raw(PROMPT, **options)["message"]["content"].strip() for _ in range(5)]
    print(f"{label}: {len(set(answers))} unique out of 5")
    for a in answers:
        print("   ", a[:80])

run("temp 0.8, no seed", temperature=0.8)
run("temp 0.8, seed 42", temperature=0.8, seed=42)