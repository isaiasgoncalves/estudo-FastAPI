
from passlib.context import CryptContext
from dotenv import load_dotenv
from sqlalchemy.orm import Session
import os
from jose import jwt, JWTError
from datetime import datetime, timedelta, timezone
from fastapi.security import OAuth2PasswordBearer

from .models import Usuario

"""
Este módulo gerencia a autenticação de usuários, incluindo hash de senhas,
criação de tokens e verificação de usuários usando JWT (JSON Web Tokens).
Ele utiliza variáveis de ambiente para chaves secretas e configurações de expiração de token.
"""

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))

bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login-form")



def create_token(user_id: int, duration = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)):
    """
    Gera um token de acesso temporário (JWT) para um usuário com base no seu ID.

    Args:
        user_id (int): O ID do usuário para o qual o token está sendo criado.
        duration (timedelta, optional): A duração pela qual o token será válido.
                                        Padrão para ACCESS_TOKEN_EXPIRE_MINUTES.

    Returns:
        str: Uma string JWT codificada.
    """

    expire_datetime = datetime.now(timezone.utc) + duration
    info_dict = {"sub": str(user_id), "exp": expire_datetime}
    encoded_jwt = jwt.encode(info_dict, key=SECRET_KEY, algorithm=ALGORITHM)

    return encoded_jwt


def authenticate_user(email: str, password: str, session: Session):
    """
    Autentica um usuário verificando seu email e senha contra o banco de dados.

    Args:
        email (str): O email do usuário tentando autenticar.
        password (str): A senha em texto puro fornecida pelo usuário.
        session (Session): A sessão do banco de dados SQLAlchemy.

    Returns:
        Usuario ou False: O objeto Usuario autenticado se as credenciais forem válidas,
                          caso contrário, False.
    """
    user = session.query(Usuario).filter(Usuario.email == email).first()
    if not user:
        return False
    elif not bcrypt_context.verify(password, user.senha):
        return False
    else:
        return user

