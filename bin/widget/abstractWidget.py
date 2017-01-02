from PySide.QtGui import *


class AbstractWidget(QWidget):
    def set_proxy_model(self):
        self.tableView.setSortingEnabled(True)
        self.model = QSortFilterProxyModel()
        self.tableView.setModel(self.model)

    def set_table_view(self, table_view_class):
        self.layout().removeWidget(self.tableView)
        self.tableView.close()
        self.tableView = table_view_class()
        self.layout().addWidget(self.tableView)
        self.set_proxy_model()

    def set_checkboxes_unchecked(self):
        for subwidget in self.children():
            if type(subwidget) is QCheckBox:
                subwidget.setChecked(False)