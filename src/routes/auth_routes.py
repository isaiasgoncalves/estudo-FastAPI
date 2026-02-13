"""
Este módulo define as rotas de autenticação para a aplicação FastAPI,
incluindo funcionalidades de criação de usuário, login e atualização de token.
"""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import datetime, timedelta

from src.models import Usuario
from src.dependencies import make_session
from src.authentication import bcrypt_context, create_token, authenticate_user, verify_token
from src.schemas import UserSchema, LoginSchema

# Delimitando as rotas de autenticação
auth_router = APIRouter(prefix="/auth", tags=["Autenticação"])


@auth_router.get("/", tags=["Autenticação"])
async def auth_main():
    """
    Rota de autenticação padrão.

    Esta rota serve como um ponto de entrada básico para a seção de autenticação
    e tipicamente indica que autenticação adicional é necessária para outras rotas.

    Returns:
        dict: Uma mensagem indicando acesso à rota de autenticação e status de autenticação.
    """
    return {"message": "Você acessou a rota de autenticação", "authenticated": False}


@auth_router.post("/create-user")
async def create_user(user_schema: UserSchema, session : Session = Depends(make_session)):
    """
    Cria um novo usuário no sistema.

    Args:
        user_schema (UserSchema): Esquema Pydantic contendo os dados do novo usuário.
        session (Session): A dependência da sessão do banco de dados SQLAlchemy.

    Raises:
        HTTPException: Se um usuário com o e-mail fornecido já existir.

    Returns:
        dict: Uma mensagem indicando a criação bem-sucedida do usuário.
    """

    usuario = session.query(Usuario).filter(Usuario.email == user_schema.email).first()

    if usuario:
        raise HTTPException(status_code=400, detail="Já existe um usuário com este email")
    else:
        crypted_pwd = bcrypt_context.hash(user_schema.password)
        new_user = Usuario(nome=user_schema.name, email=user_schema.email, senha=crypted_pwd, ativo=user_schema.active, admin=user_schema.admin)
        session.add(new_user)
        session.commit()
        return {"message": f"Usuário com email {user_schema.email} foi cadastrado com sucesso"}


@auth_router.post("/login")
async def login(login_schema: LoginSchema, session: Session = Depends(make_session)):
    """
    Autentica um usuário e emite tokens de acesso e refresh.

    Args:
        login_schema (LoginSchema): Esquema Pydantic contendo as credenciais de login do usuário (e-mail e senha).
        session (Session): A dependência da sessão do banco de dados SQLAlchemy.

    Raises:
        HTTPException: Se a autenticação falhar devido a credenciais incorretas.

    Returns:
        dict: Um dicionário contendo o token de acesso, token de refresh e tipo de token.
    """

    user = authenticate_user(login_schema.email, login_schema.password, session)
    if not user:
        raise HTTPException(status_code=400, detail="Credenciais incorretas")
    else:
        access_token = create_token(user.id)
        refresh_token = create_token(user.id, duration=timedelta(days=7))
        return {"access_token": access_token,
                "refresh_token": refresh_token,
                "token_type": "Bearer"}


@auth_router.get("/refresh")
async def use_refresh_token(refresh_token: str):
    """
    Troca um token de refresh válido por um novo token de acesso.

    Args:
        refresh_token (str): O token de refresh fornecido ao usuário.

    Returns:
        dict: Um dicionário contendo o novo token de acesso e o tipo de token.
    """
    # Verificar o refresh_token
    user = verify_token(refresh_token)
    access_token = create_token(user.id)
    return {"access_token": access_token,
            "token_type": "Bearer"}

