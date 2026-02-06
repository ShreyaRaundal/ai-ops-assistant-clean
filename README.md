1️⃣ Project Overview
AI Operations Assistant that accepts natural language tasks, plans steps using an LLM,
executes real APIs, and verifies results using a multi-agent architecture.

2️⃣ Architecture

Mention all three agents clearly:

Planner Agent – Converts user task into structured JSON plan using LLM

Executor Agent – Executes steps and calls real APIs

Verifier Agent – Validates completeness and formats final output

⚠️ This maps directly to their evaluation rubric.

3️⃣ APIs Used

Explicit list (must-have):

Groq LLM API (for planning & reasoning)

GitHub REST API (repository search)

OpenWeather API (current weather)

4️⃣ Setup Instructions (Copy-Paste Safe)
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python -m uvicorn main:app --reload

5️⃣ Environment Variables

Show example only (no real key):

GROQ_API_KEY=your_groq_api_key
OPENWEATHER_API_KEY=your_openweather_key

6️⃣ Example Prompts (VERY IMPORTANT)

Include 3–5 prompts, for example:

Find top Python repositories on GitHub and weather in Pune

Get JavaScript repositories with most stars and weather in Mumbai

Show trending Python repos and current weather in Delhi

7️⃣ How to Test

Mention:

http://127.0.0.1:8000/docs

/run endpoint with task query param

8️⃣ Limitations / Trade-offs

Add 2–3 honest points:

Sequential execution (no parallelism)

No caching

Limited error retries

This actually increases your score.
