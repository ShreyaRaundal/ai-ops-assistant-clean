import json
from llm.llm_client import call_llm


def plan_task(user_task: str) -> dict:
    """
    Converts user natural language task
    into a structured JSON execution plan.
    """

    system_prompt = """
You are a Planner Agent.

Your job is to convert the user's task into a JSON plan.

Available tools:
1. github -> search repositories
   action: search_repos
   params: { "query": "<string>" }

2. weather -> get current weather
   action: get_weather
   params: { "city": "<string>" }

Rules:
- Output ONLY valid JSON
- No explanation
- No extra text

JSON format:
{
  "steps": [
    { "tool": "...", "action": "...", "params": {...} }
  ]
}
"""

    llm_output = call_llm(system_prompt, user_task)

    try:
        return json.loads(llm_output)
    except Exception:
        return {"steps": []}
