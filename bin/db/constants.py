

import bin.db.loja
import bin.db.vendedor
import bin.db.condicao_pagamento

from bin.db.session import Session


def load_constants():
    global LOJAS, VENDEDORES, VENDEDORES_DIC, GERENTES
    global GERENTES_DIC, CONDICOES_PAGAMENTO, CONDICOES_PAGAMENTO_DIC
    global LOJA_GERENTES
    session = Session()
    LOJAS = sorted([_[0] for _ in session.query(bin.db.loja.Loja.cod_loja).all()])
    VENDEDORES_DIC = {vendedor.nome_vendedor: vendedor.cod_vendedor
                      for vendedor in session.query(bin.db.vendedor.Vendedor)
                        .filter(bin.db.vendedor.Vendedor.ativo == 'S').all()}
    VENDEDORES = sorted(VENDEDORES_DIC.keys())
    gerentes = session.query(bin.db.vendedor.Vendedor).filter(bin.db.vendedor.Vendedor.tipo_vendedor == 1)\
                        .filter(bin.db.vendedor.Vendedor.ativo == 'S').all()
    GERENTES_DIC = {gerente.nome_vendedor: gerente.cod_vendedor for gerente in gerentes}
    GERENTES = sorted(GERENTES_DIC.keys())
    LOJA_GERENTES = {gerente.cod_loja: gerente.nome_vendedor for gerente in gerentes}
    session.close()


def get_lojas():
    global LOJAS
    if not LOJAS:
        load_constants()
    return LOJAS


def get_vendedores():
    global VENDEDORES
    if not VENDEDORES:
        load_constants()
    return VENDEDORES


def get_vendedores_dic():
    global VENDEDORES_DIC
    if not VENDEDORES_DIC:
        load_constants()
    return VENDEDORES_DIC


def get_gerentes():
    global GERENTES
    if not GERENTES:
        load_constants()
    return GERENTES


def get_gerentes_dic():
    global GERENTES_DIC
    if not GERENTES_DIC:
        load_constants()
    return GERENTES_DIC


def get_loja_gerentes():
    global LOJA_GERENTES
    if not LOJA_GERENTES:
        load_constants()
    return LOJA_GERENTES


def get_condicoes_pagamento():
    global GERENTES_DIC
    if not GERENTES_DIC:
        load_constants()
    return GERENTES_DIC


def get_condicoes_pagamento_dic():
    global CONDICOES_PAGAMENTO_DIC
    if not CONDICOES_PAGAMENTO_DIC:
        load_constants()
    return CONDICOES_PAGAMENTO_DIC


LOJAS = None
VENDEDORES = None
GERENTES = None
VENDEDORES_DIC = None
GERENTES_DIC = None
CONDICOES_PAGAMENTO = None
CONDICOES_PAGAMENTO_DIC = None
LOJA_GERENTES = None

if __name__ == '__main__':
    load_constants()