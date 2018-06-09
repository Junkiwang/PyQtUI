#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Junki
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class filedialogdemo(QWidget):
    def __init__(self, parent=None):
        super(filedialogdemo, self).__init__(parent)
        self.setWindowTitle('File Dialog 例子')

        layout = QVBoxLayout()
        self.btn = QPushButton('加载图片')
        self.btn.clicked.connect(self.getfile)
        layout.addWidget(self.btn)

        self.lb1 = QLabel('')
        layout.addWidget(self.lb1)

        self.btn1 = QPushButton('加载文本文件')
        self.btn1.clicked.connect(self.getfiles)
        layout.addWidget(self.btn1)

        self.contents = QTextEdit()
        layout.addWidget(self.contents)
        self.setLayout(layout)

    def getfile(self):
        fname, _ = QFileDialog.getOpenFileName(self, 'Open file', 'c:\\', 'Image files (*.jpg *.gif)')
        self.lb1.setPixmap(QPixmap(fname))

    def getfiles(self):
        dlg = QFileDialog()
        dlg.setFileMode(QFileDialog.AnyFile)
        dlg.setFilter(QDir.Files)  # 只显示过滤器允许的文件
        if dlg.exec_():  # 意思是执行模式对话框，如果对话框dlg被执行选择文件了，就会判断exec_()的返回值
            filenames = dlg.selectedFiles()
            print(filenames, filenames[0])
            f = open(filenames[0], 'r')  # filenames是一个list，如果只有一个文件时，就需要加[0]，保证能打开文件而不是打开list防止报错

            with f:
                data = f.read()
                self.contents.setText(data)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = filedialogdemo()
    win.show()
    sys.exit(app.exec_())
