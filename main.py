

def main():
    from PySide.QtGui import QApplication
    import bin.widget.mainWindowWidget
    import sys
    app = QApplication(sys.argv)
    mainWindow = bin.widget.mainWindowWidget.MainWindow()
    mainWindow.showMaximized()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()