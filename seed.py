"""
Seed script — populates the database with realistic sample data.
Safe to re-run: clears existing data before inserting.

Usage:
    python seed.py
"""

from app.database import engine, SessionLocal
from app.database import Base

# Import all models so Base knows about them
from app.models.customer import Customer
from app.models.order import Order
from app.models.product import Product
from app.models.inventory import Inventory

from datetime import date


def seed():
    # Create all tables if they don't exist
    Base.metadata.create_all(bind=engine)

    db = SessionLocal()

    try:
        # ----------------------------------------------------------------
        # Clear existing data (order matters due to FK constraints)
        # ----------------------------------------------------------------
        print("Clearing existing data...")
        db.query(Inventory).delete()
        db.query(Order).delete()
        db.query(Customer).delete()
        db.query(Product).delete()
        db.commit()

        # ----------------------------------------------------------------
        # Customers
        # ----------------------------------------------------------------
        print("Seeding customers...")
        customers = [
            Customer(name="Alice Johnson",   email="alice@example.com"),
            Customer(name="Bob Smith",        email="bob@example.com"),
            Customer(name="Carol White",      email="carol@example.com"),
            Customer(name="David Brown",      email="david@example.com"),
            Customer(name="Emma Davis",       email="emma@example.com"),
            Customer(name="Frank Miller",     email="frank@example.com"),
            Customer(name="Grace Wilson",     email="grace@example.com"),
            Customer(name="Henry Moore",      email="henry@example.com"),
            Customer(name="Isabella Taylor",  email="isabella@example.com"),
            Customer(name="James Anderson",   email="james@example.com"),
        ]
        db.add_all(customers)
        db.commit()
        for c in customers:
            db.refresh(c)

        # ----------------------------------------------------------------
        # Orders
        # ----------------------------------------------------------------
        print("Seeding orders...")
        orders = [
            Order(
                order_number="NS1001",
                customer_id=customers[0].id,
                status="Shipped",
                tracking_number="TRK98231",
                estimated_delivery=date(2026, 8, 16),
            ),
            Order(
                order_number="NS1002",
                customer_id=customers[1].id,
                status="Processing",
                tracking_number=None,
                estimated_delivery=date(2026, 8, 20),
            ),
            Order(
                order_number="NS1003",
                customer_id=customers[2].id,
                status="Delivered",
                tracking_number="TRK11245",
                estimated_delivery=date(2026, 8, 5),
            ),
            Order(
                order_number="NS1004",
                customer_id=customers[3].id,
                status="Cancelled",
                tracking_number=None,
                estimated_delivery=None,
            ),
            Order(
                order_number="NS1005",
                customer_id=customers[4].id,
                status="Shipped",
                tracking_number="TRK44512",
                estimated_delivery=date(2026, 8, 18),
            ),
            Order(
                order_number="NS1006",
                customer_id=customers[5].id,
                status="Processing",
                tracking_number=None,
                estimated_delivery=date(2026, 8, 22),
            ),
            Order(
                order_number="NS1007",
                customer_id=customers[6].id,
                status="Delivered",
                tracking_number="TRK77893",
                estimated_delivery=date(2026, 8, 1),
            ),
            Order(
                order_number="NS1008",
                customer_id=customers[7].id,
                status="Shipped",
                tracking_number="TRK23456",
                estimated_delivery=date(2026, 8, 19),
            ),
            Order(
                order_number="NS1009",
                customer_id=customers[8].id,
                status="Processing",
                tracking_number=None,
                estimated_delivery=date(2026, 8, 25),
            ),
            Order(
                order_number="NS1010",
                customer_id=customers[9].id,
                status="Delivered",
                tracking_number="TRK99001",
                estimated_delivery=date(2026, 8, 7),
            ),
            Order(
                order_number="NS1011",
                customer_id=customers[0].id,
                status="Cancelled",
                tracking_number=None,
                estimated_delivery=None,
            ),
            Order(
                order_number="NS1012",
                customer_id=customers[1].id,
                status="Shipped",
                tracking_number="TRK55678",
                estimated_delivery=date(2026, 8, 17),
            ),
            Order(
                order_number="NS1013",
                customer_id=customers[2].id,
                status="Processing",
                tracking_number=None,
                estimated_delivery=date(2026, 8, 24),
            ),
            Order(
                order_number="NS1014",
                customer_id=customers[3].id,
                status="Delivered",
                tracking_number="TRK34521",
                estimated_delivery=date(2026, 8, 3),
            ),
            Order(
                order_number="NS1015",
                customer_id=customers[4].id,
                status="Shipped",
                tracking_number="TRK66432",
                estimated_delivery=date(2026, 8, 21),
            ),
        ]
        db.add_all(orders)
        db.commit()

        # ----------------------------------------------------------------
        # Products
        # ----------------------------------------------------------------
        print("Seeding products...")
        products = [
            Product(name="Nike Air Max",          sku="NAM-001", description="Classic running shoe."),
            Product(name="Adidas Ultraboost",      sku="AUB-002", description="High-performance running shoe."),
            Product(name="Puma RS-X",              sku="PRX-003", description="Retro-style sneaker."),
            Product(name="New Balance 990",        sku="NB9-004", description="Premium everyday trainer."),
            Product(name="Converse Chuck Taylor",  sku="CCT-005", description="Iconic canvas sneaker."),
            Product(name="Vans Old Skool",         sku="VOS-006", description="Classic skate shoe."),
            Product(name="Reebok Classic Leather", sku="RCL-007", description="Timeless leather trainer."),
            Product(name="Jordan 1 Retro",         sku="J1R-008", description="Iconic basketball shoe."),
            Product(name="Asics Gel Nimbus",       sku="AGN-009", description="Long-distance running shoe."),
            Product(name="Skechers D'Lites",       sku="SDL-010", description="Chunky comfort sneaker."),
        ]
        db.add_all(products)
        db.commit()
        for p in products:
            db.refresh(p)

        # ----------------------------------------------------------------
        # Inventory
        # ----------------------------------------------------------------
        print("Seeding inventory...")
        inventory = [
            # Nike Air Max — mixed stock
            Inventory(product_id=products[0].id, size="40", quantity=5),
            Inventory(product_id=products[0].id, size="41", quantity=3),
            Inventory(product_id=products[0].id, size="42", quantity=8),
            Inventory(product_id=products[0].id, size="43", quantity=0),
            Inventory(product_id=products[0].id, size="44", quantity=3),

            # Adidas Ultraboost — good stock
            Inventory(product_id=products[1].id, size="40", quantity=10),
            Inventory(product_id=products[1].id, size="41", quantity=7),
            Inventory(product_id=products[1].id, size="42", quantity=12),
            Inventory(product_id=products[1].id, size="43", quantity=6),

            # Puma RS-X — mostly out of stock
            Inventory(product_id=products[2].id, size="41", quantity=0),
            Inventory(product_id=products[2].id, size="42", quantity=0),
            Inventory(product_id=products[2].id, size="43", quantity=1),

            # New Balance 990 — letter sizes
            Inventory(product_id=products[3].id, size="S",  quantity=4),
            Inventory(product_id=products[3].id, size="M",  quantity=9),
            Inventory(product_id=products[3].id, size="L",  quantity=2),
            Inventory(product_id=products[3].id, size="XL", quantity=0),

            # Converse Chuck Taylor — good stock
            Inventory(product_id=products[4].id, size="38", quantity=6),
            Inventory(product_id=products[4].id, size="39", quantity=8),
            Inventory(product_id=products[4].id, size="40", quantity=11),
            Inventory(product_id=products[4].id, size="41", quantity=5),

            # Vans Old Skool — partial stock
            Inventory(product_id=products[5].id, size="39", quantity=3),
            Inventory(product_id=products[5].id, size="40", quantity=0),
            Inventory(product_id=products[5].id, size="41", quantity=7),

            # Reebok Classic — fully out of stock
            Inventory(product_id=products[6].id, size="40", quantity=0),
            Inventory(product_id=products[6].id, size="41", quantity=0),
            Inventory(product_id=products[6].id, size="42", quantity=0),

            # Jordan 1 Retro — limited stock
            Inventory(product_id=products[7].id, size="41", quantity=2),
            Inventory(product_id=products[7].id, size="42", quantity=1),
            Inventory(product_id=products[7].id, size="43", quantity=0),

            # Asics Gel Nimbus — good stock
            Inventory(product_id=products[8].id, size="40", quantity=8),
            Inventory(product_id=products[8].id, size="41", quantity=10),
            Inventory(product_id=products[8].id, size="42", quantity=5),
            Inventory(product_id=products[8].id, size="43", quantity=3),

            # Skechers D'Lites — mixed
            Inventory(product_id=products[9].id, size="38", quantity=0),
            Inventory(product_id=products[9].id, size="39", quantity=4),
            Inventory(product_id=products[9].id, size="40", quantity=6),
        ]
        db.add_all(inventory)
        db.commit()

        print("\n✓ Database seeded successfully.")
        print(f"  {len(customers)} customers")
        print(f"  {len(orders)} orders")
        print(f"  {len(products)} products")
        print(f"  {len(inventory)} inventory rows")

    except Exception as e:
        db.rollback()
        print(f"\n✗ Seeding failed: {e}")
        raise
    finally:
        db.close()


if __name__ == "__main__":
    seed()
