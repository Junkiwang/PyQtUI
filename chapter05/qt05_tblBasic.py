# -*- coding: utf-8 -*- 

'''
    【简介】
	PyQT5中单元格的基本例子
    
'''

import sys
from PyQt5.QtWidgets import *


class Table(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("QTableWidget 例子")
        self.resize(430, 230)
        conLayout = QHBoxLayout()
        tableWidget = QTableWidget(4, 3)
        # tableWidget.setRowCount(4)
        # tableWidget.setColumnCount(3)
        conLayout.addWidget(tableWidget)

        tableWidget.setHorizontalHeaderLabels(['姓名', '性别', '体重(kg)'])
        tableWidget.setVerticalHeaderLabels(['行1', '行2', '行3', '行4'])

        newItem = QTableWidgetItem("张三")
        tableWidget.setItem(0, 0, newItem)

        newItem = QTableWidgetItem("男")
        tableWidget.setItem(0, 1, newItem)

        newItem = QTableWidgetItem("70")
        tableWidget.setItem(0, 2, newItem)

        # 将表格变为禁止编辑
        # tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)

        # 设置表格为整行选择
        tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)

        # 将行和列的大小设为与内容相匹配
        # tableWidget.resizeColumnsToContents()
        # tableWidget.resizeRowsToContents()

        # 表格表头的显示与隐藏
        # tableWidget.verticalHeader().setVisible(False)
        # tableWidget.horizontalHeader().setVisible(False)

        # 自适应伸缩模式，跟随窗口大小自动变化
        # tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        # tableWidget.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # 不显示表格单元格的分割线
        # tableWidget.setShowGrid(False)

        self.setLayout(conLayout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    example = Table()
    example.show()
    sys.exit(app.exec_())
