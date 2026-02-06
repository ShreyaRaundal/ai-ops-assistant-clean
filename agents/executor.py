from tools.github_tool import search_repos
from tools.weather_tool import get_weather


def execute_plan(plan: dict) -> dict:
    """
    Executes the plan produced by Planner Agent
    by calling the required tools (APIs).
    """

    results = {}

    for step in plan.get("steps", []):
        tool = step.get("tool")
        action = step.get("action")
        params = step.get("params", {})

        if tool == "github" and action == "search_repos":
            query = params.get("query")
            results["github"] = search_repos(query)

        elif tool == "weather" and action == "get_weather":
            city = params.get("city")
            results["weather"] = get_weather(city)

    return results
