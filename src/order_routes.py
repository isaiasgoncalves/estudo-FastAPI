from fastapi import APIRouter

order_router = APIRouter(prefix="/order", tags=["Pedidos"])

@order_router.get("/", tags=["Pedidos"])
async def orders():
    """
    Rota padrão de Pedidos
    """
    return {"message": "Você acessou a rota de pedidos"}


 