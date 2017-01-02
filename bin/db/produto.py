
from sqlalchemy import Column, Integer, String, Date, Float, ForeignKey
from sqlalchemy.orm import relationship

from .base import Base


class Produto(Base):
    __tablename__ = 'Produto'

    cod_produto = Column('CodProduto', Integer, primary_key=True, autoincrement=True)

    cod_pedido = Column('CodPedidoPL', String(8), ForeignKey('PedidoPL.CodPedido'), nullable=False)
    pedido_pl = relationship("PedidoPrimaLinea", backref="produtos")

    num_item = Column('NumItem', Integer, primary_key=True)
    cod_produto_pl = Column('CodProdutoPL', String(4), nullable=False)
    cod_complemento = Column('CodComplemento', String(15), nullable=False)
    cod_acabamento = Column('CodAcabamento', String(8), nullable=False)
    desc_produto = Column('DescProduto', String(40), nullable=False)
    mostruario = Column('Mostruario', String(3), nullable=False)
    quantidade_pedido = Column('QtdPedido', Integer, nullable=False)
    preco_unitario_cheio = Column('PrecoUnitarioCheio', Float, nullable=False)
    preco_proporcional = Column('PrecoProporcional', Float, nullable=False)
    data_entrega_primaria = Column('DataEntrega1', Date, nullable=False)
    data_entrega_secundaria = Column('DataEntrega2', Date, nullable=False)
    situacao = Column('Situacao', String(1), nullable=False)
    tem_teflon = Column('TemTeflon', String(1), nullable=False)
    vendeu_teflon = Column('VendeuTeflon', String(1), nullable=True)

    def get_formatted_situacao(self):
        if self.situacao == "E":
            return "Entregue"
        elif self.situacao == "A":
            return "Aguardando"
        else:
            return "Indefinido"

    def get_formatted_vendeu_teflon(self):
        if self.vendeu_teflon == 'S':
            return "Sim"
        elif self.vendeu_teflon == 'N':
            return "Não"
        else:
            return "Indefinido"