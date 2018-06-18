# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dashboard.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from supplier import Ui_form2


class Ui_Form1(object):
    def openWindow(self):
        self.window=QtWidgets.QWidget()
        self.ui = Ui_form2()
        self.ui.setupUi(self.window)
        
        self.window.show()

    def setupUi(self, Form1):
        Form1.setObjectName("Form1")
        Form1.resize(733, 422)
        self.frame = QtWidgets.QFrame(Form1)
        self.frame.setGeometry(QtCore.QRect(10, 10, 711, 41))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(10, 20, 101, 17))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(110, 20, 68, 17))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.pushButton_5 = QtWidgets.QPushButton(self.frame)
        self.pushButton_5.setGeometry(QtCore.QRect(610, 16, 99, 21))
        self.pushButton_5.setStyleSheet("")
        self.pushButton_5.setObjectName("pushButton_5")
        self.frame_2 = QtWidgets.QFrame(Form1)
        self.frame_2.setGeometry(QtCore.QRect(10, 50, 711, 361))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.pushButton = QtWidgets.QPushButton(self.frame_2)
        self.pushButton.setGeometry(QtCore.QRect(20, 20, 131, 131))
        self.pushButton.setStyleSheet("background-image: url(:/newPrefix/images/supplier.png);\n"
"background-repeat:no-repeat;")
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.openWindow)
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_2.setGeometry(QtCore.QRect(20, 190, 131, 141))
        self.pushButton_2.setStyleSheet("background-image: url(:/newPrefix/images/stock.png);\n"
"background-repeat:no-repeat;")
        self.pushButton_2.setText("")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_3.setGeometry(QtCore.QRect(550, 20, 141, 131))
        self.pushButton_3.setStyleSheet("background-image: url(:/newPrefix/images/client.png);\n"
"background-repeat:no-repeat;")
        self.pushButton_3.setText("")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_4.setGeometry(QtCore.QRect(550, 190, 141, 141))
        self.pushButton_4.setStyleSheet("background-image: url(:/newPrefix/images/report.png);\n"
"background-repeat:no-repeat;")
        self.pushButton_4.setText("")
        self.pushButton_4.setObjectName("pushButton_4")
        self.label_3 = QtWidgets.QLabel(self.frame_2)
        self.label_3.setGeometry(QtCore.QRect(230, 50, 271, 241))
        self.label_3.setStyleSheet("background-image: url(:/newPrefix/images/ims1.png);")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.frame_2)
        self.label_4.setGeometry(QtCore.QRect(60, 160, 81, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.frame_2)
        self.label_5.setGeometry(QtCore.QRect(60, 340, 68, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.frame_2)
        self.label_6.setGeometry(QtCore.QRect(600, 160, 68, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.frame_2)
        self.label_7.setGeometry(QtCore.QRect(600, 340, 68, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")

        self.retranslateUi(Form1)
        QtCore.QMetaObject.connectSlotsByName(Form1)

    def retranslateUi(self, Form1):
        _translate = QtCore.QCoreApplication.translate
        Form1.setWindowTitle(_translate("Form1", "Form1"))
        self.label.setText(_translate("Form1", "Welcome ,"))
        self.label_2.setText(_translate("Form1", "Admin"))
        self.pushButton_5.setText(_translate("Form1", "logout"))
        self.label_4.setText(_translate("Form1", "Supplier"))
        self.label_5.setText(_translate("Form1", "Stock"))
        self.label_6.setText(_translate("Form1", "Client"))
        self.label_7.setText(_translate("Form1", "Report"))

import xy_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form1 = QtWidgets.QWidget()
    ui = Ui_Form1()
    ui.setupUi(Form1)
    Form1.show()
    sys.exit(app.exec_())

