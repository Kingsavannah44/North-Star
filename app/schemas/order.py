from pydantic import BaseModel
from typing import Optional
from datetime import date


class OrderResponse(BaseModel):
    order_number: str
    status: str
    tracking_number: Optional[str] = None
    estimated_delivery: Optional[date] = None

    model_config = {"from_attributes": True}


class SuccessResponse(BaseModel):
    success: bool = True
    data: OrderResponse


class ErrorDetail(BaseModel):
    code: str
    message: str


class ErrorResponse(BaseModel):
    success: bool = False
    error: ErrorDetail
