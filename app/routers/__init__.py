from app.routers.api import api_router
from app.routers.streaming import streaming_router
from app.routers.shared import router as shared_router


__all__ = ["api_router", "streaming_router", "shared_router"]
