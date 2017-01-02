import csv

from PySide.QtGui import QMessageBox

from bin.db.session import Session
from bin.db.comissao import Comissao


def marcar_comissoes_pago(data_limite, vendedores=True):
    session = Session()
    query = session.query(Comissao)\
        .filter(Comissao.status_pagamento == 0)\
        .filter(Comissao.data_pagamento <= data_limite)
    if vendedores:
        query = query.filter(Comissao.cod_vendedor != '002')
    else:
        query = query.filter(Comissao.cod_vendedor == '002')
    r = query.update({Comissao.status_pagamento: 1})
    session.commit()
    session.close()


def gerar_relatorio():
    session = Session()
    result = session.execute("""SELECT PedidoTeflon.CodLoja, SUM(PedidoTeflon.Valor) FROM PedidoTeflon
                    INNER JOIN Comissao
                    ON PedidoTeflon.CodPedido = Comissao.CodPedidoTeflon
                    WHERE Comissao.CodVendedor = '002'
                    AND Comissao.StatusPagamento = 0
                    GROUP BY PedidoTeflon.CodLoja""")
    with open('relatorio_vendas.csv', 'w', newline='') as file:
        wr = csv.writer(file, quoting=csv.QUOTE_ALL)
        for line in result:
            wr.writerow(line)
    QMessageBox.information(None, "Sucesso", "Relatório gerado na pasta texguard")



