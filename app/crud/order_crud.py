from sqlalchemy.orm import Session
from .. import models, schemas
from fastapi import HTTPException

def get_orders(db: Session, skip: int = 0, limit: int = 100):
    """
    Retrieves a list of orders.

    Args:
        db (Session): The database session.
        skip (int): The number of orders to skip.
        limit (int): The maximum number of orders to retrieve.

    Returns:
        List[models.Order]: A list of orders.
    """
    return db.query(models.Order).offset(skip).limit(limit).all()

def create_order(db: Session, order: schemas.OrderCreate):
    """
    Creates a new order.

    Args:
        db (Session): The database session.
        order (schemas.OrderCreate): The order data.

    Returns:
        models.Order: The created order.
    """
    db_order = models.Order(**order.dict())
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order