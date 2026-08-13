# Northstar Support Deflection Backend

Backend API for Northstar Retail Co.'s support deflection MVP, built with Python, FastAPI, and MySQL.

---

## 1. Project Overview

A REST API that automatically answers two of the most common customer support question types:

- **Order status** — "Where is my order NS1001?"
- **Stock availability** — "Is Nike Air Max size 42 available?"

---

## 2. Business Problem

Northstar's customer support team is overwhelmed by repetitive questions. This MVP intercepts and automatically answers the most common queries, reducing the volume of tickets that reach human agents.

---

## 3. MVP Scope

| Feature | Included |
|---------|----------|
| Order status lookup | ✅ |
| Stock availability check | ✅ |
| Support query classification | ✅ |
| Automated support answers | ✅ |
| Returns & refunds | ❌ (out of scope) |
| Authentication | ❌ (out of scope) |
| Admin dashboard | ❌ (out of scope) |

---

## 4. Technology Stack

| Layer | Technology |
|-------|-----------|
| Language | Python 3.11+ |
| Framework | FastAPI |
| Database | MySQL |
| ORM | SQLAlchemy 2.0 |
| Validation | Pydantic v2 |
| DB Driver | PyMySQL |
| Server | Uvicorn |
| Testing | Pytest + HTTPX |

---

## 5. Project Structure

```
northstar-backend/
├── app/
│   ├── main.py               # FastAPI app, CORS, routers
│   ├── database.py           # SQLAlchemy engine and session
│   ├── models/               # SQLAlchemy ORM models
│   ├── schemas/              # Pydantic request/response schemas
│   ├── routes/               # FastAPI route handlers
│   ├── services/             # Business logic
│   └── utils/                # Shared exceptions
├── tests/                    # Pytest test suite
├── seed.py                   # Database seed script
├── requirements.txt
├── .env.example
└── README.md
```

---

## 6. Installation

```bash
git clone <repo-url>
cd northstar-backend
```

---

## 7. Virtual Environment Setup

```bash
# Create virtual environment
python -m venv venv

# Activate (Windows)
venv\Scripts\activate

# Activate (macOS/Linux)
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

---

## 8. Environment Configuration

Copy the example file and fill in your credentials:

```bash
cp .env.example .env
```

Edit `.env`:

```
DATABASE_HOST=localhost
DATABASE_PORT=3306
DATABASE_NAME=northstar_db
DATABASE_USER=root
DATABASE_PASSWORD=yourpassword
APP_ENV=development
PORT=8000
```

---

## 9. MySQL Database Setup

Create the database in MySQL:

```sql
CREATE DATABASE northstar_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

---

## 10. Database Tables

Tables are created automatically when you run the seed script. You can also create them manually:

```python
from app.database import engine, Base
import app.models  # ensure all models are imported
Base.metadata.create_all(bind=engine)
```

---

## 11. Seed the Database

```bash
python seed.py
```

This inserts:
- 10 customers
- 15 orders (Processing, Shipped, Delivered, Cancelled)
- 10 products
- 35 inventory rows (mix of in-stock and out-of-stock)

Safe to re-run — clears existing data first.

---

## 12. Run the Server

```bash
uvicorn app.main:app --reload --port 8000
```

Server will be available at: `http://localhost:8000`

---

## 13. API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/health` | Health check |
| GET | `/api/orders/{order_number}` | Get order status |
| GET | `/api/products/{product_id}/availability` | Check stock (optional `?size=`) |
| POST | `/api/support/query` | Submit support question |
| GET | `/docs` | Swagger UI |
| GET | `/redoc` | ReDoc |

---

## 14. Example Requests

**Order status:**
```bash
curl http://localhost:8000/api/orders/NS1001
```

**Stock availability with size:**
```bash
curl "http://localhost:8000/api/products/1/availability?size=42"
```

**Support query:**
```bash
curl -X POST http://localhost:8000/api/support/query \
  -H "Content-Type: application/json" \
  -d '{"message": "Where is my order NS1001?"}'
```

---

## 15. Example Responses

**Order found:**
```json
{
  "success": true,
  "data": {
    "order_number": "NS1001",
    "status": "Shipped",
    "tracking_number": "TRK98231",
    "estimated_delivery": "2026-08-16"
  }
}
```

**Order not found:**
```json
{
  "success": false,
  "error": {
    "code": "ORDER_NOT_FOUND",
    "message": "Order NS9999 was not found."
  }
}
```

**Stock available:**
```json
{
  "success": true,
  "data": {
    "product_id": 1,
    "product_name": "Nike Air Max",
    "size": "42",
    "available": true,
    "quantity": 8
  }
}
```

**Support — deflected:**
```json
{
  "success": true,
  "data": {
    "category": "order_status",
    "answer": "Your order NS1001 has shipped (tracking: TRK98231) and is expected to arrive on 2026-08-16.",
    "deflected": true
  }
}
```

**Support — not deflected:**
```json
{
  "success": true,
  "data": {
    "category": "unknown",
    "answer": "I couldn't find an automated answer for your question. Please contact Northstar Support.",
    "deflected": false
  }
}
```

---

## 16. Run Tests

Tests use an in-memory SQLite database — no MySQL connection needed.

```bash
pytest
```

Run with verbose output:

```bash
pytest -v
```

---

## 17. Known Limitations

- Classification uses keyword matching — ambiguous messages may be misclassified
- Product name matching in support queries is exact substring match (case-insensitive)
- No authentication or rate limiting
- No pagination on any endpoints
- Order number extraction only supports the NS#### format

---

## 18. Future Improvements

- Add JWT authentication for customer-specific order lookups
- Improve classification with a lightweight ML model
- Add pagination to product listings
- Implement returns & refunds workflow
- Add rate limiting per IP/customer
- Introduce Redis caching for frequently queried orders/products
