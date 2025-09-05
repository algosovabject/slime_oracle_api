from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime

app = FastAPI(title="Slime Mold Oracle API")

# Request schema
class QueryRequest(BaseModel):
    query: str

# Response schema
class OracleResponse(BaseModel):
    symbols: list[str]
    interpretation: str
    mood: dict
    path: list[str]

@app.post("/oracle/query", response_model=OracleResponse)
def ask_oracle(request: QueryRequest):
    # Placeholder logic (you’ll plug in your Oracle here later)
    now = datetime.now()
    mood = {
        "time_of_day": now.strftime("%H:%M"),
        "lunar_phase": "waxing gibbous",  # just hardcoded for now
        "tone": "cryptic"
    }
    response = {
        "symbols": ["The Serpent", "The Mirror", "The Final Quiet"],
        "interpretation": "Subversion, reflection, and endings shaping beginnings.",
        "mood": mood,
        "path": ["Knowledge", "Cycles", "Transformation"]
    }
    return response
