from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from loguru import logger as LOGGER

from app.routers import api_router, streaming_router
from app.settings import get_settings


class Application(FastAPI):
    """Setting up and preparing the launch of the QR-code service"""

    def __init__(self):
        self.settings = get_settings()
        self.logger = self.settings.configure_logging()

        super().__init__(
            title=self.settings.APP_TITLE,
            description=self.settings.APP_DESCRIPTION,
            root_path=self.settings.APP_PUBLIC_PATH,
            root_path_in_servers=True,
            docs_url="/api",
            openapi_url="/api/openapi.json",
            redoc_url="/api/v1/docs",
            version=self.settings.APP_RELEASE,
        )
        self.run_startup_actions()

    def run_startup_actions(self) -> None:
        self.add_middlewares()
        self.include_routers()

    def include_routers(self) -> None:
        self.include_router(api_router)
        self.include_router(streaming_router)
        LOGGER.debug("[MAIN] Routers added")

    def add_middlewares(self) -> None:
        self.add_middleware(
            CORSMiddleware,
            allow_origins=["*"],
            allow_methods=["*"],
            allow_headers=["*"],
        )
        LOGGER.debug("[MAIN] Middlewares added")


app = Application()
