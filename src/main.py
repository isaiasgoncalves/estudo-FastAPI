"""
Este é o arquivo principal da aplicação para o projeto FastAPI.
Ele configura a instância da aplicação FastAPI e inclui todos os roteadores de API definidos.
"""

from fastapi import FastAPI

from src.routes.auth_routes import auth_router
from src.routes.order_routes import order_router



# Para rodar:
# > uvicorn main:app --reload
app = FastAPI()
"""
A instância principal da aplicação FastAPI.
Todas as rotas da API são incluídas aqui.
"""
app.include_router(auth_router)
app.include_router(auth_router)
app.include_router(order_router)



