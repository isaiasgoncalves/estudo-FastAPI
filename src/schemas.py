"""
Este módulo define esquemas Pydantic para validação e serialização de dados
dentro da aplicação FastAPI.
"""

from pydantic import BaseModel
from typing import Optional


class UserSchema(BaseModel):
    """
    Esquema Pydantic para validação de dados do usuário.

    Atributos:
        name (str): O nome do usuário.
        email (str): O endereço de e-mail único do usuário.
        password (str): A senha do usuário (será hashed).
        active (Optional[bool]): Indica se a conta do usuário está ativa.
        admin (Optional[bool]): Indica se o usuário possui privilégios de administrador.
    """
    name: str
    email: str
    password: str
    active: Optional[bool]
    admin: Optional[bool]

    class Config:
        from_attributes = True


class OrderSchema(BaseModel):
    """
    Esquema Pydantic para validação de dados de criação de pedido.

    Atributos:
        user_id (int): O ID do usuário que está fazendo o pedido.
    """
    user_id: int

    class Config:
        from_attributes = True


class LoginSchema(BaseModel):
    """
    Esquema Pydantic para validação de credenciais de login do usuário.

    Atributos:
        email (str): O endereço de e-mail do usuário.
        password (str): A senha em texto puro do usuário.
    """
    email: str
    password: str

    class Config:
        from_attributes = True