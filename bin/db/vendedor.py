
from sqlalchemy import Column, String, Float, ForeignKey, Integer
from sqlalchemy.orm import relationship

from bin.db.base import Base


class Vendedor(Base):
    __tablename__ = 'Vendedor'

    cod_vendedor = Column('CodVendedor', String(3), primary_key=True)
    nome_vendedor = Column('NomeVendedor', String(40), nullable=False)
    cod_loja = Column('CodLoja', String(2), ForeignKey('Loja.CodLoja'))
    loja = relationship("Loja", backref="vendedores")
    percentual_comissao = Column('PercentualComissao', Float, nullable=False)
    ativo = Column('Ativo', String(1), nullable=False)
    tipo_vendedor = Column('TipoVendedor', Integer, nullable=False)