# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(523, 236)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.edit_label = QtWidgets.QLabel(Form)
        self.edit_label.setObjectName("edit_label")
        self.gridLayout.addWidget(self.edit_label, 0, 0, 1, 1)
        self.browser_label = QtWidgets.QLabel(Form)
        self.browser_label.setObjectName("browser_label")
        self.gridLayout.addWidget(self.browser_label, 0, 1, 1, 1)
        self.text_edit = QtWidgets.QTextEdit(Form)
        self.text_edit.setObjectName("text_edit")
        self.gridLayout.addWidget(self.text_edit, 1, 0, 1, 1)
        self.text_browser = QtWidgets.QTextBrowser(Form)
        self.text_browser.setObjectName("text_browser")
        self.gridLayout.addWidget(self.text_browser, 1, 1, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.edit_label.setText(_translate("Form", "QTextEdit"))
        self.browser_label.setText(_translate("Form", "QTextBrowser"))
