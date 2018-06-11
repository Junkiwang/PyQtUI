#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Junki
import sys, math
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class Drawing(QWidget):
    def __init__(self, parent=None):
        super(Drawing, self).__init__(parent)
        self.resize(300, 200)
        self.setWindowTitle('在窗口画点')

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.drawpoints(qp)
        qp.end()

    def drawpoints(self, qp):
        qp.setPen(Qt.red)
        size = self.size()
        for i in range(1000):
            x = 100 * (-1 + 2.0 * i / 1000) + size.width() / 2.0
            y = -50 * math.sin((x - size.width() / 2.0) * math.pi / 50) + size.height() / 2.0
            qp.drawPoint(x, y)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Drawing()
    win.show()
    sys.exit(app.exec_())
