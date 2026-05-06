from fastapi import FastAPI

app = FastAPI()

@app.post("/support/workflow")
def support_workflow(ticket: str):
    return {"status": "processed", "ticket": ticket}
