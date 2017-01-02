
from sqlalchemy import Column, Integer, String, Date, Float, ForeignKey
from sqlalchemy.orm import relationship

from bin.db.base import Base


class PedidoPrimaLinea(Base):
    __tablename__ = 'PedidoPL'

    cod_pedido = Column('CodPedido', String(8), primary_key=True)

    cod_loja = Column('CodLoja', String(2), ForeignKey('Loja.CodLoja'))
    loja = relationship("Loja", backref="pedidos")
    cod_cliente_pl = Column('CodClientePL', String(8), ForeignKey('Cliente.CodClientePL'), nullable=False)
    cliente = relationship("Cliente", backref="pedidos")
    cod_endereco = Column('CodEndereco', Integer, ForeignKey('Endereco.CodEndereco'), nullable=False)
    endereco = relationship("Endereco", backref="pedidos")
    cod_vendedor = Column('CodVendedor', String(3),
                          ForeignKey('Vendedor.CodVendedor'))
    vendedor = relationship("Vendedor", backref="pedidos")

    data_pedido = Column('DataPedido', Date, nullable=False)
    valor_produtos = Column('ValorProdutos', Float, nullable=False)
    valor_credito_troca = Column('ValorCreditoTroca', Float, nullable=False)
    valor_total_pedido = Column('ValorTotalDoPedido', Float, nullable=False)
    situacao = Column('Situacao', String(1), nullable=False)

    def get_formatted_situacao(self):
        if self.situacao == "E":
            return "Entregue"
        elif self.situacao == "A":
            return "Aguardando"
        else:
            return "Indefinido"
