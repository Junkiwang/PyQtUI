#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Junki
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class ComboboxDemo(QWidget):
    def __init__(self, parent=None):
        super(ComboboxDemo, self).__init__(parent)
        self.setWindowTitle('Combobox例子')
        self.resize(300, 90)
        layout = QVBoxLayout()
        self.lb1 = QLabel('')

        self.cb = QComboBox()
        self.cb.addItem('C')
        self.cb.addItem('C++')
        self.cb.addItems(['C#', 'Java', 'Html', 'Python'])
        self.cb.currentIndexChanged.connect(self.selectionchange)
        layout.addWidget(self.cb)
        layout.addWidget(self.lb1)
        self.setLayout(layout)

    def selectionchange(self, i):
        self.lb1.setText(self.cb.currentText())
        print('Items in the list are:')
        for count in range(self.cb.count()):
            print('item' + str(count) + '=' + self.cb.itemText(count))
        print('Current index', i, 'selection changed', self.cb.currentText())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = ComboboxDemo()
    win.show()
    sys.exit(app.exec_())
