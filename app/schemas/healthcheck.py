from pydantic import BaseModel


class GetHealthcheckResponse(BaseModel):
    msg: str
    release: str
