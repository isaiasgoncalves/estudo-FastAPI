"""
Este módulo define dependências comuns usadas em toda a aplicação FastAPI,
como gerenciamento de sessão de banco de dados.
"""

from fastapi import Depends, HTTPException
from sqlalchemy.orm import sessionmaker, Session
from jose import jwt, JWTError
from starlette import status

from .models import db, Usuario
from .authentication import SECRET_KEY, ALGORITHM, oauth2_scheme


def make_session():
    """
    Dependência que fornece uma sessão de banco de dados SQLAlchemy.

    Esta é uma função geradora que rende uma sessão e garante que ela seja
    fechada após a conclusão da requisição.

    Yields:
        Session: Uma sessão de banco de dados SQLAlchemy.
    """

    try:
        Session = sessionmaker(bind=db)
        session = Session()
        yield session
    finally:
        session.close()



def verify_token(token: str = Depends(oauth2_scheme), session: Session = Depends(make_session)):
    """
    Verifica um token JWT e extrai o usuário associado a ele.

    Args:
        token (str): O token JWT a ser verificado.
        session (Session, optional): A sessão do banco de dados SQLAlchemy. Padrão para Depends(make_session).

    Returns:
        Usuario: O objeto Usuario ass ociado ao token verificado.
    """

    try:
        info_dict = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        id_user = int(info_dict['sub'])
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Acesso Negado, verifique a validade do token"
        )

    user = session.query(Usuario).filter(Usuario.id == id_user).first()
    if not user:
        raise HTTPException(status_code=401, detail="Usuário Inválido")

    return user