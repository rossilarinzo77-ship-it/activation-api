
from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime
import requests
import re

app = FastAPI()

class CheckRequest(BaseModel):
    brand: str
    card_id: str
    card_number: str | None = None
    pin: str | None = None

def extract_balance(text: str):
    match = re.search(r"\$\s*[\d,]+\.\d{2}", text)
    if match:
        return float(match.group(0).replace("$", "").replace(",", ""))
    return None

@app.post("/activation/check")
def check_activation(req: CheckRequest):
    status = "PENDING"

    # Only do real check if PIN is provided
    if req.card_number and req.pin:
        try:
            r = requests.get(
                "https://www.kohls.com/guestservices/gift-cards",
                timeout=20
            )

            balance = extract_balance(r.text)

            if balance is None:
                status = "UNKNOWN"
            elif balance > 0:
                status = "ACTIVE"
            else:
                status = "INACTIVE"

        except Exception:
            status = "UNKNOWN"

    return {
        "brand": req.brand,
        "card_id": req.card_id,
        "status": status,
        "checked_at": datetime.utcnow().isoformat()
    }
