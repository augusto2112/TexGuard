
from sqlalchemy import Column, Integer, String, Float

from .base import Base


class CondicaoPagamento(Base):
    __tablename__ = 'CondicaoPagamento'

    cod_condicao_pagamento = Column('CodCondicaoPagamento', String(6), primary_key=True)
    descricao = Column('Descricao', String(40), nullable=False)
    parcelas = Column('Parcelas', Integer, nullable=False)
    dias_para_vencimento_primeira_parcela = Column('DiasParaVencimentoPrimeiraParcela', Integer, nullable=False)
    desconto = Column('Desconto', Float, nullable=False)
