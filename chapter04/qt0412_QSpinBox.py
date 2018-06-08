#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Junki
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class spindemo(QWidget):
    def __init__(self, parent=None):
        super(spindemo, self).__init__(parent)
        self.setWindowTitle('SpinBox例子')
        self.resize(300, 100)

        layout = QVBoxLayout()
        self.lb1 = QLabel('current value:')
        self.lb1.setAlignment(Qt.AlignCenter)
        self.sp = QSpinBox()
        layout.addWidget(self.lb1)
        layout.addWidget(self.sp)
        self.sp.valueChanged.connect(self.valuechange)
        self.setLayout(layout)

    def valuechange(self):
        self.lb1.setText('current value:' + str(self.sp.value()))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = spindemo()
    win.show()
    sys.exit(app.exec_())
