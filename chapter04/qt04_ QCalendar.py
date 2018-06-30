#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Junki
import sys
from PyQt5 import QtCore
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class CalendarDemo(QWidget):
    def __init__(self):
        super(CalendarDemo, self).__init__()
        self.initUI()
        self.setGeometry(100, 100, 350, 350)
        self.setWindowTitle('Calendar 例子')

    def initUI(self):
        self.cal = QCalendarWidget(self)
        self.cal.setMinimumDate(QDate(1980, 1, 1))
        self.cal.setMaximumDate(QDate(4000, 1, 1))
        self.cal.setGridVisible(True)
        self.cal.move(20, 20)
        self.cal.clicked[QtCore.QDate].connect(self.showDate)
        self.lb = QLabel('                 ', self)    # 默认显示长度
        self.lb.move(20, 300)
        date = self.cal.selectedDate()
        # self.lb.setText(date.toString('yyyy-MM-dd dddd'))

    def showDate(self, date):
        self.lb.setText(date.toString('yyyy-MM-dd dddd'))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = CalendarDemo()
    win.show()
    sys.exit(app.exec_())
