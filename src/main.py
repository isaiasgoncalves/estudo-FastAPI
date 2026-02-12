from fastapi import FastAPI

from src.auth_routes import auth_router
from order_routes import order_router



# Para rodar:
# > uvicorn main:app --reload
app = FastAPI()
app.include_router(auth_router)
app.include_router(order_router)



