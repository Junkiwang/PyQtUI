# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QFileDialog
from MainForm import Ui_MainWindow


class CallMainForm(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(CallMainForm, self).__init__()
        self.setupUi(self)
        self.fileCloseAction.triggered.connect(self.close)
        self.fileOpenAction.triggered.connect(self.openMsg)

    def openMsg(self):
        file, ok = QFileDialog.getOpenFileName(self, '打开', 'C:/', 'All Files (*);;Text Files (*.txt)')
        self.statusbar.showMessage(file)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = CallMainForm()
    win.show()
    sys.exit(app.exec_())
