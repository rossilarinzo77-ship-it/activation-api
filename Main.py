from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime

app = FastAPI()

class CheckRequest(BaseModel):
    brand: str
    card_id: str

@app.post("/activation/check")
def check_activation(data: CheckRequest):
    return {
        "card_id": data.card_id,
        "brand": data.brand,
        "status": "UNKNOWN",
        "checked_at": datetime.utcnow().isoformat()
    }
