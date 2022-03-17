"""
@author:  wangyangang
@contact: wangyangang@wangyangang.com
@site:    https://wangyangang.com
@time:   3/18/22 - 12:38 AM
"""
import sys
from PyQt5.QtWidgets import QApplication, QWidget
from test import Ui_Form


class Demo(QWidget, Ui_Form):
    def __init__(self):
        super(Demo, self).__init__()
        self.setupUi(self)                                          # 1
        self.text_edit.textChanged.connect(self.show_text_func)     # 2

    def show_text_func(self):
        self.text_browser.setText(self.text_edit.toPlainText())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())