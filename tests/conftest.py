"""
Test configuration.

Uses an in-memory SQLite database so tests run without a MySQL server.
The app's get_db dependency is overridden to use the test DB session.
"""

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.main import app
from app.database import Base, get_db
from app.models.customer import Customer
from app.models.order import Order
from app.models.product import Product
from app.models.inventory import Inventory
from datetime import date

SQLITE_URL = "sqlite:///./test.db"

engine = create_engine(SQLITE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db


@pytest.fixture(scope="session", autouse=True)
def setup_database():
    """Create tables and seed test data once for the entire test session."""
    Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()

    # Customers
    customer = Customer(name="Test User", email="test@example.com")
    db.add(customer)
    db.commit()
    db.refresh(customer)

    # Orders
    db.add_all([
        Order(
            order_number="NS1001",
            customer_id=customer.id,
            status="Shipped",
            tracking_number="TRK98231",
            estimated_delivery=date(2026, 8, 16),
        ),
        Order(
            order_number="NS1002",
            customer_id=customer.id,
            status="Processing",
            tracking_number=None,
            estimated_delivery=date(2026, 8, 20),
        ),
        Order(
            order_number="NS1003",
            customer_id=customer.id,
            status="Delivered",
            tracking_number="TRK11111",
            estimated_delivery=date(2026, 8, 1),
        ),
        Order(
            order_number="NS1004",
            customer_id=customer.id,
            status="Cancelled",
            tracking_number=None,
            estimated_delivery=None,
        ),
    ])
    db.commit()

    # Products
    product1 = Product(name="Nike Air Max", sku="NAM-001", description="Test product")
    product2 = Product(name="Adidas Ultraboost", sku="AUB-002", description="Test product 2")
    db.add_all([product1, product2])
    db.commit()
    db.refresh(product1)
    db.refresh(product2)

    # Inventory
    db.add_all([
        Inventory(product_id=product1.id, size="42", quantity=8),
        Inventory(product_id=product1.id, size="43", quantity=0),
        Inventory(product_id=product1.id, size="44", quantity=3),
        # product2 fully out of stock
        Inventory(product_id=product2.id, size="40", quantity=0),
        Inventory(product_id=product2.id, size="41", quantity=0),
    ])
    db.commit()
    db.close()

    yield

    Base.metadata.drop_all(bind=engine)


@pytest.fixture(scope="session")
def client():
    return TestClient(app)
