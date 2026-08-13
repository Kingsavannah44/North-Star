def test_order_status_question_is_classified(client):
    """Order-related message is classified as order_status."""
    response = client.post("/api/support/query", json={"message": "Where is my order NS1001?"})
    assert response.status_code == 200
    data = response.json()
    assert data["data"]["category"] == "order_status"


def test_stock_question_is_classified(client):
    """Stock-related message is classified as stock_availability."""
    response = client.post("/api/support/query", json={"message": "Is Nike Air Max size 42 available?"})
    assert response.status_code == 200
    data = response.json()
    assert data["data"]["category"] == "stock_availability"


def test_order_question_with_valid_order_is_deflected(client):
    """Valid order number in message returns deflected=true with a meaningful answer."""
    response = client.post("/api/support/query", json={"message": "Where is my order NS1001?"})
    assert response.status_code == 200
    data = response.json()
    assert data["data"]["deflected"] is True
    assert "NS1001" in data["data"]["answer"]
    assert "shipped" in data["data"]["answer"].lower()


def test_order_question_with_unknown_order_is_not_deflected(client):
    """Order number not in DB — deflected=false, helpful message returned."""
    response = client.post("/api/support/query", json={"message": "Where is my order NS9999?"})
    assert response.status_code == 200
    data = response.json()
    assert data["data"]["deflected"] is False
    assert "NS9999" in data["data"]["answer"]


def test_stock_question_with_known_product_is_deflected(client):
    """Known product stock question returns deflected=true."""
    response = client.post("/api/support/query", json={"message": "Is Nike Air Max size 42 available?"})
    assert response.status_code == 200
    data = response.json()
    assert data["data"]["deflected"] is True
    assert "Nike Air Max" in data["data"]["answer"]


def test_unknown_question_returns_deflected_false(client):
    """Unrecognised question returns unknown category and deflected=false."""
    response = client.post("/api/support/query", json={"message": "What is your return policy?"})
    assert response.status_code == 200
    data = response.json()
    assert data["data"]["category"] == "unknown"
    assert data["data"]["deflected"] is False


def test_empty_message_returns_422(client):
    """Empty message fails Pydantic validation."""
    response = client.post("/api/support/query", json={"message": ""})
    assert response.status_code == 422


def test_missing_message_field_returns_422(client):
    """Missing message field fails Pydantic validation."""
    response = client.post("/api/support/query", json={})
    assert response.status_code == 422
