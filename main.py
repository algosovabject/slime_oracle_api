from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "API is alive!"}

@app.post("/oracle/query")
def oracle_query(payload: dict):
    question = payload.get("question", "")
    return {
        "symbols": ["fungus", "veil", "stone"],
        "interpretation": f"The mold whispers in response to '{question}'."
    }
