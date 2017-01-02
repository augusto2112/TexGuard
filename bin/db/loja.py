
from sqlalchemy import Column, String

from bin.db.base import Base


class Loja(Base):
    __tablename__ = 'Loja'

    cod_loja = Column('CodLoja', String(2), primary_key=True)
    uf = Column("UF", String(3), nullable=False)

    def __repr__(self):
        return "<Loja:(cod_loja={}, vendedores={}>".format(self.cod_loja, self.vendedores)