import base64

from faststream.rabbit import RabbitQueue, RabbitRouter
from loguru import logger as LOGGER

from app.schemas.qrcode import QRRPCRequest, QRRPCResponse
from app.services import QRCodeService
from app.settings import SETTINGS


qrprefix = f"{SETTINGS.APP_STAND}::{SETTINGS.APP_NAME}::"
router = RabbitRouter(prefix=qrprefix)


@router.subscriber(queue=RabbitQueue(name="get_qrcode"))
async def get_qrcode(payload: QRRPCRequest) -> QRRPCResponse:
    """
    Сгенерировать QR-код для переданного URL и вернуть его через RPC.

    Args:
        payload (QRRPCRequest): Данные RPC-запроса, содержащие:
            - id (UUID): Уникальный идентификатор запроса
            - url (str): Абсолютный URL

    Returns:
        QRRPCResponse: RPC-ответ, содержащий:
            - id (UUID): `payload.id`.
            - body (str): Base64-кодированное содержимое PNG-файла

    """
    LOGGER.debug(f"Принял запрос #{payload.id}")
    buf = QRCodeService.generate(value=payload.url)
    png_bytes = buf.getvalue()
    body_b64 = base64.b64encode(png_bytes).decode("ascii")
    return QRRPCResponse(id=payload.id, body=body_b64)
