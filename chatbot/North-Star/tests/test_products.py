def test_product_with_available_size(client):
    """Product 1, size 42 — in stock with 8 units."""
    response = client.get("/api/products/1/availability?size=42")
    assert response.status_code == 200
    data = response.json()
    assert data["success"] is True
    assert data["data"]["available"] is True
    assert data["data"]["quantity"] == 8
    assert data["data"]["size"] == "42"
    assert data["data"]["product_name"] == "Nike Air Max"


def test_product_with_zero_stock_size(client):
    """Product 1, size 43 — exists but out of stock."""
    response = client.get("/api/products/1/availability?size=43")
    assert response.status_code == 200
    data = response.json()
    assert data["data"]["available"] is False
    assert data["data"]["quantity"] == 0


def test_product_without_size_returns_total(client):
    """Product 1, no size filter — returns aggregated total stock."""
    response = client.get("/api/products/1/availability")
    assert response.status_code == 200
    data = response.json()
    assert data["data"]["size"] is None
    assert data["data"]["quantity"] == 11  # 8 + 0 + 3
    assert data["data"]["available"] is True


def test_product_not_found_returns_404(client):
    """Non-existent product ID returns 404."""
    response = client.get("/api/products/9999/availability")
    assert response.status_code == 404
    data = response.json()
    assert data["success"] is False
    assert data["error"]["code"] == "PRODUCT_NOT_FOUND"


def test_size_not_found_returns_404(client):
    """Requesting a size that doesn't exist for the product returns 404."""
    response = client.get("/api/products/1/availability?size=99")
    assert response.status_code == 404
    data = response.json()
    assert data["error"]["code"] == "SIZE_NOT_FOUND"


def test_fully_out_of_stock_product(client):
    """Product 2 — all sizes have 0 quantity."""
    response = client.get("/api/products/2/availability")
    assert response.status_code == 200
    data = response.json()
    assert data["data"]["available"] is False
    assert data["data"]["quantity"] == 0
