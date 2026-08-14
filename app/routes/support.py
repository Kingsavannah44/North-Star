from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.services.support_service import handle_support_query
from app.schemas.support import SupportQueryRequest, SupportQueryResponse

router = APIRouter(prefix="/api/support", tags=["Support"])


@router.post(
    "/query",
    response_model=SupportQueryResponse,
    summary="Submit a support question",
    description=(
        "Submit a customer support message. "
        "The backend will classify it and attempt to answer automatically. "
        "If the question cannot be answered, deflected will be false."
    ),
)
def support_query(request: SupportQueryRequest, db: Session = Depends(get_db)):
    result = handle_support_query(db, request.message)
    return {"success": True, "data": result}
