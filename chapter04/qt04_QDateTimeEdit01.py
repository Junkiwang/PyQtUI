# -*- coding: utf-8 -*-

'''
    【简介】
	PyQt5中 DateTimeEdit 例子
   
  
'''

import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QDate, QDateTime, QTime


class DateTimeEditDemo(QWidget):
    def __init__(self):
        super(DateTimeEditDemo, self).__init__()
        self.initUI()
        self.setWindowTitle('QDateTimeEdit例子')
        self.resize(300, 90)

    def initUI(self):
        vlayout = QVBoxLayout()
        self.getbutton = QPushButton('获取日期和时间')
        self.getbutton.clicked.connect(self.__print)
        self.dateTimeEdit = QDateTimeEdit(self)
        self.dateTimeEdit.setCalendarPopup(True)
        self.dateTimeEdit2 = QDateTimeEdit(QDateTime.currentDateTime(), self)
        self.dateTimeEdit2.setMaximumDate(QDate.currentDate().addDays(365))
        self.dateTimeEdit2.setMinimumDate(QDate.currentDate().addDays(-365))
        self.dateTimeEdit2.setCalendarPopup(True)
        self.dateTimeEdit2.dateChanged.connect(self.onDateChanged)
        self.dateTimeEdit2.dateTimeChanged.connect(self.onDateTimeChanged)
        self.dateTimeEdit2.timeChanged.connect(self.onTimeChanged)
        self.dateEdit = QDateEdit(QDate.currentDate(), self)
        self.timeEdit = QTimeEdit(QTime.currentTime(), self)

        # 设置日期时间格式
        self.dateTimeEdit.setDisplayFormat("yyyy-MM-dd HH:mm:ss")
        self.dateTimeEdit2.setDisplayFormat("yyyy/MM/dd HH-mm-ss")
        self.dateEdit.setDisplayFormat("yyyy.MM.dd")
        self.timeEdit.setDisplayFormat("HH:mm:ss")

        vlayout.addWidget(self.dateTimeEdit)
        vlayout.addWidget(self.dateTimeEdit2)
        vlayout.addWidget(self.dateEdit)
        vlayout.addWidget(self.timeEdit)
        vlayout.addWidget(self.getbutton)
        self.setLayout(vlayout)

    def __print(self):
        dateTime = self.dateTimeEdit2.dateTime()
        maxDate = self.dateTimeEdit2.maximumDate()
        maxDateTime = self.dateTimeEdit2.maximumDateTime()
        maxTime = self.dateTimeEdit2.maximumTime()
        minDate = self.dateTimeEdit2.minimumDate()
        minDateTime = self.dateTimeEdit2.minimumDateTime()
        minTime = self.dateTimeEdit2.minimumTime()

        print('\n选择日期时间')
        print('dateTime=%s' % str(dateTime))
        print('maxDate=%s' % str(maxDate))
        print('maxDateTime=%s' % str(maxDateTime))
        print('maxTime=%s' % str(maxTime))
        print('minDate=%s' % str(minDate))
        print('minDateTime=%s' % str(minDateTime))
        print('minTime=%s' % str(minTime))

    def onDateChanged(self, date):
        print(date)

    def onDateTimeChanged(self, dateTime):
        print(dateTime)

    def onTimeChanged(self, time):
        print(time)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = DateTimeEditDemo()
    demo.show()
    sys.exit(app.exec_())
