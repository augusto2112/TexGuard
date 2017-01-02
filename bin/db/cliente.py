
from sqlalchemy import Column, String, Integer

from bin.db.base import Base


class Cliente(Base):
    __tablename__ = 'Cliente'

    cod_cliente = Column('CodCliente', Integer, primary_key=True, autoincrement=True)
    cod_cliente_pl = Column('CodClientePL', String(8))
    nome = Column('Nome', String(35), nullable=False)
    cpf = Column('CPF', String(20), nullable=False)
