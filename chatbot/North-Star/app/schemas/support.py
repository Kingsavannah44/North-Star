from pydantic import BaseModel, field_validator


class SupportQueryRequest(BaseModel):
    message: str

    @field_validator("message")
    @classmethod
    def message_must_not_be_empty(cls, v: str) -> str:
        if not v or not v.strip():
            raise ValueError("Message cannot be empty.")
        return v.strip()


class SupportQueryData(BaseModel):
    category: str
    answer: str
    deflected: bool


class SupportQueryResponse(BaseModel):
    success: bool = True
    data: SupportQueryData


class ErrorDetail(BaseModel):
    code: str
    message: str


class ErrorResponse(BaseModel):
    success: bool = False
    error: ErrorDetail
