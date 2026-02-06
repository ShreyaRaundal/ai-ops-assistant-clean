from fastapi import FastAPI
from agents.planner import plan_task
from agents.executor import execute_plan
from agents.verifier import verify_and_format

app = FastAPI(title="AI Ops Assistant")

@app.post("/run")
def run(task: str):
    plan = plan_task(task)
    data = execute_plan(plan)
    final_output = verify_and_format(task, data)
    return final_output
