
from sqlalchemy import Column, Integer, String, Date, Float, ForeignKey
from sqlalchemy.orm import relationship

from .base import Base


class PedidoTeflon(Base):
    __tablename__ = 'PedidoTeflon'

    cod_pedido = Column('CodPedido', Integer, primary_key=True, autoincrement=True)
    cod_pedido_pl = Column('CodPedidoPL', String(8), ForeignKey('PedidoPL.CodPedido'))
    pedido_pl = relationship('PedidoPrimaLinea', backref='pedidos_teflon')
    cod_loja = Column('CodLoja', String(2), ForeignKey('Loja.CodLoja'))
    loja = relationship('Loja', backref='pedidos_teflon')
    cod_vendedor = Column('CodVendedor', String(3),
                          ForeignKey('Vendedor.CodVendedor'))
    vendedor = relationship("Vendedor", backref="pedidos_teflon")
    cod_cliente = Column('CodCliente', String(8), ForeignKey('Cliente.CodCliente'), nullable=False)
    cliente = relationship("Cliente", backref="pedidos_teflon")
    cod_endereco = Column('CodEndereco', Integer, ForeignKey('Endereco.CodEndereco'), nullable=False)
    endereco = relationship('Endereco', backref="pedido_teflon")
    valor = Column('Valor', Float, nullable=False)
    tipo_venda = Column('TipoVenda', Integer, nullable=False)
    data_pedido = Column('DataPedido', Date, nullable=False)
    data_cadastro = Column('DataCadastro', Date)

    def get_formatted_tipo_venda(self):
        if self.tipo_venda == 0:
            return "Não vendeu teflon"
        elif self.tipo_venda == 1:
            return "Vendeu na Loja"
        elif self.tipo_venda == 2:
            return "Cliente ligou e comprou"
        elif self.tipo_venda == 3:
            return "Vendeu no pós-venda"
        else:
            return "Indefinido"

    def get_formatted_cod_pedido_pl(self):
        return self.cod_pedido_pl or "Sem Pedido"

    def get_formatted_loja(self):
        return self.pedido_pl.cod_loja or "Sem Loja"