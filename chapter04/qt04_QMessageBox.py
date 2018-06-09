#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Junki
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class messageboxDemo(QWidget):
    def __init__(self, parent=None):
        super(messageboxDemo, self).__init__(parent)
        self.setWindowTitle('QMessageBox例子')
        self.resize(300, 100)
        self.btn = QPushButton(self)
        self.btn.setText('点击弹出消息框')
        self.btn.move(100, 30)
        self.btn.clicked.connect(self.msg)

    def msg(self):
        reply = QMessageBox.information(self, '标题', '对话框消息正文', QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        print(reply)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = messageboxDemo()
    win.show()
    sys.exit(app.exec_())
