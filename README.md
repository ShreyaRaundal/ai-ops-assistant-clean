AI Operations Assistant


1️⃣ Project Overview

AI Operations Assistant is a multi-agent GenAI system that accepts natural-language tasks, plans execution steps using an LLM, calls real-world APIs, and verifies results before returning a structured response.
The system runs locally and demonstrates agent-based reasoning, API orchestration, and LLM integration.

2️⃣ Architecture

The system follows a Planner–Executor–Verifier multi-agent architecture.

🔹 Planner Agent

Uses an LLM (Groq) for reasoning

Converts user input into a structured JSON execution plan

Decides:

Which tools to use

Actions to perform

Parameters required

🔹 Executor Agent

Reads the plan step-by-step

Calls real third-party APIs

Collects raw responses from each tool

🔹 Verifier Agent

Validates completeness of results

Normalizes API responses

Formats the final structured output
<img width="814" height="454" alt="image" src="https://github.com/user-attachments/assets/05edff5d-87be-43d1-ab2e-89381b8e2adb" />
<img width="942" height="459" alt="image" src="https://github.com/user-attachments/assets/227272fa-3b1d-4bf1-a0a0-74d2a2aef134" />

3️⃣ APIs Used

The project integrates real third-party APIs:

Groq LLM API – Task planning and reasoning

GitHub REST API – Repository search and metadata

OpenWeather API – Current weather data

4️⃣ Setup Instructions (Copy-Paste Safe)
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python -m uvicorn main:app --reload

5️⃣ Environment Variables

Create a .env file using .env.example.

GROQ_API_KEY=your_groq_api_key
OPENWEATHER_API_KEY=your_openweather_api_key
<img width="635" height="51" alt="image" src="https://github.com/user-attachments/assets/c851d711-5576-41a1-8a89-7fc790073b4f" />


https://console.groq.com/keys
https://home.openweathermap.org/api_keys


🔗 API Key Portals:

https://console.groq.com/keys

https://home.openweathermap.org/api_keys

6️⃣ Example Prompts (VERY IMPORTANT)

You can test the system with prompts such as:

Find top Python repositories on GitHub and weather in Pune

Get JavaScript repositories with most stars and weather in Mumbai

Show trending Python repositories and current weather in Delhi

7️⃣ How to Test

Start the server:

python -m uvicorn main:app --reload


Open Swagger UI:
http://127.0.0.1:8000/docs

Call the /run endpoint with a task query parameter.
Example UI:
http://127.0.0.1:8000/docs
![Uploading image.png…]()

<img width="1365" height="755" alt="image" src="https://github.com/user-attachments/assets/42d5fedb-5441-457c-9cf9-322c4a7def77" />
<img width="1366" height="739" alt="image" src="https://github.com/user-attachments/assets/13b39d68-3151-494f-b4ca-84c503d6c224" />

8️⃣ Limitations / Trade-offs

Sequential execution (no parallel API calls)

No caching of API responses

Limited retry logic on API failures

These trade-offs were made to keep the system simple, readable, and beginner-friendly.


<img width="1366" height="688" alt="image" src="https://github.com/user-attachments/assets/98f62ffb-72c7-401c-a0ba-2079623a556a" />

<img width="1346" height="671" alt="image" src="https://github.com/user-attachments/assets/cad3f64c-d8fe-4c24-a42c-febb3b408cc7" />

<img width="1366" height="680" alt="image" src="https://github.com/user-attachments/assets/2c5db2b0-1ed9-4d0e-876a-323a07a0a00c" />






