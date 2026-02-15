from fastapi import APIRouter

from app.routers.api.qrcode.router import router as qrcode_router


api_router = APIRouter(prefix="/api/v1")
api_router.include_router(qrcode_router, prefix="/qrcode", tags=["qrcode"])
