"""Delimita as rotas de autenticação da API"""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from .models import Usuario
from .dependencies import make_session
from .authentication import bcrypt_context
from .schemas import UserSchema

# Delimitando as rotas de autenticação
auth_router = APIRouter(prefix="/auth", tags=["Autenticação"])

@auth_router.get("/", tags=["Autenticação"])
async def auth_main():
    """
    Rota padrão de autenticação do sistema. Todas as rotas precisam de autenticação
    """
    return {"message": "Você acessou a rota de autenticação", "authenticated": False}



@auth_router.post("/create-user")
async def create_user(user_schema: UserSchema, session : Session = Depends(make_session)):

    usuario = session.query(Usuario).filter(Usuario.email == user_schema.email).first()

    if usuario:
        raise HTTPException(status_code=400, detail="Já existe um usuário com este email")
    else:
        crypted_pwd = bcrypt_context.hash(user_schema.password)
        new_user = Usuario(nome=user_schema.name, email=user_schema.email, senha=crypted_pwd, ativo=user_schema.active, admin=user_schema.admin)
        session.add(new_user)
        session.commit()
        return {"message": f"Usuário com email {user_schema.email} foi cadastrado com sucesso"}


