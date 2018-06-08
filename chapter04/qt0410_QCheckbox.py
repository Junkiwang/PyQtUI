#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Junki
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtCore import Qt


class CheckBoxDemo(QWidget):
    def __init__(self, parent=None):
        super(CheckBoxDemo, self).__init__(parent)
        self.setWindowTitle('CheckBox例子')

        groupBox = QGroupBox('Checkboxes')
        groupBox.setFlat(True)

        layout = QHBoxLayout()
        self.checkbox1 = QCheckBox('&Checkbox1')
        self.checkbox1.setChecked(True)
        self.checkbox1.stateChanged.connect(lambda: self.checkboxstate(self.checkbox1))
        layout.addWidget(self.checkbox1)

        self.checkbox2 = QCheckBox('Checkbox2')
        self.checkbox2.toggled.connect(lambda: self.checkboxstate(self.checkbox2))
        layout.addWidget(self.checkbox2)

        self.checkbox3 = QCheckBox('Checkbox3')
        self.checkbox3.setTristate(True)
        self.checkbox3.setCheckState(Qt.PartiallyChecked)
        self.checkbox3.stateChanged.connect(lambda: self.checkboxstate(self.checkbox3))
        layout.addWidget(self.checkbox3)

        groupBox.setLayout(layout)
        mainlayout = QVBoxLayout()
        mainlayout.addWidget(groupBox)
        self.setLayout(mainlayout)

    def checkboxstate(self, checkbox):
        chk1state = self.checkbox1.text() + ', isChecked=' + str(self.checkbox1.isChecked()) + ', checkState=' + str(
            self.checkbox1.checkState()) + '\n'
        chk2state = self.checkbox2.text() + ', isChecked=' + str(self.checkbox2.isChecked()) + ', checkState=' + str(
            self.checkbox2.checkState()) + '\n'
        chk3state = self.checkbox3.text() + ', isChecked=' + str(self.checkbox3.isChecked()) + ', checkState=' + str(
            self.checkbox3.checkState()) + '\n'
        print(chk1state, chk2state, chk3state)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = CheckBoxDemo()
    win.show()
    sys.exit(app.exec_())
