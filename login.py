# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from dashboard import Ui_Form1

class Ui_Form(object):
    def openWindow(self):
        self.window=QtWidgets.QWidget()
        self.ui = Ui_Form1()
        self.ui.setupUi(self.window)
        Form.hide()
        self.window.show()

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(606, 312)
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(20, 30, 281, 251))
        self.frame.setAutoFillBackground(False)
        self.frame.setStyleSheet("background-image: url(:/newPrefix/images/ims1.png);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame_2 = QtWidgets.QFrame(Form)
        self.frame_2.setGeometry(QtCore.QRect(320, 30, 261, 251))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setGeometry(QtCore.QRect(40, 70, 81, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setGeometry(QtCore.QRect(40, 130, 71, 20))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame_2)
        self.label_3.setGeometry(QtCore.QRect(40, 20, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.lineEdit = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit.setGeometry(QtCore.QRect(40, 90, 181, 30))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_2.setGeometry(QtCore.QRect(40, 150, 181, 27))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(self.frame_2)
        self.pushButton.setGeometry(QtCore.QRect(40, 190, 99, 27))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.loadData)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "User Name"))
        self.label_2.setText(_translate("Form", "Password"))
        self.label_3.setText(_translate("Form", "Login"))
        self.pushButton.setText(_translate("Form", "Login"))
    
    def loadData(self):
        if self.lineEdit.text()=="admin":
            print("Welcome Admin")
            if self.lineEdit_2.text()=="123":
                self.pushButton.clicked.connect(self.openWindow)
                print("You are Logged in!")
            else:
                print("You forgot your password")
        else:
            print("Please contact your software supplier!")
        return None

import xy_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

