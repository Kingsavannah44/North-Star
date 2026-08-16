Northstar Retail's support team answers the same three questions all day: where is my order, how do I return this, and is this in stock. Every one of those is a ticket a person has to open and answer by hand.

This is a chatbot that answers all three without a human, so the ticket never gets opened. Anything it can't answer is passed to a person with a ticket reference rather than guessed at.

Run it with one command - `python start.py` - then open http://localhost:8000

**Team**
- Ibrahim Warsame - team lead
- Brian Kipkemoi - backend
- Ursula Immaculate - frontend
- Eric Kamau - QA
- Batula - documentation

Backend setup instructions are below. The go-live readiness note is in GO-LIVE.md.

# Northstar Support Deflection Backend

This is the backend API for Northstar Retail Co.'s support deflection MVP. It was built as part of a 5-day sprint to reduce the volume of repetitive customer support tickets.

---

## What problem does this solve?

Northstar's support team was getting overwhelmed by the same questions every day — mostly people asking where their order is or whether something is in stock. This backend handles those questions automatically so they never need to reach a human agent.

---

## What it covers

- Order status lookup by order number
- Stock availability check by product and size
- Automatic classification of customer support messages
- Automated responses for supported question types
- Clean fallback when the system can't confidently answer

Returns and refunds are out of scope for this sprint.

---

## Tech stack

- Python 3.11+
- FastAPI
- MySQL
- SQLAlchemy ORM
- Pydantic v2
- PyMySQL
- Uvicorn
- Pytest + HTTPX for testing

---

## Project structure

```
northstar-backend/
├── app/
│   ├── main.py
│   ├── database.py
│   ├── models/
│   │   ├── customer.py
│   │   ├── order.py
│   │   ├── product.py
│   │   └── inventory.py
│   ├── schemas/
│   │   ├── order.py
│   │   ├── product.py
│   │   └── support.py
│   ├── routes/
│   │   ├── orders.py
│   │   ├── products.py
│   │   └── support.py
│   ├── services/
│   │   ├── order_service.py
│   │   ├── inventory_service.py
│   │   └── support_service.py
│   └── utils/
│       └── exceptions.py
├── tests/
│   ├── conftest.py
│   ├── test_orders.py
│   ├── test_products.py
│   └── test_support.py
├── seed.py
├── requirements.txt
├── pytest.ini
├── .env.example
└── README.md
```

---

## Getting started

### 1. Clone the repo

```bash
git clone https://github.com/Kingsavannah44/North-Star.git
cd North-Star
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it:

```bash
# Windows
venv\Scripts\activate

# macOS / Linux
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set up environment variables

Copy the example file and fill in your database credentials:

```bash
cp .env.example .env
```

Open `.env` and update:

```
DATABASE_HOST=localhost
DATABASE_PORT=3306
DATABASE_NAME=northstar_db
DATABASE_USER=root
DATABASE_PASSWORD=yourpassword
APP_ENV=development
PORT=8000
```

### 5. Seed the database

This will create the database if it doesn't exist, create all tables, and insert sample data:

```bash
python seed.py
```

You'll get 10 customers, 15 orders across all statuses, 10 products and 36 inventory rows with a mix of in-stock and out-of-stock sizes.

### 6. Start the server

```bash
uvicorn app.main:app --reload --port 8000
```

The API will be running at `http://localhost:8000`.

Swagger docs are at `http://localhost:8000/docs`.

---

## API endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/health` | Check if the server is running |
| GET | `/api/orders/{order_number}` | Look up an order by its number |
| GET | `/api/products/{product_id}/availability` | Check stock, optional `?size=` param |
| POST | `/api/support/query` | Submit a support question |

---

## Example requests

**Check an order:**
```bash
curl http://localhost:8000/api/orders/NS1001
```

**Check stock for a specific size:**
```bash
curl "http://localhost:8000/api/products/1/availability?size=42"
```

**Ask a support question:**
```bash
curl -X POST http://localhost:8000/api/support/query \
  -H "Content-Type: application/json" \
  -d '{"message": "Where is my order NS1001?"}'
```

---

## Example responses

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

**Stock check:**
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

**Support question — answered automatically:**
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

**Support question — escalated to human:**
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

## Running tests

Tests use SQLite in memory so you don't need a MySQL connection running.

```bash
pytest
```

Verbose output:

```bash
pytest -v
```

---

## Known limitations

- The support classifier uses keyword matching, so unusual phrasing can be misclassified
- Product name matching in support queries is a simple substring check
- No authentication on any endpoints
- Order number extraction only works for the NS#### format
- No pagination on any listing endpoints

---

## What could be improved next

- Add JWT authentication so customers can only see their own orders
- Improve the classifier with a lightweight ML model
- Add pagination to product listings
- Build out the returns and refunds workflow
- Add rate limiting to prevent abuse
- Cache frequently queried orders and products with Redis
