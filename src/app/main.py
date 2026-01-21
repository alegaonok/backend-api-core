from fastapi import FastAPI
from src.app.api.health import router as health_router

app = FastAPI(title = "Backend API Core")

app.include_router(health_router)

