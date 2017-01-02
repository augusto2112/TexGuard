
from sqlalchemy import Column, Integer, Date, Float, ForeignKey
from sqlalchemy.orm import relationship

from .base import Base


class Pagamento(Base):
    __tablename__ = 'Pagamento'

    cod_pagamento = Column('CodPagamento', Integer, primary_key=True, autoincrement=True)
    cod_pedido_teflon = Column('CodPedidoTeflon', Integer, ForeignKey('PedidoTeflon.CodPedido'),
                               nullable=False)
    pedido_teflon = relationship('PedidoTeflon', backref="pagamentos")
    cod_condicao_pagamento = Column('CodCondicaoPagamento',
                                    Integer, ForeignKey('CondicaoPagamento.CodCondicaoPagamento'))
    condicao_pagamento = relationship("CondicaoPagamento", backref="pagamentos")
    valor = Column('Valor', Float, nullable=False)
    vencimento = Column('Vencimento', Date, nullable=False)
    pago = Column('Pago', Integer, nullable=False, default=0)
    data_pago = Column('DataPago', Date)
    conferido = Column("Conferido", Integer, nullable=False, default=0)

    def get_formatted_pago(self):
        if self.pago == 0:
            return "Não pago"
        elif self.pago == 1:
            return "Pago"
        else:
            return "Erro"

    def get_formatted_data_pago(self):
        if self.data_pago:
            return self.data_pago.strftime("%d/%m/%y")
        else:
            return "Não Pago"

    def get_formatted_conferido(self):
        if self.conferido == 0:
            return "Não conferido"
        elif self.conferido == 1:
            return "Conferido"
        else:
            return "Erro"