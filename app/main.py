from fastapi import FastAPI

app = FastAPI()

@app.get("/system/health")
def get_health():
    return {"health": "OK"}
