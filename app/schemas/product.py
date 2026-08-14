from pydantic import BaseModel
from typing import Optional


class AvailabilityResponse(BaseModel):
    product_id: int
    product_name: str
    size: Optional[str] = None
    available: bool
    quantity: int

    model_config = {"from_attributes": True}


class SuccessResponse(BaseModel):
    success: bool = True
    data: AvailabilityResponse


class ErrorDetail(BaseModel):
    code: str
    message: str


class ErrorResponse(BaseModel):
    success: bool = False
    error: ErrorDetail
