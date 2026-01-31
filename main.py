from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel
import os, csv, io
from datetime import datetime

app = FastAPI(title="Activation API")

class CardResult(BaseModel):
    brand: str
    card_number: str
    status: str
    balance: float | None = None

@app.get("/")
def root():
    return {"status": "ok"}

@app.post("/submit-result")
def submit_result(result: CardResult):
    return {"saved": True, "data": result}

# -------------------------
# CSV upload
# -------------------------
@app.post("/upload-cards")
async def upload_cards(file: UploadFile = File(...)):
    contents = await file.read()
    decoded = contents.decode("utf-8")
    reader = csv.reader(io.StringIO(decoded))

    cards = []
    for row in reader:
        if len(row) >= 2:
            cards.append({
                "brand": row[0],
                "card_number": row[1]
            })

    return {
        "count": len(cards),
        "cards": cards,
        "timestamp": datetime.utcnow().isoformat()
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 8000)),
    )
