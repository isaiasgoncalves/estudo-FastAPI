from fastapi import APIRouter

# Delimitando as rotas de autenticação
auth_router = APIRouter(prefix="/auth", tags=["Autenticação"])

@auth_router.get("/", tags=["Autenticação"])
async def auth():
    """
    Rota padrão de autenticação do sistema. Todas as rotas precisam de autenticação
    """
    return {"message": "Você acessou a rota de autenticação", "authenticated": False}

