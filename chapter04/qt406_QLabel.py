#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Junki

from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QPalette
import sys


class WindowDemo(QWidget):
    def __init__(self):
        super().__init__()
        label1 = QLabel(self)
        label2 = QLabel(self)
        label3 = QLabel(self)
        label4 = QLabel(self)

        label1.setText('这是一个文本标签')
        label1.setAutoFillBackground(True)
        palette = QPalette()
        palette.setColor(QPalette.Window, Qt.blue)
        label1.setPalette(palette)
        label1.setAlignment(Qt.AlignCenter)
        label2.setText('<a href="#">欢迎使用Python GUI应用</a>')
        label3.setAlignment(Qt.AlignCenter)
        label3.setToolTip('这是一个图片标签')
        label3.setPixmap(QPixmap('./images/python.jpg'))
        label4.setText('<a href="http://www.cnblogs.com/wangshuo1/">欢迎访问信平的小屋</a>')
        label4.setAlignment(Qt.AlignRight)

        vbox = QVBoxLayout()
        vbox.addWidget(label1)
        vbox.addStretch()
        vbox.addWidget(label2)
        vbox.addStretch()
        vbox.addWidget(label3)
        vbox.addStretch()
        vbox.addWidget(label4)

        label1.setOpenExternalLinks(True)
        label4.setOpenExternalLinks(False)
        label4.linkActivated.connect(self.link_clicked)
        label2.linkHovered.connect(self.link_hovered)
        label1.setTextInteractionFlags(Qt.TextSelectableByMouse)
        self.setLayout(vbox)
        self.setWindowTitle('QLabel例子')

    def link_clicked(self):
        print('当鼠标点击label4标签时，触发事件')

    def link_hovered(self):
        print('当鼠标滑过label2标签时，触发事件')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = WindowDemo()
    win.show()
    sys.exit(app.exec_())
