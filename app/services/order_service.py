from sqlalchemy.orm import Session
from app.models.order import Order
from app.utils.exceptions import OrderNotFoundError


def get_order_by_number(db: Session, order_number: str) -> Order:
    """
    Fetch an order by its order number (e.g. NS1001).
    Raises OrderNotFoundError if not found.
    """
    order = db.query(Order).filter(Order.order_number == order_number).first()

    if not order:
        raise OrderNotFoundError(order_number)

    return order
