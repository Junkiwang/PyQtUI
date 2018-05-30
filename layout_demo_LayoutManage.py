# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'layout_demo_LayoutManage.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(530, 280, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(100, 250, 54, 12))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(100, 290, 54, 12))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(100, 330, 54, 12))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(190, 210, 54, 12))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(300, 210, 54, 12))
        self.label_5.setObjectName("label_5")
        self.doubleSpinBox_returns_min = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox_returns_min.setGeometry(QtCore.QRect(180, 240, 62, 22))
        self.doubleSpinBox_returns_min.setObjectName("doubleSpinBox_returns_min")
        self.doubleSpinBox_returns_max = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox_returns_max.setGeometry(QtCore.QRect(290, 250, 62, 22))
        self.doubleSpinBox_returns_max.setObjectName("doubleSpinBox_returns_max")
        self.doubleSpinBox_maxdrawdown_min = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox_maxdrawdown_min.setGeometry(QtCore.QRect(180, 280, 62, 22))
        self.doubleSpinBox_maxdrawdown_min.setObjectName("doubleSpinBox_maxdrawdown_min")
        self.doubleSpinBox_maxdrawdown_max = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox_maxdrawdown_max.setGeometry(QtCore.QRect(290, 280, 62, 22))
        self.doubleSpinBox_maxdrawdown_max.setObjectName("doubleSpinBox_maxdrawdown_max")
        self.doubleSpinBox_sharp_min = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox_sharp_min.setGeometry(QtCore.QRect(180, 320, 62, 22))
        self.doubleSpinBox_sharp_min.setObjectName("doubleSpinBox_sharp_min")
        self.doubleSpinBox_sharp_max = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox_sharp_max.setGeometry(QtCore.QRect(290, 320, 62, 22))
        self.doubleSpinBox_sharp_max.setObjectName("doubleSpinBox_sharp_max")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "开始"))
        self.label.setText(_translate("MainWindow", "收益"))
        self.label_2.setText(_translate("MainWindow", "最大回撤"))
        self.label_3.setText(_translate("MainWindow", "sharp比"))
        self.label_4.setText(_translate("MainWindow", "最小值"))
        self.label_5.setText(_translate("MainWindow", "最大值"))

