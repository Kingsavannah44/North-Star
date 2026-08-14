def test_existing_order_returns_correct_data(client):
    """Existing order NS1001 returns full order details."""
    response = client.get("/api/orders/NS1001")
    assert response.status_code == 200
    data = response.json()
    assert data["success"] is True
    assert data["data"]["order_number"] == "NS1001"
    assert data["data"]["status"] == "Shipped"
    assert data["data"]["tracking_number"] == "TRK98231"
    assert data["data"]["estimated_delivery"] == "2026-08-16"


def test_order_not_found_returns_404(client):
    """Unknown order number returns 404 with structured error."""
    response = client.get("/api/orders/NS9999")
    assert response.status_code == 404
    data = response.json()
    assert data["success"] is False
    assert data["error"]["code"] == "ORDER_NOT_FOUND"
    assert "NS9999" in data["error"]["message"]


def test_processing_order(client):
    """Processing order returns correct status."""
    response = client.get("/api/orders/NS1002")
    assert response.status_code == 200
    assert response.json()["data"]["status"] == "Processing"
    assert response.json()["data"]["tracking_number"] is None


def test_delivered_order(client):
    """Delivered order returns correct status."""
    response = client.get("/api/orders/NS1003")
    assert response.status_code == 200
    assert response.json()["data"]["status"] == "Delivered"


def test_cancelled_order(client):
    """Cancelled order returns correct status with no delivery date."""
    response = client.get("/api/orders/NS1004")
    assert response.status_code == 200
    data = response.json()["data"]
    assert data["status"] == "Cancelled"
    assert data["estimated_delivery"] is None


def test_order_number_is_case_insensitive(client):
    """Order number lookup works regardless of case."""
    response = client.get("/api/orders/ns1001")
    assert response.status_code == 200
    assert response.json()["data"]["order_number"] == "NS1001"
