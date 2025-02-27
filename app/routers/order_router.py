from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import crud, schemas, database
from typing import List

router = APIRouter(prefix="/orders", tags=["orders"])

@router.get("/", response_model=List[schemas.OrderRead], summary="Get a list of orders")
def read_orders(skip: int = 0, limit: int = 100, db: Session = Depends(database.get_db)):
    """
    Retrieves a list of orders.

    Args:
        skip (int): The number of orders to skip.
        limit (int): The maximum number of orders to retrieve.
        db (Session): The database session.

    Returns:
        List[schemas.OrderRead]: A list of orders.
    """
    return crud.get_orders(db=db, skip=skip, limit=limit)

@router.post("/create", response_model=schemas.OrderRead, summary="Create a new order")
def create_order(order: schemas.OrderCreate, db: Session = Depends(database.get_db)):
    """
    Creates a new order.

    Args:
        order (schemas.OrderCreate): The order data.
        db (Session): The database session.

    Returns:
        schemas.OrderRead: The created order.
    """
    return crud.create_order(db=db, order=order)