from fastapi import FastAPI
from .routers import order_router  
from .database import engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(order_router.router)