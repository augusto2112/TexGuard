
from sqlalchemy import Column, Integer, String, Date, Float, ForeignKey
from sqlalchemy.orm import relationship

from bin.db.base import Base


class Comissao(Base):
    __tablename__ = 'Comissao'
    cod_comissao = Column('CodComissao', Integer, primary_key=True, autoincrement=True)
    cod_vendedor = Column('CodVendedor', String(3),
                          ForeignKey('Vendedor.CodVendedor'))
    vendedor = relationship("Vendedor", backref="comissoes")

    cod_pedido_teflon = Column('CodPedidoTeflon', Integer,
                               ForeignKey('PedidoTeflon.CodPedido'))
    pedido_teflon = relationship('PedidoTeflon', backref="comissoes")

    valor = Column('Valor', Float, nullable=False)
    data_pagamento = Column('DataPagamento', Date, nullable=False)
    status_pagamento = Column('StatusPagamento', Integer, nullable=False)










