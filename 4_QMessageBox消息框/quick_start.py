"""
@author:  wangyangang
@contact: wangyangang@wangyangang.com
@site:    https://wangyangang.com
@time:   3/17/22 - 9:45 PM
"""
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox


class Demo(QWidget):
    def __init__(self):
        super(Demo, self).__init__()
        self.button = QPushButton('information', self)
        self.button.clicked.connect(self.show_messagebox)      # 1

    def show_messagebox(self):
        QMessageBox.information(self, 'Title', 'Content',
                                QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel)  # 2


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())