"""
Este módulo define as rotas da API relacionadas ao gerenciamento de pedidos na aplicação FastAPI.
"""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from src.dependencies import make_session
from src.schemas import OrderSchema
from src.models import Pedido


order_router = APIRouter(prefix="/orders", tags=["Pedidos"])

@order_router.get("/", tags=["Pedidos"])
async def orders():
    """
    Rota padrão para gerenciamento de pedidos.

    Returns:
        dict: Uma mensagem indicando acesso à rota de pedidos.
    """
    return {"message": "Você acessou a rota de pedidos"}


@order_router.post("/order", tags=["Pedidos"])
async def make_order(order_schema:OrderSchema, session: Session = Depends(make_session)):
    """
    Cria um novo pedido no sistema.

    Args:
        order_schema (OrderSchema): Esquema Pydantic contendo os detalhes do pedido (por exemplo, user_id).
        session (Session): A dependência da sessão do banco de dados SQLAlchemy.

    Returns:
        dict: Uma mensagem indicando a criação bem-sucedida do pedido e o ID do novo pedido.
    """
    new_order = Pedido(usuario=order_schema.user_id)
    session.add(new_order)
    session.commit()
    return {"message": f"Pedido adicionado com sucesso. ID do Pedido: {new_order.id}"}