"""
Este módulo define as rotas da API relacionadas ao gerenciamento de pedidos na aplicação FastAPI.
"""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from src.dependencies import make_session, verify_token
from src.schemas import OrderSchema
from src.models import Pedido


order_router = APIRouter(prefix="/orders", tags=["Pedidos"], dependencies=[Depends(verify_token)])

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
    return {"m  essage": f"Pedido adicionado com sucesso. ID do Pedido: {new_order.id}"}


@order_router.post("/order/cancel/{order_id}", tags=["Pedidos"])
async def cancel_order(order_id : int, session: Session = Depends(make_session), user = Depends(verify_token)):
    order = session.query(Pedido).filter(Pedido.id == order_id).first()

    if not order:
        raise HTTPException(status_code=400, detail="Pedido não encontrado")

    if not user.admin and user.id != order.usuario.id:
        raise HTTPException(status_code=401, detail="Acesso negado")

    order.status = "CANCELADO"
    session.commit()
    return {
        "message": f"Pedido {order_id} cancelado com sucesso",
        "order" : order
    }