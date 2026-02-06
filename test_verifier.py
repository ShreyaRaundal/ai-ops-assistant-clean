from agents.planner import plan_task
from agents.executor import execute_plan
from agents.verifier import verify_and_format

task = "Find top python repositories on GitHub and weather in Pune"

plan = plan_task(task)
raw_data = execute_plan(plan)
final_output = verify_and_format(task, raw_data)

print(final_output)
