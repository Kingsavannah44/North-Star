from typing import Optional
from sqlalchemy.orm import Session
from app.models.product import Product
from app.models.inventory import Inventory
from app.utils.exceptions import ProductNotFoundError, SizeNotFoundError


def check_availability(db: Session, product_id: int, size: Optional[str] = None) -> dict:
    product = db.query(Product).filter(Product.id == product_id).first()
    if not product:
        raise ProductNotFoundError(product_id)

    if size:
        row = db.query(Inventory).filter(
            Inventory.product_id == product_id,
            Inventory.size.ilike(size)
        ).first()

        if not row:
            raise SizeNotFoundError(size, product.name)

        return {
            "product_id": product.id,
            "product_name": product.name,
            "size": row.size,
            "available": row.quantity > 0,
            "quantity": row.quantity,
        }

    all_rows = db.query(Inventory).filter(Inventory.product_id == product_id).all()
    total = sum(r.quantity for r in all_rows)

    return {
        "product_id": product.id,
        "product_name": product.name,
        "size": None,
        "available": total > 0,
        "quantity": total,
    }
