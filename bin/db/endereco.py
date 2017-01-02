
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from .base import Base


class Endereco(Base):
    __tablename__ = 'Endereco'

    cod_endereco = Column('CodEndereco', Integer, primary_key=True)
    cod_cliente = Column('CodCliente', String(8), ForeignKey('Cliente.CodCliente'))
    cliente = relationship('Cliente', backref='enderecos')
    cep = Column('CEP', String(8), nullable=False)
    endereco = Column('Endereco', String(40), nullable=False)
    bairro = Column('Bairro', String(20), nullable=False)
    cidade = Column('Cidade', String(20), nullable=False)
    uf = Column('UF', String(2), nullable=False)
    fone = Column('Fone', String(15))
    fone2 = Column('Fone2', String(15))
    email = Column('Email', String(150))
    ponto_referencia_cliente = Column('PontoReferencia', String(40))