#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Junki
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import*

class InputdialogDemo(QWidget):
    def __init__(self, parent=None):
        super(InputdialogDemo, self).__init__(parent)
        self.setWindowTitle('QInputDialog例子')
        layout = QFormLayout()
        self.btn1 = QPushButton('获得列表里的选项')
        self.btn1.clicked.connect(self.getItem)
        self.e1 = QLineEdit()
        layout.addRow(self.btn1, self.e1)

        self.btn2 = QPushButton('获得字符串')
        self.btn2.clicked.connect(self.getIext)
        self.e2 = QLineEdit()
        layout.addRow(self.btn2, self.e2)

        self.btn3 = QPushButton('获得整数')
        self.btn3.clicked.connect(self.getInt)
        self.e3 = QLineEdit()
        layout.addRow(self.btn3, self.e3)
        self.setLayout(layout)

    def getItem(self):
        items = ('C', 'C++', 'Java', 'Python')
        item, ok = QInputDialog.getItem(self, 'select input dialog', '语言列表', items, 0, False)
        if ok and item:
            self.e1.setText(str(item))

    def  getIext(self):
        text, ok = QInputDialog.getText(self, 'text input dialog', '输入姓名：')
        if ok:
            self.e2.setText(str(text))

    def getInt(self):
        num, ok = QInputDialog.getInt(self, 'integer input dialog', '输入数字')
        if ok:
            self.e3.setText(str(num))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = InputdialogDemo()
    win.show()
    sys.exit(app.exec_())
