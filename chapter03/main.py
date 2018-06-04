#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Junki
import sys
import helloworld, firstMainWin
from PyQt5.QtWidgets import QApplication, QMainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = firstMainWin.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
