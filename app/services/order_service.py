from sqlalchemy.orm import Session
from app.models.order import Order
from app.utils.exceptions import OrderNotFoundError


def get_order_by_number(db: Session, order_number: str) -> Order:
    order = db.query(Order).filter(Order.order_number == order_number).first()

    if not order:
        raise OrderNotFoundError(order_number)

    return order
