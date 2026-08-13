import re
from typing import Optional
from sqlalchemy.orm import Session
from app.services.order_service import get_order_by_number
from app.services.inventory_service import check_availability
from app.models.product import Product
from app.utils.exceptions import OrderNotFoundError, ProductNotFoundError, SizeNotFoundError


# ---------------------------------------------------------------------------
# Classification
# ---------------------------------------------------------------------------

ORDER_KEYWORDS = [
    "where is my order", "order status", "track my order",
    "has my order shipped", "when will my order", "order number",
    "my order", "shipment", "tracking", "dispatched",
    "delivery status", "shipped", "arrive",
]

STOCK_KEYWORDS = [
    "in stock", "out of stock", "available", "availability",
    "do you have", "is there", "size", "stock", "quantity",
    "left in", "any left",
]


def classify_message(message: str) -> str:
    """
    Classify a message as 'order_status', 'stock_availability', or 'unknown'
    using simple keyword matching. Order keywords are checked first.
    """
    lower = message.lower()

    if any(kw in lower for kw in ORDER_KEYWORDS):
        return "order_status"

    if any(kw in lower for kw in STOCK_KEYWORDS):
        return "stock_availability"

    return "unknown"


# ---------------------------------------------------------------------------
# Extractors
# ---------------------------------------------------------------------------

def extract_order_number(message: str) -> Optional[str]:
    """Extract an order number like NS1001 from a message."""
    match = re.search(r"\bNS\d+\b", message, re.IGNORECASE)
    return match.group(0).upper() if match else None


def extract_size(message: str) -> Optional[str]:
    """
    Extract a size from a message.
    Handles: 'size 42', 'in size M', 'size XL', 'size 10.5'
    """
    match = re.search(r"\b(?:in\s+)?size\s+(\S+)", message, re.IGNORECASE)
    return match.group(1) if match else None


def find_product_in_message(db: Session, message: str) -> Optional[Product]:
    """
    Scan all product names and return the first one found in the message.
    """
    products = db.query(Product).all()
    lower = message.lower()
    for product in products:
        if product.name.lower() in lower:
            return product
    return None


# ---------------------------------------------------------------------------
# Main handler
# ---------------------------------------------------------------------------

def handle_support_query(db: Session, message: str) -> dict:
    """
    Classify the message and attempt to compose an automated answer.
    Always returns: { category, answer, deflected }
    """
    category = classify_message(message)

    # --- ORDER STATUS ---
    if category == "order_status":
        order_number = extract_order_number(message)

        if not order_number:
            return {
                "category": category,
                "answer": (
                    "It looks like you have a question about an order. "
                    "Please provide your order number (e.g. NS1001) so we can look it up."
                ),
                "deflected": False,
            }

        try:
            order = get_order_by_number(db, order_number)
        except OrderNotFoundError:
            return {
                "category": category,
                "answer": (
                    f"We couldn't find order {order_number}. "
                    "Please double-check the number or contact Northstar Support."
                ),
                "deflected": False,
            }

        status_answers = {
            "Processing": (
                f"Your order {order.order_number} is currently being processed. "
                "We'll notify you once it ships."
            ),
            "Shipped": (
                f"Your order {order.order_number} has shipped"
                + (f" (tracking: {order.tracking_number})" if order.tracking_number else "")
                + (f" and is expected to arrive on {order.estimated_delivery}." if order.estimated_delivery else ".")
            ),
            "Delivered": (
                f"Your order {order.order_number} has been delivered. "
                "We hope you enjoy your purchase!"
            ),
            "Cancelled": (
                f"Your order {order.order_number} was cancelled. "
                "Please contact Northstar Support if you need further assistance."
            ),
        }

        return {
            "category": category,
            "answer": status_answers.get(
                order.status,
                f"Your order {order.order_number} status is: {order.status}.",
            ),
            "deflected": True,
        }

    # --- STOCK AVAILABILITY ---
    if category == "stock_availability":
        size = extract_size(message)
        product = find_product_in_message(db, message)

        if not product:
            return {
                "category": category,
                "answer": (
                    "I couldn't identify which product you're asking about. "
                    "Please visit our product pages or contact Northstar Support."
                ),
                "deflected": False,
            }

        try:
            availability = check_availability(db, product.id, size)
        except SizeNotFoundError as e:
            return {
                "category": category,
                "answer": e.detail["message"],
                "deflected": False,
            }
        except ProductNotFoundError:
            return {
                "category": "unknown",
                "answer": "I couldn't find an automated answer. Please contact Northstar Support.",
                "deflected": False,
            }

        size_text = f" size {availability['size']}" if availability["size"] else ""

        if availability["available"]:
            answer = (
                f"{availability['product_name']}{size_text} is currently in stock. "
                f"{availability['quantity']} unit(s) available."
            )
        else:
            answer = (
                f"Sorry, {availability['product_name']}{size_text} is currently out of stock. "
                "Please check back later or contact Northstar Support."
            )

        return {
            "category": category,
            "answer": answer,
            "deflected": True,
        }

    # --- UNKNOWN ---
    return {
        "category": "unknown",
        "answer": "I couldn't find an automated answer for your question. Please contact Northstar Support.",
        "deflected": False,
    }
