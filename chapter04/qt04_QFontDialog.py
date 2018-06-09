#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Junki
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class FontDialogDemo(QWidget):
    def __init__(self, parent=None):
        super(FontDialogDemo, self).__init__(parent)
        self.setWindowTitle('FontDialog例子')

        layout = QVBoxLayout()
        self.fontbtn = QPushButton('choose font')
        self.fontbtn.clicked.connect(self.getFont)
        layout.addWidget(self.fontbtn)
        self.fontlb1 = QLabel('Hello,测试字体样式')
        layout.addWidget(self.fontlb1)
        self.setLayout(layout)

    def getFont(self):
        font, ok = QFontDialog.getFont()
        if ok:
            self.fontlb1.setFont(font)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = FontDialogDemo()
    win.show()
    sys.exit(app.exec_())
