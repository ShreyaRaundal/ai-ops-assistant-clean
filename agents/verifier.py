import json
from llm.llm_client import call_llm


def verify_and_format(task: str, data: dict) -> dict:
    """
    Verifies executor output and formats final response.
    """

    system_prompt = """
You are a Verifier Agent.

Your job:
- Check if the data is complete
- Ensure the response matches the user task
- Return a clean, well-structured JSON response
- Do NOT add extra explanations
"""

    user_prompt = f"""
User task:
{task}

Data collected:
{json.dumps(data, indent=2)}
"""

    response = call_llm(system_prompt, user_prompt)

    try:
        return json.loads(response)
    except Exception:
        return {
            "task": task,
            "result": data
        }
