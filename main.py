from fastapi import FastAPI
import os

app = FastAPI(
    title="Activation API",
    description="Gift card activation test API",
    version="1.0.0"
)

# -------------------------
# Root / health endpoint
# -------------------------
@app.get("/")
def root():
    return {
        "status": "ok",
        "message": "Render app is LIVE 🚀",
        "port": os.environ.get("PORT")
    }

# -------------------------
# Ping endpoint
# -------------------------
@app.get("/ping")
def ping():
    return {"ping": "pong"}

# -------------------------
# Card check endpoint
# -------------------------
@app.get("/check-card")
def check_card(brand: str, card_number: str):
    return {
        "brand": brand,
        "card_number": card_number,
        "status": "received",
        "note": "Test endpoint – logic will be added later"
    }

# -------------------------
# Render startup entrypoint
# -------------------------
if __name__ == "__main__":
    import uvicorn

    print("🔥 APP STARTED SUCCESSFULLY 🔥")

    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 8000)),
        log_level="info"
    )
