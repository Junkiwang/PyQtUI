#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Junki
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class Drawing(QWidget):
    def __init__(self, parent=None):
        super(Drawing, self).__init__(parent)
        self.setWindowTitle('在窗口中绘制文字')
        self.resize(300, 200)
        self.text = '欢迎学习PyQt5'

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.begin(self)
        self.drawtext(event, painter)
        painter.end()

    def drawtext(self, event, qp):
        qp.setPen(QColor(168, 34, 3))
        qp.setFont(QFont('SimSun', 20))
        qp.drawText(event.rect(), Qt.AlignCenter, self.text)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Drawing()
    win.show()
    sys.exit(app.exec_())
