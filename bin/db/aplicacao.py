
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from .base import Base


class Aplicacao(Base):
    __tablename__ = 'Aplicacao'

    cod_aplicacao = Column('CodAplicacao', Integer, primary_key=True, autoincrement=True)
    cod_pedido_teflon = Column('CodPedidoTeflon', Integer, ForeignKey('PedidoTeflon.CodPedido'), nullable=False)
    pedido_teflon = relationship('PedidoTeflon', backref='aplicacoes')
    cod_produto = Column('CodProduto', Integer, ForeignKey('Produto.CodProduto'))
    produto = relationship('Produto', backref='aplicacoes')
    quantidade_produto = Column('QuantidadeProduto', Integer, nullable=False)

    def __repr__(self):
        return "Aplicacao cod_aplicacao={0}, cod_pedido_teflon={1}, cod_produto={2}, quantidade_produto={3}".format(
            self.cod_aplicacao, self.cod_pedido_teflon, self.cod_produto, self.quantidade_produto
        )
