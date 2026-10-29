import csv
import time
from llm_client import chat_raw

PROMPT = "Write a one-sentence tagline for a coffee shop."
TEMPS = [0, 0.5, 1.0]
RUNS = 10

rows = []
for temp in TEMPS:
    for run in range(1, RUNS + 1):
        start = time.perf_counter()
        data = chat_raw(PROMPT, temperature=temp)
        secs = round(time.perf_counter() - start, 2)
        rows.append({
            "temperature": temp,
            "run": run,
            "answer": data["message"]["content"].strip(),
            "output_tokens": data.get("eval_count"),
            "done_reason": data.get("done_reason"),
            "seconds": secs,
        })
        print(temp, run, rows[-1]["answer"][:70])

with open("temperature_results.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=rows[0].keys())
    writer.writeheader()
    writer.writerows(rows)

print("\nUnique answers per temperature:")
for temp in TEMPS:
    answers = [r["answer"].lower() for r in rows if r["temperature"] == temp]
    print(f"  temperature {temp}: {len(set(answers))} unique out of {len(answers)}")