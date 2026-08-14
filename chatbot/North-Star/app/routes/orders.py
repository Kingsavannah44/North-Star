from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.services.order_service import get_order_by_number
from app.schemas.order import SuccessResponse, OrderResponse

router = APIRouter(prefix="/api/orders", tags=["Orders"])


@router.get(
    "/{order_number}",
    response_model=SuccessResponse,
    summary="Get order status",
    description=(
        "Look up an order by its order number (e.g. NS1001). "
        "Returns the current status, tracking number, and estimated delivery date."
    ),
)
def get_order(order_number: str, db: Session = Depends(get_db)):
    order = get_order_by_number(db, order_number.upper())
    return {
        "success": True,
        "data": OrderResponse.model_validate(order),
    }
