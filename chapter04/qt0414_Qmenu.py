#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Junki
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class MenuDemo(QMainWindow):
    def __init__(self, parent=None):
        super(MenuDemo, self).__init__(parent)
        # layout = QHBoxLayout()
        self.statusBar()
        bar = self.menuBar()
        file = bar.addMenu('File')
        tool = bar.addMenu('Tool')


        file.addAction('New')

        save = QAction('Save', self)
        save.setShortcut('Ctrl+S')
        file.addAction(save)
        save.setStatusTip('还没写')

        edit = file.addMenu('Edit')  # edit 不是动作，是菜单，子菜单中才是动作
        edit.addAction('copy')
        edit.addAction('paste')

        quit = QAction('Quit', self)
        file.addAction(quit)

        file.triggered[QAction].connect(self.processtrigger)
        # self.setLayout(layout)
        self.setWindowTitle('menu例子')

    def processtrigger(self, a):
        print(a.text()+ ' is triggered')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MenuDemo()
    win.show()
    sys.exit(app.exec_())
