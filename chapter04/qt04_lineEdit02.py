#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Junki
from PyQt5.QtWidgets import QApplication, QLineEdit, QWidget, QFormLayout
from PyQt5.QtGui import QIntValidator, QDoubleValidator, QRegExpValidator
from PyQt5.QtCore import QRegExp
import sys


class lineEditDemo(QWidget):
    def __init__(self, parent=None):
        super(lineEditDemo, self).__init__(parent)
        self.setWindowTitle('QLineEdit例子')

        flo = QFormLayout()
        pIntlineEdit = QLineEdit()
        pDoublelineEdit = QLineEdit()
        pValidatorlineEdit = QLineEdit()

        flo.addRow('整型', pIntlineEdit)
        flo.addRow('浮点型', pDoublelineEdit)
        flo.addRow('字母和数字', pValidatorlineEdit)

        pIntlineEdit.setPlaceholderText('整型')
        pDoublelineEdit.setPlaceholderText('浮点型')
        pValidatorlineEdit.setPlaceholderText('字母和数字')

        pIntValidator = QIntValidator(self)
        pIntValidator.setRange(0, 99)

        pDoubleValidator = QDoubleValidator(self)
        pDoubleValidator.setRange(-360, 360)
        pDoubleValidator.setNotation(QDoubleValidator.StandardNotation) #分标准浮点记数和科学浮点记数
        pDoubleValidator.setDecimals(2)

        r = QRegExp('^[a-zA-Z0-9]+$')
        pReValidator = QRegExpValidator(self)
        pReValidator.setRegExp(r)

        pIntlineEdit.setValidator(pIntValidator)
        pDoublelineEdit.setValidator(pDoubleValidator)
        pValidatorlineEdit.setValidator(pReValidator)

        self.setLayout(flo)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = lineEditDemo()
    win.show()
    sys.exit(app.exec_())
