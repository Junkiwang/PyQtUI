#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Junki
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
class SliderDemo(QWidget):
    def __init__(self, parent=None):
        super(SliderDemo, self).__init__(parent)
        self.setWindowTitle('QSlider例子')
        self.resize(300, 100)

        layout = QVBoxLayout()
        self.lb1 = QLabel('Hello PyQt5')
        self.lb1.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.lb1)

        self.s1 = QSlider(Qt.Horizontal)
        self.s1.setMinimum(10)
        self.s1.setMaximum(50)
        self.s1.setSingleStep(3)
        self.s1.setValue(20)
        self.s1.setTickPosition(QSlider.TicksBothSides)
        self.s1.setTickInterval(5)
        layout.addWidget(self.s1)
        self.s1.valueChanged.connect(self.valuechange)
        self.setLayout(layout)

    def valuechange(self):
        print('current slider value=%s' % self.s1.value())
        size = self.s1.value()
        self.lb1.setFont(QFont('Arial', size))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = SliderDemo()
    win.show()
    sys.exit(app.exec_())
