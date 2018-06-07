#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Junki

import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class RadioDemo(QWidget):
    def __init__(self, parent=None):
        super(RadioDemo, self).__init__(parent)
        self.setWindowTitle('RadioButton例子')
        layout = QHBoxLayout()
        self.btn1 = QRadioButton('Button1')
        self.btn1.setChecked(True)
        self.btn1.toggled.connect(lambda: self.btnstate(self.btn1))
        layout.addWidget(self.btn1)

        self.btn2 = QRadioButton('Button2')
        self.btn2.toggled.connect(lambda: self.btnstate(self.btn2))
        layout.addWidget(self.btn2)
        self.setLayout(layout)

    def btnstate(self, btn):
        if btn.text() == 'Button1':
            if btn.isChecked() == True:
                print(btn.text() + 'is selected')
            else:
                print(btn.text() + 'is deselected')
        if btn.text() == 'Button2':
            if btn.isChecked() == True:
                print(btn.text() + 'is selected')
            else:
                print(btn.text() + 'is deselected')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = RadioDemo()
    win.show()
    sys.exit(app.exec_())
