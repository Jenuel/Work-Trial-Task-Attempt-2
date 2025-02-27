from fastapi import FastAPI
from .routers import order_router  
from . import models, database  

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

app.include_router(order_router.router)