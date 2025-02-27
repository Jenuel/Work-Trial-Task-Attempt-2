import pytest
from fastapi.testclient import TestClient
from unittest.mock import MagicMock

from app.main import app
from app import schemas, crud
from app.routers import order_router 

client = TestClient(app)

mock_orders = [
    schemas.OrderRead(id=1, symbol="AAPL", price=150.0, quantity=10, order_type="buy"),
    schemas.OrderRead(id=2, symbol="GOOG", price=2700.0, quantity=5, order_type="sell"),
]

def mock_get_orders(db, skip, limit):
    return mock_orders[skip:skip + limit]

def mock_create_order(db, order):
    new_id = len(mock_orders) + 1
    new_order = schemas.OrderRead(id=new_id, **order.dict())
    mock_orders.append(new_order)
    return new_order

@pytest.fixture(autouse=True)
def mock_crud_functions(monkeypatch):
    monkeypatch.setattr(crud, "get_orders", mock_get_orders)
    monkeypatch.setattr(crud, "create_order", mock_create_order)

def test_read_orders():
    response = client.get("/orders/")
    assert response.status_code == 200
    orders = response.json()
    assert isinstance(orders, list)
    assert len(orders) == len(mock_orders)

def test_create_order():
    order_data = {
        "symbol": "MSFT",
        "price": 300.0,
        "quantity": 20,
        "order_type": "buy"
    }
    response = client.post("/orders/create", json=order_data)
    assert response.status_code == 200
    created_order = response.json()
    assert created_order["symbol"] == "MSFT"
    assert created_order["price"] == 300.0
    assert created_order["quantity"] == 20
    assert created_order["order_type"] == "buy"
    assert "id" in created_order
    assert created_order["id"] == len(mock_orders)