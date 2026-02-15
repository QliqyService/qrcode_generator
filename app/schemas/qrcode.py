from uuid import UUID

from pydantic import BaseModel


class QRRequest(BaseModel):
    data: str


class QRRPCRequest(BaseModel):
    id: UUID
    url: str


class QRRPCResponse(BaseModel):
    id: UUID
    body: str
