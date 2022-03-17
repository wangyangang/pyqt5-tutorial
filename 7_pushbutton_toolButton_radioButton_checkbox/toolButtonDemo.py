"""
@author:  wangyangang
@contact: wangyangang@wangyangang.com
@site:    https://wangyangang.com
@time:   3/17/22 - 11:26 PM
"""
import sys
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QToolButton


class Demo(QWidget):
    def __init__(self):
        super(Demo, self).__init__()
        self.test_button = QToolButton(self)                        # 1
        self.test_button.setCheckable(True)
        self.test_button.setIcon(QIcon('python.jpg'))
        self.test_button.toggled.connect(self.button_state_func)
        self.test_button.isCheckable()

    def button_state_func(self):
        print(self.test_button.isChecked())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())