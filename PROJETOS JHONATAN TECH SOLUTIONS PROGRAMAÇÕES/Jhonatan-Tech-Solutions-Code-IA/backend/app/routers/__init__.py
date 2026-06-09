"""
Routers package initialization
"""
from app.routers.health import router as health_router
from app.routers.code import router as code_router

__all__ = ["health_router", "code_router"]
