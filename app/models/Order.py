from sqlalchemy import Column, Integer, String, Float
from ..database import Base

class Order(Base):
    """Represents an order in the database."""
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    symbol = Column(String, description="The symbol of the stock.")
    price = Column(Float, description="The price of the order.")
    quantity = Column(Integer, description="The quantity of the order.")
    order_type = Column(String, description="The type of the order (buy or sell).")