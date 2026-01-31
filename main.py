from fastapi import FastAPI
import os

app = FastAPI()

# -------------------------
# Health / root endpoint
# -------------------------
@app.get("/")
def root():
    return {
        "status": "ok",
        "message": "Render app is LIVE 🚀",
        "port": os.environ.get("PORT")
    }

# -------------------------
# Optional test endpoint
# -------------------------
@app.get("/ping")
def ping():
    return {"ping": "pong"}

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
