#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Junki
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class Combo(QComboBox):  # 将一个普通的下拉按钮转化成可以放置拖曳文件的目标控件下拉按钮
    def __init__(self, title, parent):
        super(Combo, self).__init__(parent)
        self.setAcceptDrops(True)

    def dragEnterEvent(self, e):
        print(e)
        if e.mimeData().hasText():
            e.accept()
        else:
            e.ignore()

    def dropEvent(self, e):
        self.addItem(e.mimeData().text())

class Example(QWidget):  # 写主界面
    def __init__(self):
        super(Example, self).__init__()
        # self.initUI()

    # def initUI(self):
        lo = QFormLayout()
        lo.addRow(QLabel('请把左边的文本拖曳到右边的下拉菜单中'))
        edit = QLineEdit()
        edit.setDragEnabled(True)
        com = Combo('Button', self)
        lo.addRow(edit, com)
        self.setLayout(lo)
        self.setWindowTitle('简单的拖曳例子')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Example()
    win.show()
    sys.exit(app.exec_())
