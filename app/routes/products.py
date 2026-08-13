from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from typing import Optional
from app.database import get_db
from app.services.inventory_service import check_availability
from app.schemas.product import SuccessResponse

router = APIRouter(prefix="/api/products", tags=["Products"])


@router.get(
    "/{product_id}/availability",
    response_model=SuccessResponse,
    summary="Check product availability",
    description=(
        "Check whether a product is in stock. "
        "Pass an optional ?size= query parameter to check a specific size. "
        "Returns available (bool) and quantity."
    ),
)
def get_availability(
    product_id: int,
    size: Optional[str] = Query(default=None, description="Product size, e.g. 42 or M"),
    db: Session = Depends(get_db),
):
    data = check_availability(db, product_id, size)
    return {"success": True, "data": data}
