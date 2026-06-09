"""
Health check router
"""
from fastapi import APIRouter
from app.schemas import HealthCheck
from app.core.config import get_settings

router = APIRouter(tags=["health"])
settings = get_settings()


@router.get("/health", response_model=HealthCheck)
async def health_check():
    """Health check endpoint"""
    return HealthCheck(
        status="healthy",
        service=settings.APP_NAME,
        version=settings.APP_VERSION
    )


@router.get("/ping")
async def ping():
    """Ping endpoint"""
    return {"message": "pong"}
