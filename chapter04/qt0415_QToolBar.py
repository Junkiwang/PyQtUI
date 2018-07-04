#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Junki

import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class ToolBarDemo(QMainWindow):
    def __init__(self, parent=None):
        super(ToolBarDemo, self).__init__(parent)
        self.setWindowTitle('ToolBar例子')
        self.resize(300, 200)

        # layout = QVBoxLayout()
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

        tb = self.addToolBar('File')
        new = QAction(QIcon('./images/new.png'), 'new', self)
        tb.addAction(new)

        open = QAction(QIcon('./images/open.png'), 'open', self)
        tb.addAction(open)

        save = QAction(QIcon('./images/save.png'), 'save', self)
        tb.addAction(save)

        tb.actionTriggered[QAction].connect(self.toolbtnpressed)
        # self.setLayout(layout)

    def toolbtnpressed(self, a):
        print('pressed tool button is ' + a.text())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = ToolBarDemo()
    win.show()
    sys.exit(app.exec_())
