#!/usr/bin/env python
# -*- coding: utf-8 -*-
import rospy
import sys

from interface import Ui_MainWindow
from signup import Ui_Signup

from geometry_msgs.msg import Twist
from dprm.msg import dprm

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

import sqlite3

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(506, 274)
        Dialog.setStyleSheet("")
        self.u_name_label = QtWidgets.QLabel(Dialog)
        self.u_name_label.setGeometry(QtCore.QRect(150, 110, 71, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.u_name_label.setFont(font)
        self.u_name_label.setAlignment(QtCore.Qt.AlignCenter)
        self.u_name_label.setObjectName("u_name_label")
        self.pass_label = QtWidgets.QLabel(Dialog)
        self.pass_label.setGeometry(QtCore.QRect(150, 150, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pass_label.setFont(font)
        self.pass_label.setAlignment(QtCore.Qt.AlignCenter)
        self.pass_label.setObjectName("pass_label")
        self.uname_lineEdit = QtWidgets.QLineEdit(Dialog)
        self.uname_lineEdit.setGeometry(QtCore.QRect(230, 110, 113, 20))
        self.uname_lineEdit.setObjectName("uname_lineEdit")
        self.pass_lineEdit = QtWidgets.QLineEdit(Dialog)
        self.pass_lineEdit.setGeometry(QtCore.QRect(230, 150, 113, 20))
        self.pass_lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.pass_lineEdit.setObjectName("pass_lineEdit")
        self.login_btn = QtWidgets.QPushButton(Dialog)
        self.login_btn.setGeometry(QtCore.QRect(230, 200, 51, 23))
        self.login_btn.setObjectName("login_btn")
        self.login_btn.clicked.connect(self.Login_btn)
        
        self.signup_btn = QtWidgets.QPushButton(Dialog)
        self.signup_btn.setGeometry(QtCore.QRect(290, 200, 51, 23))
        self.signup_btn.setObjectName("signup_btn")
        self.signup_btn.clicked.connect(self.Signup_btn)
        
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(170, 10, 211, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Login"))
        self.u_name_label.setText(_translate("Dialog", "USERNAME "))
        self.pass_label.setText(_translate("Dialog", "PASSWORD"))
        self.login_btn.setText(_translate("Dialog", "Login"))
        self.signup_btn.setText(_translate("Dialog", "Sign Up"))
        self.label.setText(_translate("Dialog", "Login Form"))
        
    def warningBox(self,title,message):
        msg= QMessageBox()
        msg.setWindowTitle(title)
        msg.setText(message)
        msg.setIcon(QMessageBox.Warning)
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()
        
    def Login_btn(self,x):
        username = self.uname_lineEdit.text()
        password = self.pass_lineEdit.text()
        if not username:
            self.warningBox("Warning",'Username Missing!')
        elif not password:
            self.warningBox("Warning",'Password Missing!')
        else:
            connection = sqlite3.connect("login.db")
            result = connection.execute("SELECT * FROM USERS WHERE USERNAME = ? AND PASSWORD = ?",(username,password))
            if(len(result.fetchall()) > 0):
                Dialog.hide()
                self.InterfaceShow()
            else:
                self.warningBox('Warning','Invalid Username And Password')
            connection.close()
        

    def InterfaceShow(self):
        self.Interface = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.Interface)
        self.Interface.show()
        
    def signUpShow(self):
        self.signUpWindow=QtWidgets.QDialog()
        self.ui=Ui_Signup()
        self.ui.setupUi(self.signUpWindow)
        self.signUpWindow.show()
        
    def Signup_btn(self):
        username = self.uname_lineEdit.text()
        password = self.pass_lineEdit.text()
        if not username:
            self.warningBox("Warning",'Username Missing!')
        elif not password:
            self.warningBox("Warning",'Password Missing!')
        else:
            connection = sqlite3.connect("login.db")
            result = connection.execute("SELECT * FROM USERS WHERE USERNAME = ? AND PASSWORD = ?",(username,password))
            if(len(result.fetchall()) > 0):
                self.signUpShow()
            else:
                self.warningBox('Warning','Invalid Username And Password')
            connection.close()


if __name__ == "__main__": 
    rospy.init_node('motar_interface')
    velocity_pub = rospy.Publisher('cmd_vel', Twist, queue_size = 10)
    point_pub = rospy.Publisher("motar_mini/dprm", dprm, queue_size=10)
    
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

