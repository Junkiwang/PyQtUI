#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Junki
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class DialogDemo(QWidget):
    def __init__(self, parent=None):
        super(DialogDemo, self).__init__(parent)
        self.setWindowTitle('Dialog例子')
        self.resize(350, 300)
        layout = QVBoxLayout()

        self.btn = QPushButton('弹出对话框')
        # self.btn.setText('弹出对话框')  # 用这个就不用layout布局管理了
        layout.addWidget(self.btn)
        self.btn.move(50, 30)
        self.btn.clicked.connect(self.showdialog)
        self.setLayout(layout)

    def showdialog(self):
        dialog = QDialog()
        btn = QPushButton('ok', dialog)
        btn.move(50, 50)
        dialog.setWindowTitle('Dialog')
        dialog.setWindowModality(Qt.WindowModal)
        dialog.exec_()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = DialogDemo()
    win.show()
    sys.exit(app.exec_())
