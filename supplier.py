# -*- coding: utf-8 -*-

# form2 implementation generated from reading ui file 'supplier.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3

class Ui_form2(object):
    def setupUi(self, form2):
        form2.setObjectName("form2")
        form2.resize(726, 448)
        form2.setStyleSheet("background-color:rgb(255, 255, 255);")
        self.frame = QtWidgets.QFrame(form2)
        self.frame.setGeometry(QtCore.QRect(10, 0, 701, 51))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(10, 10, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(380, 10, 161, 27))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.setindex0)
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(560, 10, 99, 27))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.setindex1)
        self.stackedWidget = QtWidgets.QStackedWidget(form2)
        self.stackedWidget.setGeometry(QtCore.QRect(10, 60, 711, 381))
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.frame_2 = QtWidgets.QFrame(self.page)
        self.frame_2.setGeometry(QtCore.QRect(0, -10, 701, 371))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setGeometry(QtCore.QRect(30, 20, 81, 21))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame_2)
        self.label_3.setGeometry(QtCore.QRect(30, 50, 101, 21))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.frame_2)
        self.label_4.setGeometry(QtCore.QRect(30, 80, 68, 17))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.frame_2)
        self.label_5.setGeometry(QtCore.QRect(30, 110, 68, 17))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.frame_2)
        self.label_6.setGeometry(QtCore.QRect(30, 140, 68, 17))
        self.label_6.setObjectName("label_6")
        self.lineEdit = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit.setGeometry(QtCore.QRect(140, 20, 181, 27))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_2.setGeometry(QtCore.QRect(140, 50, 181, 27))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_3.setGeometry(QtCore.QRect(140, 80, 181, 27))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_4.setGeometry(QtCore.QRect(140, 110, 181, 27))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_5.setGeometry(QtCore.QRect(140, 140, 181, 27))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_3.setGeometry(QtCore.QRect(70, 180, 99, 27))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.insert)
        self.label_7 = QtWidgets.QLabel(self.frame_2)
        self.label_7.setGeometry(QtCore.QRect(40, 270, 81, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.frame_2)
        self.label_8.setGeometry(QtCore.QRect(90, 250, 68, 17))
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.frame_2)
        self.label_9.setGeometry(QtCore.QRect(40, 300, 81, 21))
        self.label_9.setObjectName("label_9")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_6.setGeometry(QtCore.QRect(150, 300, 181, 27))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.pushButton_4 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_4.setGeometry(QtCore.QRect(190, 180, 99, 27))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(self.update)
        self.label_11 = QtWidgets.QLabel(self.frame_2)
        self.label_11.setGeometry(QtCore.QRect(400, 20, 91, 31))
        self.label_11.setObjectName("label_11")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_8.setGeometry(QtCore.QRect(510, 20, 181, 27))
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.label_12 = QtWidgets.QLabel(self.frame_2)
        self.label_12.setGeometry(QtCore.QRect(400, 56, 101, 21))
        self.label_12.setObjectName("label_12")
        self.lineEdit_9 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_9.setGeometry(QtCore.QRect(510, 50, 181, 27))
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.pushButton_5 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_5.setGeometry(QtCore.QRect(510, 90, 99, 27))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.clicked.connect(self.delete)
        self.label_10 = QtWidgets.QLabel(self.frame_2)
        self.label_10.setGeometry(QtCore.QRect(500, 180, 161, 131))
        self.label_10.setStyleSheet("background-image: url(:/newPrefix/images/supplier.png);\n"
"background-repeat:no-repeat;")
        self.label_10.setText("")
        self.label_10.setObjectName("label_10")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.frame_3 = QtWidgets.QFrame(self.page_2)
        self.frame_3.setGeometry(QtCore.QRect(10, 10, 691, 361))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.label_13 = QtWidgets.QLabel(self.frame_3)
        self.label_13.setGeometry(QtCore.QRect(20, 20, 81, 17))
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.frame_3)
        self.label_14.setGeometry(QtCore.QRect(300, 20, 101, 17))
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.frame_3)
        self.label_15.setGeometry(QtCore.QRect(270, 20, 21, 17))
        self.label_15.setObjectName("label_15")
        self.lineEdit_10 = QtWidgets.QLineEdit(self.frame_3)
        self.lineEdit_10.setGeometry(QtCore.QRect(100, 10, 161, 27))
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.lineEdit_11 = QtWidgets.QLineEdit(self.frame_3)
        self.lineEdit_11.setGeometry(QtCore.QRect(410, 10, 161, 27))
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.pushButton_6 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_6.setGeometry(QtCore.QRect(590, 10, 81, 27))
        self.pushButton_6.setObjectName("pushButton_6")
        self.tableWidget = QtWidgets.QTableWidget(self.frame_3)
        self.tableWidget.setGeometry(QtCore.QRect(10, 40, 671, 311))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        self.stackedWidget.addWidget(self.page_2)

        self.retranslateUi(form2)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(form2)

    def retranslateUi(self, form2):
        _translate = QtCore.QCoreApplication.translate
        form2.setWindowTitle(_translate("form2", "form2"))
        self.label.setText(_translate("form2", "Supplier"))
        self.pushButton.setText(_translate("form2", "Add/Update/Delete"))
        self.pushButton_2.setText(_translate("form2", "View"))
        self.label_2.setText(_translate("form2", "Supplier ID"))
        self.label_3.setText(_translate("form2", "Supplier Name"))
        self.label_4.setText(_translate("form2", "Contact"))
        self.label_5.setText(_translate("form2", "E-Mail"))
        self.label_6.setText(_translate("form2", "Address"))
        self.pushButton_3.setText(_translate("form2", "Add"))
        self.label_7.setText(_translate("form2", "Update By"))
        self.label_9.setText(_translate("form2", "Supplier ID"))
        self.pushButton_4.setText(_translate("form2", "Update"))
        self.label_11.setText(_translate("form2", "Supplier ID"))
        self.label_12.setText(_translate("form2", "Supplier Name"))
        self.pushButton_5.setText(_translate("form2", "Delete"))
        self.label_13.setText(_translate("form2", "Supplier ID"))
        self.label_14.setText(_translate("form2", "Supplier Name"))
        self.label_15.setText(_translate("form2", "OR"))
        self.pushButton_6.setText(_translate("form2", "Search"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("form2", "Supplier ID"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("form2", "Supplier Name"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("form2", "Contact"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("form2", "E-Mail"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("form2", "Address"))

    def setindex0(self):
        self.stackedWidget.setCurrentIndex(0)

    def setindex1(self):
        self.stackedWidget.setCurrentIndex(1)

    def insert(self):
        sid=self.lineEdit.text()
        sname=self.lineEdit_2.text()
        contact=self.lineEdit_3.text()
        email=self.lineEdit_4.text()
        address=self.lineEdit_5.text()
        try:
            conn=sqlite3.connect('invento')
            c=conn.cursor()
            c.execute("INSERT INTO supplier(sup_id,sup_name,contact,email,address) VALUES(?,?,?,?,?)",(sid,sname,contact,email,address))
            print("Successfully inserted values")
            conn.commit()
            conn.close()
        except:
            print("Error")

    def update(self):
        sid=self.lineEdit.text()
        sname=self.lineEdit_2.text()
        contact=self.lineEdit_3.text()
        email=self.lineEdit_4.text()
        address=self.lineEdit_5.text()
        new_sid=self.lineEdit_6.text()
        try:
            conn=sqlite3.connect('invento')
            c=conn.cursor()
            c.execute("UPDATE supplier SET sup_id=?,sup_name=?,contact=?,email=?,address=? WHERE sup_id=? ",(sid,sname,contact,email,address,new_sid))
            print("Successfully updated")
            conn.commit()
            conn.close()
        except:
            print("Not Updated")

    def delete(self):
        try:
            sid=self.lineEdit_8.text()
            sname=self.lineEdit_9.text()
            conn=sqlite3.connect('invento')
            c=conn.cursor()
            c.execute("DELETE FROM supplier WHERE sup_id=? OR sup_name=?",(sid,sname))
            print("Deleted Successfully")
            conn.commit()
            conn.close()
        except:
            print("Not Deleted")


import xy_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    form2 = QtWidgets.QWidget()
    ui = Ui_form2()
    ui.setupUi(form2)
    form2.show()
    sys.exit(app.exec_())

