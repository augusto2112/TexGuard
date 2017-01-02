
from PySide.QtGui import *

from bin.ui.mainWindowWidget_ui import Ui_MainWindow

from bin.scripts.atualizarComissoes import gerar_relatorio

from bin.widget.aplicacaoWidget import AplicacaoWidget
from bin.widget.cadastroClienteWidget import CadastroClienteDialog
from bin.widget.cadastroPedidoAtreladoWidget import CadastroPedidoAtreladoWidget
from bin.widget.clienteWidget import ClienteWidget
from bin.widget.comissaoWidget import ComissaoWidget
from bin.widget.enderecoWidget import EnderecoWidget
from bin.widget.impressaoDialog import SelecaoImpressao
from bin.widget.pagamentoWidget import PagamentoWidget
from bin.widget.pedidoDetalheWidget import PedidoDetalhe
from bin.widget.pedidoPLWidget import PedidoPLWidget
from bin.widget.pedidoTeflonWidget import PedidoTeflonWidget
from bin.widget.produtoWidget import ProdutoWidget
from bin.widget.cadastroPedidoIndependenteWidget import CadastroPedidoIndependenteWidget
from bin.widget.comissao_pago import ComissaoPagoDialog


class MainWindow(Ui_MainWindow, QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.ui = self.setupUi(self)

        self.action_widget_dic = {
            self.actionAplicacoes: AplicacaoWidget,
            self.actionCadastroVendaAtrelada: CadastroPedidoAtreladoWidget,
            self.actionClientes: ClienteWidget,
            self.actionComissoes: ComissaoWidget,
            self.actionEnderecos: EnderecoWidget,
            self.actionImprimirComissoes: SelecaoImpressao,
            self.actionPagamentos: PagamentoWidget,
            self.actionPedidoPrimaLineaDetalhe: PedidoDetalhe,
            self.actionPedidoPrimaLinea: PedidoPLWidget,
            self.actionPedidoTeflon: PedidoTeflonWidget,
            self.actionProdutos: ProdutoWidget,
            self.actionCadastroCliente: CadastroClienteDialog,
            self.actionCadastroVendaIndependente: CadastroPedidoIndependenteWidget,
            self.actionMarcarComoPagas: ComissaoPagoDialog
        }

        for action in self.action_widget_dic.keys():
            action.triggered.connect(self.abrir_widget)
        self.dialogs = []
        self.actionGerarRelatorioDeVendas.triggered.connect(gerar_relatorio)

    def abrir_widget(self):
        WidgetClass = self.action_widget_dic[self.sender()]
        widget = WidgetClass()
        if isinstance(widget, QDialog):
            self.dialog = widget
            widget.setModal(False)
            widget.show()
        elif isinstance(widget, QWidget):
            self.setCentralWidget(widget)


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    dialog = MainWindow()
    dialog.showMaximized()
    sys.exit(app.exec_())
