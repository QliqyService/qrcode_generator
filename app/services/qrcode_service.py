from io import BytesIO

import qrcode


class QRCodeService:
    @staticmethod
    def generate(value: str) -> BytesIO:
        img = qrcode.make(value)

        buffer = BytesIO()
        img.save(buffer, format="PNG")
        buffer.seek(0)
        return buffer
