#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Junki

import sys
import serial
import threading
import binascii
import serial.tools.list_ports
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class serialDemo(QWidget):
    def __init__(self, parent=None):
        super(serialDemo, self).__init__(parent)
        self.setWindowTitle('串口通信工具')
        # self.resize(700, 400)
        self.setFixedSize(700, 400)

        groupbox1 = QGroupBox()
        groupbox_sz = QGroupBox('串口设置')
        layout_sz = QGridLayout()
        self.label1 = QLabel('COM口')
        self.comb1 = QComboBox()
        self.comb1.addItem('')
        self.comb1.activated.connect(self._checkport)
        layout_sz.addWidget(self.label1, 0 ,0)
        layout_sz.addWidget(self.comb1, 0, 1)

        self.label2 = QLabel('波特率')
        self.comb2 = QComboBox()
        self.comb2.addItems(['1200', '2400', '4800', '9600', '19200', '38400', '57600', '115200', '自定义'])
        layout_sz.addWidget(self.label2, 1, 0)
        layout_sz.addWidget(self.comb2, 1, 1)

        self.label3 = QLabel('数据位')
        self.comb3 = QComboBox()
        self.comb3.addItems(['8', '7', '6', '5'])
        layout_sz.addWidget(self.label3, 2, 0)
        layout_sz.addWidget(self.comb3, 2, 1)

        self.label4 = QLabel('校验位')
        self.comb4 = QComboBox()
        self.comb4.addItems(['None', 'Even', 'Odd', 'Mark', 'Space'])
        layout_sz.addWidget(self.label4, 3, 0)
        layout_sz.addWidget(self.comb4, 3, 1)

        self.label5 = QLabel('停止位')
        self.comb5 = QComboBox()
        self.comb5.addItems(['1', '1.5', '2'])
        layout_sz.addWidget(self.label5, 4, 0)
        layout_sz.addWidget(self.comb5, 4, 1)
        groupbox_sz.setLayout(layout_sz)

        groupbox_dk = QGroupBox('串口操作')
        layout_dk = QGridLayout()
        self.btn1 = QPushButton('打开')
        self.btn1.clicked.connect(self._openport)
        layout_dk.addWidget(self.btn1, 0, 0)

        self.btn2 = QPushButton('关闭')
        self.btn2.clicked.connect(self._closeport)
        layout_dk.addWidget(self.btn2, 0, 1)
        groupbox_dk.setLayout(layout_dk)

        self.label6 = QLabel('串口状态：')
        self.label7 = QLabel('未打开串口')
        self.label7.setFont(QFont('黑体', 10))
        layout_dk.addWidget(self.label6, 1, 0)
        layout_dk.addWidget(self.label7, 1, 1)

        layout1 = QVBoxLayout()
        layout1.addWidget(groupbox_sz)
        layout1.addWidget(groupbox_dk)
        groupbox1.setLayout(layout1)

        groupbox2 = QGroupBox('接收区')
        layout_js = QHBoxLayout()
        self.text1 = QTextBrowser()
        self.text1.resize(200, 300)
        layout_js.addWidget(self.text1)
        groupbox2.setLayout(layout_js)

        groupbox3 = QGroupBox('发送区')
        layout_fs = QHBoxLayout()
        self.text2 = QTextEdit()
        self.text2.resize(150, 50)
        layout_fs.addWidget(self.text2)
        groupbox3.setLayout(layout_fs)

        layout3 = QFormLayout()
        self.checkbtn1 = QCheckBox('Hex显示')
        self.checkbtn1.setChecked(False)
        self.checkbtn1.stateChanged.connect(self._Hdisplay)
        self.checkbtn2 = QCheckBox('Hex发送')
        self.checkbtn2.setChecked(False)
        self.checkbtn2.stateChanged.connect(self._Hsend)
        layout3.addRow(self.checkbtn1, self.checkbtn2)
        self.btn3 = QPushButton('发送')
        self.btn3.clicked.connect(self._senddata)
        self.btn4 = QPushButton('清除')
        self.btn4.clicked.connect(self._clearsenddata)
        layout3.addRow(self.btn3, self.btn4)
        cz = QWidget()
        cz.setLayout(layout3)

        layout4 = QHBoxLayout()
        layout4.addWidget(groupbox3)
        layout4.addWidget(cz)
        fs = QWidget()
        fs.setLayout(layout4)

        layout5 = QGridLayout()
        layout5.addWidget(groupbox2, 0, 0, 1, 2)
        layout5.addWidget(fs, 1, 0, 1, 2)
        sj = QWidget()
        sj.setLayout(layout5)

        layout = QHBoxLayout()
        layout.addWidget(groupbox1)
        layout.addWidget(sj)
        self.setLayout(layout)

    def _checkport(self):
        pass

    def _openport(self):
        pass

    def _closeport(self):
        pass

    def _Hdisplay(self):
        pass

    def _Hsend(self):
        pass

    def _senddata(self):
        pass

    def _clearsenddata(self):
        pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = serialDemo()
    win.show()
    sys.exit(app.exec_())
