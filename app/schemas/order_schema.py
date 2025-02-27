from pydantic import BaseModel
from typing import Optional, List

class OrderBase(BaseModel):
    """Base schema for an order."""
    symbol: str = "AAPL"
    price: float = 150.50
    quantity: int = 10
    order_type: str = "buy"

class OrderCreate(OrderBase):
    """Schema for creating an order."""
    pass

class OrderRead(OrderBase):
    """Schema for reading an order."""
    id: int

    class Config:
        orm_mode = True