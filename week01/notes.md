
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
                                SDET + AI: Week-by-Week Checklist
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

Week 1
    LLM fundamentals, free setup, first API calls, non-determinism
    Local lab repo with first scripts

Week 2
    Structured output, prompting, first Pytest suite for an LLM
    Pytest + JSON schema suite

Week 3
    AI-assisted testing I: test generation, test data, Playwright MCP
    AI-generated API and UI tests

Week 4
    AI-assisted testing II: failure triage, self-healing locators
    AI failure summarizer in Pytest + Allure

Week 5
    LLM evaluation concepts: quality dimensions, golden datasets, metamorphic tests
    Golden dataset + first metrics

Week 6
    DeepEval deep dive
    15+ DeepEval tests

Week 7
    LLM-as-judge and Promptfoo
    Judge-based tests + Promptfoo config

Week 8
    Ragas, tracing (Langfuse), CI
    Chatbot with 30+ evals running in CI

Week 9
    RAG build and RAG testing
    RAG app with retrieval and faithfulness metrics

Week 10
    Agents and MCP testing
    LangGraph agent with trajectory tests

Week 11
    Safety and red teaming (OWASP LLM Top 10, Garak, PyRIT)
    Red-team report on your own app

Week 12
    Portfolio, resume, interview prep
    3 polished GitHub projects, updated resume



>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


Week 1: LLM Fundamentals, Free Setup and Non-Determinism

Goal: understand how an LLM actually produces output, set up free models, call them from Python, and see non-determinism with your own eyes. Everything later builds on this.
Done when: you can explain tokens, context window, temperature and non-determinism without notes, you have Ollama running, and your repo has the practice scripts below.

>>  Topics to cover
    • How LLMs work at a high level: tokens, embeddings, transformer, next-token prediction.
    • Training vs fine-tuning vs inference. Pre-training, instruction tuning, RLHF (idea only).
    • Context window, token limits, cost and latency.
    • Generation parameters: temperature, top_p, top_k, max_tokens, stop sequences, seed.
    • System prompt vs user prompt vs assistant messages.
    • Why output is non-deterministic and why that breaks classic exact-match assertions.
    • Hallucination: what it is and why it happens.
    • Local vs hosted models. Open vs closed models.
    • The three tracks of AI testing (AI-assisted, testing AI, AI-driven automation).


>>  Resources to use (all free)

    Search each title to confirm it is still available, since courses move.
    • Andrej Karpathy, "Intro to Large Language Models" (about 1 hour). Watch fully, take notes.
    • 3Blue1Brown, "Large Language Models explained briefly" and the transformer chapters of his neural network series.
    • Hugging Face LLM Course, chapter 1 (Transformer models).
    • Microsoft "Generative AI for Beginners" on GitHub: lessons on LLM basics and prompt engineering.
    • Ollama documentation and model library (install, ollama run, REST API).
    • Google AI Studio quickstart (free Gemini API key) for a hosted comparison.
    • Groq or OpenRouter free tier as a second hosted option.

    YouTube channels for this week
    • Andrej Karpathy (concepts).
    • 3Blue1Brown (visual intuition).
    • freeCodeCamp (long hands-on courses on LLM APIs and Python).
    • Krish Naik and CampusX (practical, Hindi/English).

    Readable docs and PDFs
    • Google's Prompt Engineering whitepaper (PDF).
    • Ollama API docs (/api/generate and /api/chat).
    • The "prompting" guide of any one provider (OpenAI, Anthropic or Google), read once end to end.
    • OWASP GenAI Security Project home page (skim only, we return in Week 11).


>>  Day-by-day checklist

    Day 1 - Setup (1.5 hrs)
    • ☐ Install Ollama and pull one small model (for example a 3B–8B Llama, Qwen or Mistral variant that fits your RAM).
    • ☐ Run it in the terminal with ollama run and chat for 10 minutes.
    • ☐ Create a GitHub repo named llm-testing-lab with folders week01 to week12.
    • ☐ Create a Python virtual environment and install requests, pytest, python-dotenv.
    • ☐ Get a free Google AI Studio API key and store it in .env (add .env to .gitignore).

    Day 2 - Concepts (2 hrs)
    • ☐ Watch Karpathy's "Intro to LLMs".
    • ☐ Write a one-page note: tokens, context window, temperature, hallucination, in your own words.

    Day 3 - First API calls (2 hrs)
    • ☐ Call Ollama from Python using requests (/api/chat, stream=false).
    • ☐ Call the Gemini API once from Python.
    • ☐ Print the full raw JSON response and identify where the text, token counts and timings are.

    Day 4 - Parameters (2 hrs)
    • ☐ Run the same prompt at temperature 0, 0.5 and 1.0, ten times each. Save all outputs to a CSV.
    • ☐ Try a fixed seed in Ollama and note whether outputs repeat.
    • ☐ Change max_tokens (num_predict in Ollama) and observe truncation.

    Day 5 - Prompt roles (1.5 hrs)
    • ☐ Write three different system prompts for the same user question and compare behaviour.
    • ☐ Try one prompt that tries to override the system prompt and note what happens.

    Day 6 - First tests (2 hrs)
    • ☐ Write a Pytest file test_week01.py with the practice tests below.
    • ☐ Run it five times and record which tests are flaky.

    Day 7 - Review and push (1 hr)
    • ☐ Write a README for week01 with what you learned and sample outputs.
    • ☐ Answer the interview questions below aloud without looking.
    • ☐ Push to GitHub and message me "Week 1 done".


>>  Practice tasks

    1. Hello LLM: a Python function ask(prompt, model, temperature) that returns text from Ollama.
    2. Variability experiment: run one prompt 10 times at temperature 0 and 1.0, then compute how many unique answers you got at each setting.
    3. Token awareness: read the token counts from the response and print prompt vs completion tokens for three prompts of different length.
    4. Weak assertions: write Pytest tests that check properties instead of exact text: the answer is non-empty, contains an expected keyword, stays under N characters, and does not contain a banned word.
    5. Hallucination probe: ask the model five questions whose answers do not exist (a fake library, a fake person). Record which ones it answered confidently.
    6. Compare models: run the same five prompts on your local model and Gemini, and write three lines on the differences.
    Stretch (optional): call the same model through Groq or OpenRouter and compare latency.


>>  Week 1 completion checklist
    • ☐ Ollama works locally.
    • ☐ One hosted free API works from Python.
    • ☐ Variability experiment CSV exists.
    • ☐ At least five Pytest tests run, and you know why some are flaky.
    • ☐ Notes and README pushed to GitHub.
    • ☐ You can answer 80% of the questions below.







Week 1 Interview Questions and Answers (55)

>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
A. LLM basics (1-12)

1. What is an LLM? 
A large neural network, usually a transformer, trained on huge amounts of text to predict the next token. Chat behaviour comes from further instruction tuning.

2. What is a token? 
A chunk of text (word, part of a word or symbol) that the model reads and writes. Limits and cost are counted in tokens, not words.

3. What is a context window? 
The maximum number of tokens (prompt plus output) the model can consider in one call. Anything beyond it is cut off or ignored.

4. What is an embedding? 
A numeric vector representing the meaning of text, so similar meanings sit close together. Used in search and RAG.

5. What is the transformer architecture, in one line? 
A model that uses attention to weigh how relevant each token is to every other token, instead of reading strictly in sequence.

6. Pre-training vs fine-tuning? 
Pre-training learns general language from massive data. Fine-tuning adapts the model on a smaller, task-specific dataset.

7. What is RLHF? 
Reinforcement learning from human feedback: humans rank outputs, and the model is tuned to prefer the preferred style, improving helpfulness and safety.

8. What is inference? 
Using a trained model to generate output. It is what happens each time you call the API.

9. Open-weight vs closed model? 
Open-weight models can be downloaded and run locally (Llama, Qwen, Mistral). Closed models are only reachable through a provider's API.

10. Why run a model locally? 
Privacy, no per-call cost, no rate limits, and repeatable test environments. The trade-off is hardware limits and usually lower quality.

11. What is the difference between an LLM and a chatbot? 
The LLM is the model. A chatbot is an application around it: prompts, memory, tools, UI and guardrails.

12. What is GenAI vs agentic AI? 
GenAI produces content from a prompt. Agentic AI uses an LLM to plan, call tools and take multiple steps toward a goal.

>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
B. Parameters and prompts (13-26)

13. What does temperature do? 
It controls randomness in token selection. Low values give focused, repeatable output. High values give more varied output.

14. What is top_p? 
Nucleus sampling: the model samples only from the smallest set of tokens whose probabilities add up to p.

15. What is top_k? 
The model samples only from the k most likely next tokens.

16. What does max_tokens do?
Caps the length of the generated output. Too low truncates answers mid-sentence, which is a common test failure.

17. What are stop sequences? 
Strings that make generation stop when produced. Useful for controlling format.

18. What is a seed parameter? 
A value that tries to make sampling reproducible. It helps but does not guarantee identical output across hardware or versions.

19. System vs user vs assistant message? 
System sets behaviour and rules, user is the person's input, assistant is the model's earlier replies kept as history.

20. Zero-shot vs few-shot prompting? 
Zero-shot gives only the instruction. Few-shot adds examples of desired input and output inside the prompt.

21. What is chain-of-thought prompting? 
Asking the model to reason step by step, which often improves accuracy on multi-step problems.

22. What is prompt injection, briefly? 
Input that tries to override the developer's instructions. We study it properly in Week 11.

23. Why is the same prompt giving different answers at temperature 0? 
GPU floating-point effects, batching, model updates and tie-breaking can still change results. Temperature 0 reduces 
variation but does not guarantee identical output.

24. How do you get structured output from an LLM? 
Ask for JSON in the prompt, use the provider's JSON or schema mode, then validate the result against a schema.

25. What is a prompt template? 
A reusable prompt with placeholders filled at runtime. Treat templates as code and version them.

26. Why should prompts be version-controlled? 
A small wording change can change behaviour. You need history and tests to catch regressions.

>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
C. Non-determinism and quality (27-40)

27. Why is LLM output non-deterministic? 
Tokens are sampled from a probability distribution, and infrastructure adds small numeric differences. The same input can produce different valid 
outputs.

28. Why do exact-match assertions fail for LLM tests? 
There are many correct phrasings of one answer. Exact match marks correct but differently worded answers as failures.

29. What do you assert instead? 
Properties: contains key facts, matches a schema, within length limits, no banned content, similarity above a threshold, or a judged score above a threshold.

30. What is a flaky LLM test and how do you reduce flakiness? 
A test that passes and fails on identical code. Lower temperature, fix seed, loosen assertions to properties, run multiple 
samples, and use pass-rate thresholds.

31. What is a pass-rate threshold? 
Running a case N times and requiring, for example, at least 90% passes instead of requiring 100% on a single run.

32. What is hallucination? 
The model states something false or unsupported with confidence.

33. Why do LLMs hallucinate? 
They generate likely text, not verified facts. Gaps in training data and pressure to answer both contribute.

34. How can you reduce hallucination? 
Ground answers in retrieved documents (RAG), instruct the model to say it does not know, lower temperature, and verify outputs.

35. What is faithfulness? 
Whether the answer is supported by the provided context, with no invented content.

36. What is relevance? 
Whether the answer actually addresses the user's question.

37. What is robustness in LLM testing? 
Whether behaviour stays correct under typos, rephrasing, odd formatting or adversarial input.

38. What is consistency? 
Whether similar inputs, or repeated runs, produce answers that agree with each other.

39. What is bias in LLM output? 
Systematically unfair or stereotyped behaviour toward groups, often inherited from training data.

40. What is toxicity? 
Harmful, hateful or abusive content in output, which safety tests should screen for.

>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
D. Testing perspective (41-55)

41. How is testing an LLM app different from testing a normal API? 
Outputs are probabilistic and open-ended, so you test quality ranges and properties with metrics rather than a single expected value.

42. What are the three tracks of AI testing? 
AI-assisted testing, testing AI systems, and AI-driven test automation.

43. What would you check in a raw LLM API response? 
Status code, schema, latency, token usage, finish reason (stop vs length), and the content itself.

44. What does a finish reason of "length" tell you? 
The output was cut off by the token limit, so the answer may be incomplete.

45. How would you test token or cost limits? 
Send inputs near the context limit, assert graceful handling, and track token usage per call.

46. How would you test latency for an LLM endpoint? 
Measure time to first token and total time over many runs, and assert on percentiles rather than a single value.

47. How do you handle rate limits in tests? 
Retries with backoff, small test batches, caching responses for non-eval tests, and a local model for heavy runs.

48. Why use a local model for part of your test suite? 
No cost, no rate limits, controllable version, and it keeps data private.

49. How would you mock an LLM in unit tests? 
Replace the client with a stub returning fixed responses, so you test your own code, not the model.

50. When should you not mock the LLM? 
When you are evaluating the model or prompt quality itself, since a mock cannot reveal real behaviour.

51. How would you log LLM tests for debugging? 
Store prompt, parameters, model version, raw response, latency and token counts for every call.

52. What should be pinned for reproducible LLM tests? 
Model name and version, prompt version, parameters, seed, and dataset version.

53. Why can an LLM test suite start failing without any code change? 
The provider updated the model, or a free-tier model changed behind the same name. This is model drift.

54. What is a golden dataset? 
A curated set of inputs with expected outputs or criteria, used to measure quality over time. We build one in Week 5.

55. A stakeholder asks: "Is the chatbot 100% accurate?" What do you say? 
No LLM system is 100% accurate. I would report measured quality: pass rates and scores on a defined dataset, known failure categories, and agreed thresholds.






>>  Virtual Env: 
python -m venv .venv
.venv\Scripts\activate.bat







