
from bin.db.aplicacao import Aplicacao
from bin.db.cliente import Cliente
from bin.db.comissao import Comissao
from bin.db.condicao_pagamento import CondicaoPagamento
from bin.db.endereco import Endereco
from bin.db.loja import Loja
from bin.db.pagamento import Pagamento
from bin.db.pedido_prima_linea import PedidoPrimaLinea
from bin.db.pedido_teflon import PedidoTeflon
from bin.db.produto import Produto
from bin.db.vendedor import Vendedor
from bin.db.session import Session

session = Session()

session.query(Aplicacao).all()
session.query(Cliente).all()
session.query(Comissao).all()
session.query(CondicaoPagamento).all()
session.query(Endereco).all()
session.query(Loja).all()
session.query(Pagamento).all()
session.query(PedidoPrimaLinea).all()
session.query(PedidoTeflon).all()
session.query(Produto).all()
session.query(Vendedor).all()
session.close()

# print(session.query(Comissao).all())