"""
Este módulo define dependências comuns usadas em toda a aplicação FastAPI,
como gerenciamento de sessão de banco de dados.
"""

from sqlalchemy.orm import sessionmaker
from .models import db


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