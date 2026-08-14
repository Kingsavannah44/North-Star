# Frontend

This folder is owned by the frontend developer.

Place your `index.html`, `style.css`, and `app.js` here. FastAPI will serve everything in this folder as static files and will serve `index.html` at the root `/`.

---

## How the backend serves this folder

- `/` → serves `index.html`
- `/static/style.css` → serves `style.css`
- `/static/app.js` → serves `app.js`

---

## API endpoints you can call from JavaScript

All endpoints are on the same server, so no CORS configuration is needed.

**Get order status**
```
GET /api/orders/{order_number}
```

Example:
```js
const res = await fetch('/api/orders/NS1001');
const json = await res.json();
// json.data.order_number, json.data.status, json.data.tracking_number, json.data.estimated_delivery
```

**Check stock availability**
```
GET /api/products/{product_id}/availability?size=42
```

Example:
```js
const res = await fetch('/api/products/1/availability?size=42');
const json = await res.json();
// json.data.product_name, json.data.available, json.data.quantity
```

**Submit a support question**
```
POST /api/support/query
Content-Type: application/json
```

Example:
```js
const res = await fetch('/api/support/query', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({ message: 'Where is my order NS1001?' })
});
const json = await res.json();
// json.data.category, json.data.answer, json.data.deflected
```

---

## Response shapes

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

**Support query:**
```json
{
  "success": true,
  "data": {
    "category": "order_status",
    "answer": "Your order NS1001 has shipped...",
    "deflected": true
  }
}
```

**Error:**
```json
{
  "success": false,
  "error": {
    "code": "ORDER_NOT_FOUND",
    "message": "Order NS9999 was not found."
  }
}
```

---

## Starting the full application

```bash
python start.py
```

The app runs at `http://localhost:8000`.
