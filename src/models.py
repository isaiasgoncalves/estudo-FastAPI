from sqlalchemy import create_engine, Column, Integer, String, Boolean, Float, ForeignKey
from sqlalchemy.orm import declarative_base
from sqlalchemy_utils.types import ChoiceType

# Cria a conexão com o BD
db = create_engine("sqlite:///base_de_dados.db")

# Cria a base do BD
Base = declarative_base()

# Cria as classes e tabelas co banco

class Usuario(Base):
    __tablename__ = "usuario"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    nome = Column("nome", String)
    email = Column("email", String, nullable=False)
    senha = Column("senha", String(128))
    ativo = Column("ativo", Boolean)
    admin = Column("admin", Boolean, default=False)

    def __init__(self, nome:str, email:str, senha:str, ativo:bool, admin=False):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.ativo = ativo
        self.admin = admin


class Pedido(Base):
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
        self.usuario = usuario
        self.preco = preco
        self.usuario = usuario
        self.preco = preco
        self.status = status



class ItemPedido(Base):
    __tablename__ = "item_pedido"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    quantidade = Column("quantidade", Integer, nullable=False)
    sabor = Column("sabor", String)
    tamanho = Column("tamanho", String)
    preco_unitario = Column("preco_unitario", Float)
    pedido = Column("pedido", ForeignKey("pedido.id"), nullable=False)

    def __init__(self, sabor, tamanho, quantidade, pedido, preco_unitario):
        self.sabor = sabor
        self.tamanho = tamanho
        self.quantidade = quantidade
        self.pedido = pedido
        self.preco_unitario = preco_unitario



# Executa a criação de metadados do banco

