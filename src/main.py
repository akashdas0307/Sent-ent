import asyncio
import logging
from fastapi import FastAPI, WebSocket

# Basic logging setup
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger = logging.getLogger("sentient-core")

app = FastAPI(title="Sentient AI Framework")

@app.on_event("startup")
async def startup_event():
    logger.info("Starting up Sentient AI Framework Core...")
    # Initialization of Event Bus, Thalamus, Prajna, Brainstem, etc. will happen here.

@app.on_event("shutdown")
async def shutdown_event():
    logger.info("Shutting down Sentient AI Framework Core...")

@app.get("/health")
async def health_check():
    return {"status": "alive", "modules": "initializing"}

# Basic websocket endpoint for future GUI integration
@app.websocket("/ws/dashboard")
async def websocket_dashboard(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            # We will stream event bus updates here in the future
            data = await websocket.receive_text()
            await websocket.send_text(f"Message received: {data}")
    except Exception as e:
        logger.info(f"WebSocket connection closed: {e}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
