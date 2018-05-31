#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Junki
# Module implementing LayoutDemo
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow, QApplication
from layout_demo_LayoutManage import Ui_MainWindow
class LayoutDemo(QMainWindow, Ui_MainWindow):
    def __init__(self, parent = None):
        # @param parent refernece to the parent widget
        # @type QWidget
        super(LayoutDemo, self).__init__(parent)
        self.setupUi(self)
    @pyqtSlot()
    def on_pushButton_clicked(self):
        print('收益_min:',self.doubleSpinBox_returns_min.text())
        print('收益_max:',self.doubleSpinBox_returns_max.text())
        print('最大回撤_min:',self.doubleSpinBox_maxdrawdown_min.text())
        print('最大回撤_max:',self.doubleSpinBox_maxdrawdown_max.text())
        print('sharp比_min:',self.doubleSpinBox_sharp_min.text())
        print('sharp比_min:',self.doubleSpinBox_sharp_max.text())

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    ui = LayoutDemo()
    ui.show()
    sys.exit(app.exec_())


