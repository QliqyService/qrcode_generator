from enum import StrEnum
from functools import lru_cache
from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict

from app.logger import CustomLogger


class AppStand(StrEnum):
    DEV = "dev"
    PROD = "prod"
    LOCAL = "local"


class ServiceName(StrEnum):
    QRCODE = "qrcode_generator"


class _Settings(BaseSettings):
    """QR-code service settings"""

    ROOT_DIR: Path = Path(__file__).parent.parent
    APP_DIR: Path = ROOT_DIR / "app"

    APP_TITLE: str = "Qliqy | QR Code Generator"
    APP_DESCRIPTION: str = """
# QR Code Generator API
This service generates QR-codes from provided text.
"""
    APP_PUBLIC_PATH: str | None = None
    APP_RELEASE: str = "0.1.0"
    APP_STAND: AppStand = AppStand.LOCAL
    APP_NAME: ServiceName = ServiceName.QRCODE
    RABBITMQ_HOST: str
    RABBITMQ_PORT: int
    RABBITMQ_USER: str
    RABBITMQ_PASSWORD: str

    @property
    def RABBITMQ_URL(self):
        return f"amqp://{self.RABBITMQ_USER}:{self.RABBITMQ_PASSWORD}@{self.RABBITMQ_HOST}:{self.RABBITMQ_PORT}?name={self.APP_NAME}"

    @staticmethod
    def configure_logging():
        return CustomLogger.make_logger()

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


@lru_cache
def get_settings(env_file: str = ".env") -> _Settings:
    return _Settings(_env_file=env_file)


SETTINGS = get_settings()
