#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Junki
import sys
from PyQt5.QtWidgets import QWidget, QToolTip, QApplication
from PyQt5.QtGui import QFont


class WinForm(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        QToolTip.setFont(QFont('黑体', 10))
        self.setToolTip('这是一个<b>气泡提示</b>')
        self.setWindowTitle('气泡提示demo')
        self.setGeometry(200, 300, 400, 400)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    winform = WinForm()
    winform.show()
    sys.exit(app.exec_())
