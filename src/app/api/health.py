from fastapi import APIRouter
from src.app.schemas.health import HealthResponse
from src.app.core.config import settings

router = APIRouter()

@router.get(
    "/health",
    response_model = HealthResponse,
    tags = ["health"]
)

def health_check() -> HealthResponse:
    return HealthResponse(
        status = "ok",
        service = settings.APP_NAME,
        version = settings.VERSION,
    )
