from agents.planner import plan_task
from agents.executor import execute_plan

task = "Find top python repositories on GitHub and weather in Pune"

plan = plan_task(task)
results = execute_plan(plan)

print(results)
