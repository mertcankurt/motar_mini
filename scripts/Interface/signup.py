#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'signup.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!
import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox


import sqlite3


class Ui_Signup(object):
    def setupUi(self, Signup):
        Signup.setObjectName("Signup")
        Signup.resize(570, 375)
        Signup.setModal(True)
        self.label = QtWidgets.QLabel(Signup)
        self.label.setGeometry(QtCore.QRect(160, 130, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Signup)
        self.label_2.setGeometry(QtCore.QRect(160, 230, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Signup)
        self.label_3.setGeometry(QtCore.QRect(160, 180, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.uname_lineEdit = QtWidgets.QLineEdit(Signup)
        self.uname_lineEdit.setGeometry(QtCore.QRect(250, 130, 141, 20))
        self.uname_lineEdit.setObjectName("uname_lineEdit")
        self.email_lineEdit = QtWidgets.QLineEdit(Signup)
        self.email_lineEdit.setGeometry(QtCore.QRect(250, 180, 141, 20))
        self.email_lineEdit.setObjectName("email_lineEdit")
        self.password_lineEdit = QtWidgets.QLineEdit(Signup)
        self.password_lineEdit.setGeometry(QtCore.QRect(250, 230, 141, 20))
        self.password_lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)#Password u gizleyen kod
        self.password_lineEdit.setObjectName("password_lineEdit")
        self.signup_btn = QtWidgets.QPushButton(Signup)
        self.signup_btn.setGeometry(QtCore.QRect(270, 290, 75, 23))
        self.signup_btn.setObjectName("signup_btn")
        ########################### Event #############################3
        self.signup_btn.clicked.connect(self.insertData)
        ################################################################
        self.label_4 = QtWidgets.QLabel(Signup)
        self.label_4.setGeometry(QtCore.QRect(150, 10, 321, 81))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")

        self.retranslateUi(Signup)
        QtCore.QMetaObject.connectSlotsByName(Signup)

    def retranslateUi(self, Signup):
        _translate = QtCore.QCoreApplication.translate
        Signup.setWindowTitle(_translate("Signup", "Dialog"))
        self.label.setText(_translate("Signup", "USERNAME"))
        self.label_2.setText(_translate("Signup", "PASSWORD"))
        self.label_3.setText(_translate("Signup", "EMAIL ID"))
        self.signup_btn.setText(_translate("Signup", "Sign Up"))
        self.label_4.setText(_translate("Signup", "Create Account"))
    
    def warningBox(self,title,message):
        msg= QMessageBox()
        msg.setWindowTitle(title)
        msg.setText(message)
        msg.setIcon(QMessageBox.Warning)
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()

    def insertData(self):
        username = self.uname_lineEdit.text()
        email = self.email_lineEdit.text()
        password = self.password_lineEdit.text()
        if not username or not email or not password:
            self.warningBox("Warning","Username, email or password Missing")
        else:
            connection  = sqlite3.connect("login.db")
            connection.execute("INSERT INTO USERS VALUES(?,?,?)",(username,email,password))
            connection.commit()
            connection.close()
            self.warningBox("İnfo","Succesfully Added a new User!")
        
        
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Signup = QtWidgets.QDialog()
    ui = Ui_Signup()
    ui.setupUi(Signup)
    Signup.show()
    sys.exit(app.exec_())

