from sqlalchemy.orm import Session
from typing import Optional
from app.models.product import Product
from app.models.inventory import Inventory
from app.utils.exceptions import ProductNotFoundError, SizeNotFoundError


def check_availability(db: Session, product_id: int, size: Optional[str] = None) -> dict:
    product = db.query(Product).filter(Product.id == product_id).first()

    if not product:
        raise ProductNotFoundError(product_id)

    if size:
        inventory_row = (
            db.query(Inventory)
            .filter(
                Inventory.product_id == product_id,
                Inventory.size.ilike(size),
            )
            .first()
        )

        if not inventory_row:
            raise SizeNotFoundError(size, product.name)

        return {
            "product_id": product.id,
            "product_name": product.name,
            "size": inventory_row.size,
            "available": inventory_row.quantity > 0,
            "quantity": inventory_row.quantity,
        }

    rows = db.query(Inventory).filter(Inventory.product_id == product_id).all()
    total_quantity = sum(row.quantity for row in rows)

    return {
        "product_id": product.id,
        "product_name": product.name,
        "size": None,
        "available": total_quantity > 0,
        "quantity": total_quantity,
    }
