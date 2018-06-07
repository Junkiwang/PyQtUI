#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Junki
from PyQt5.QtWidgets import QApplication, QTextEdit, QWidget, QVBoxLayout, QPushButton
import sys


class textEditDemo(QWidget):
    def __init__(self, parent=None):
        super(textEditDemo, self).__init__(parent)
        self.setWindowTitle('QTextEdit例子')

        self.resize(300, 300)
        self.textEdit = QTextEdit()
        self.btnPress0 = QPushButton('获取输入内容')
        self.btnPress1 = QPushButton('显示文本')
        self.btnPress2 = QPushButton('显示Html')

        layout = QVBoxLayout()
        layout.addWidget(self.textEdit)
        layout.addWidget(self.btnPress0)
        layout.addWidget(self.btnPress1)
        layout.addWidget(self.btnPress2)
        self.setLayout(layout)

        self.btnPress0.clicked.connect(self.getText)
        self.btnPress1.clicked.connect(self.btnPress1_Clicked)
        self.btnPress2.clicked.connect(self.btnPress2_Clicked)

    def getText(self):
        print('获取到文本框中的输入内容：%s' % self.textEdit.toPlainText())

    def btnPress1_Clicked(self):
        self.textEdit.setPlainText('Hello PyQt5!\n单击按钮。')

    def btnPress2_Clicked(self):
        self.textEdit.setHtml('<font color="red" size="6"><red>Hello PyQt5!<br>单击按钮。</red></font>')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = textEditDemo()
    win.show()
    sys.exit(app.exec_())
