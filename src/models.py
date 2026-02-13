"""
Este módulo define os modelos SQLAlchemy para o banco de dados da aplicação,
incluindo Usuário, Pedido e ItemPedido. Ele também configura a conexão com o banco de dados.
"""

from sqlalchemy import create_engine, Column, Integer, String, Boolean, Float, ForeignKey
from sqlalchemy.orm import declarative_base
from sqlalchemy_utils.types import ChoiceType

# Cria a conexão com o BD
db = create_engine("sqlite:///base_de_dados.db")

# Cria a base do BD
Base = declarative_base()

# Cria as classes e tabelas co banco

class Usuario(Base):
    """
    Representa um usuário no sistema.

    Atributos:
        id (int): Chave primária, ID do usuário auto-incrementável.
        nome (str): O nome do usuário.
        email (str): O endereço de e-mail único do usuário.
        senha (str): A senha hash do usuário (128 bits).
        ativo (bool): Indica se a conta do usuário está ativa.
        admin (bool): Indica se o usuário possui privilégios de administrador.
    """
    __tablename__ = "usuario"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    nome = Column("nome", String)
    email = Column("email", String, nullable=False)
    senha = Column("senha", String(128))
    ativo = Column("ativo", Boolean)
    admin = Column("admin", Boolean, default=False)

    def __init__(self, nome:str, email:str, senha:str, ativo:bool, admin=False):
        """
        Inicializa um novo objeto Usuario.

        Args:
            nome (str): O nome do usuário.
            email (str): O endereço de e-mail único do usuário.
            senha (str): A senha hash do usuário.
            ativo (bool): Indica se a conta do usuário está ativa.
            admin (bool, optional): Indica se o usuário possui privilégios de administrador. Padrão para False.
        """
        self.nome = nome
        self.email = email
        self.senha = senha
        self.ativo = ativo
        self.admin = admin


class Pedido(Base):
    """
    Representa um pedido feito por um usuário.

    Atributos:
        id (int): Chave primária, ID do pedido auto-incrementável.
        status (str): O status atual do pedido (por exemplo, "PENDING", "CANCELED", "FINISHED").
        usuario (int): Chave estrangeira para o usuário que fez o pedido.
        preco (float): O preço total do pedido.
    """
    __tablename__ = "pedido"

    ORDER_STATUS = (
        ("PENDING", "Pendente"),
        ("CANCELED", "Cancelado"),
        ("FINISHED", "Finalizado")
    )

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    status = Column("status", String, nullable=False, default="PENDING")
    usuario = Column("usuario", ForeignKey("usuario.id"), nullable=False)
    preco = Column("preco", Float, nullable=False)
    # items =

    def __init__(self, usuario:int, preco:float = 0, status="PENDING"):
        """
        Inicializa um novo objeto Pedido.

        Args:
            usuario (int): O ID do usuário que fez o pedido.
            preco (float, optional): O preço total do pedido. Padrão para 0.
            status (str, optional): O status inicial do pedido. Padrão para "PENDING".
        """
        self.usuario = usuario
        self.preco = preco
        self.usuario = usuario
        self.preco = preco
        self.status = status



class ItemPedido(Base):
    """
    Representa um item dentro de um pedido.

    Atributos:
        id (int): Chave primária, ID do item de pedido auto-incrementável.
        quantidade (int): A quantidade do item.
        sabor (str): O sabor/tipo do item.
        tamanho (str): O tamanho do item.
        preco_unitario (float): O preço unitário do item.
        pedido (int): Chave estrangeira para o pedido ao qual este item pertence.
    """
    __tablename__ = "item_pedido"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    quantidade = Column("quantidade", Integer, nullable=False)
    sabor = Column("sabor", String)
    tamanho = Column("tamanho", String)
    preco_unitario = Column("preco_unitario", Float)
    pedido = Column("pedido", ForeignKey("pedido.id"), nullable=False)

    def __init__(self, sabor, tamanho, quantidade, pedido, preco_unitario):
        """
        Inicializa um novo objeto ItemPedido.

        Args:
            sabor (str): O sabor/tipo do item.
            tamanho (str): O tamanho do item.
            quantidade (int): A quantidade do item.
            pedido (int): O ID do pedido ao qual este item pertence.
            preco_unitario (float): O preço unitário do item.
        """
        self.sabor = sabor
        self.tamanho = tamanho
        self.quantidade = quantidade
        self.pedido = pedido
        self.preco_unitario = preco_unitario



