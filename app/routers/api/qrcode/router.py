from fastapi.responses import StreamingResponse

from app.routers.api import Router
from app.schemas.qrcode import QRRequest
from app.services.qrcode_service import QRCodeService


router = Router(
    name="QR Codes",
    description="Endpoints for generating QR codes",
)


@router.post("/generate")
def generate_qrcode(payload: QRRequest):
    """
     Сгенерировать QR-код в формате PNG.
    Args:
        payload (QRRequest): Тело HTTP-запроса, содержащее:
            - data (str)

    Returns:
        StreamingResponse: Потоковый HTTP-ответ с изображением
        QR-кода в формате PNG.
    """
    buf = QRCodeService.generate(payload.data)
    return StreamingResponse(buf, media_type="image/png")
