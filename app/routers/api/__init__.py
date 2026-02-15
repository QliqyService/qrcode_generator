from app.routers.api.base import Router
from app.routers.api.healthcheck.router import router as health_router
from app.routers.api.qrcode.router import router as qrcode_router


__all__ = ["api_router"]

api_router = Router(prefix="/api/v1")

api_router.include_router(health_router, prefix="/health")
api_router.include_router(qrcode_router, prefix="/qrcode")
