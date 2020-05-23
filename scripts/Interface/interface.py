#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy

from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
from dprm.msg import dprm

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (QSlider)
from PyQt5.QtGui import QPixmap
import sys

turn=1.0

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1267, 589)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("QMainWindow{background-color: rgb(52, 101, 164);}\n")
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.robotmvmtgroupbox = QtWidgets.QGroupBox(self.centralwidget)
        self.robotmvmtgroupbox.setGeometry(QtCore.QRect(420, 0, 461, 551))
        self.robotmvmtgroupbox.setStyleSheet("")
        self.robotmvmtgroupbox.setObjectName("robotmvmtgroupbox")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.robotmvmtgroupbox)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        #Robot Pose
        self.robotpose = QtWidgets.QLabel(self.robotmvmtgroupbox)
        self.robotpose.setMinimumSize(QtCore.QSize(210, 410))
        self.robotpose.setObjectName("robotpose")
        self.robotpose.setPixmap(QPixmap('map_from_top.png'))
        self.robotpose.setScaledContents(True)
        self.verticalLayout_5.addWidget(self.robotpose)
        
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setObjectName("formLayout_2")
        self.xyzpose = QtWidgets.QLineEdit(self.robotmvmtgroupbox)
        self.xyzpose.setReadOnly(True)
        self.xyzpose.setObjectName("xyzpose")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.xyzpose)
        self.destinationlabel = QtWidgets.QLabel(self.robotmvmtgroupbox)
        self.destinationlabel.setObjectName("destinationlabel")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.destinationlabel)
        self.destinationpose = QtWidgets.QLineEdit(self.robotmvmtgroupbox)
        self.destinationpose.setReadOnly(True)
        self.destinationpose.setObjectName("destinationpose")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.destinationpose)
        self.statuslabel = QtWidgets.QLabel(self.robotmvmtgroupbox)
        self.statuslabel.setObjectName("statuslabel")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.statuslabel)
        self.status = QtWidgets.QLineEdit(self.robotmvmtgroupbox)
        self.status.setReadOnly(True)
        self.status.setObjectName("status")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.status)
        self.xyzlabel = QtWidgets.QLabel(self.robotmvmtgroupbox)
        self.xyzlabel.setObjectName("xyzlabel")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.xyzlabel)
        self.verticalLayout_5.addLayout(self.formLayout_2)
        self.list = QtWidgets.QListWidget(self.centralwidget)
        self.list.setGeometry(QtCore.QRect(880, 20, 381, 321))
        self.list.setObjectName("list")
        self.controlframe = QtWidgets.QFrame(self.centralwidget)
        self.controlframe.setGeometry(QtCore.QRect(880, 350, 381, 211))
        self.controlframe.setStyleSheet("")
        self.controlframe.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.controlframe.setFrameShadow(QtWidgets.QFrame.Raised)
        self.controlframe.setObjectName("controlframe")
           
        self.Upbutton = QtWidgets.QPushButton(self.controlframe)
        self.Upbutton.setGeometry(QtCore.QRect(100, 30, 70, 50))
        self.Upbutton.setStyleSheet("background-color: rgb(237, 212, 0);")
        self.Upbutton.setObjectName("Upbutton")
        
        self.downbutton = QtWidgets.QPushButton(self.controlframe)
        self.downbutton.setGeometry(QtCore.QRect(100, 150, 70, 50))
        self.downbutton.setStyleSheet("background-color: rgb(237, 212, 0);")
        self.downbutton.setObjectName("downbutton")
        
        self.leftbutton = QtWidgets.QPushButton(self.controlframe)
        self.leftbutton.setGeometry(QtCore.QRect(20, 90, 70, 50))
        self.leftbutton.setStyleSheet("background-color: rgb(237, 212, 0);")
        self.leftbutton.setObjectName("leftbutton")
        
        self.rightbutton = QtWidgets.QPushButton(self.controlframe)
        self.rightbutton.setGeometry(QtCore.QRect(180, 90, 70, 50))
        self.rightbutton.setStyleSheet("background-color: rgb(237, 212, 0);")
        self.rightbutton.setObjectName("rightbutton")
        
        self.stopbutton = QtWidgets.QPushButton(self.controlframe)
        self.stopbutton.setGeometry(QtCore.QRect(100, 90, 70, 50))
        self.stopbutton.setAutoFillBackground(False)
        self.stopbutton.setStyleSheet("background-color: rgb(204, 0, 0);")
        self.stopbutton.setObjectName("stopbutton")
        
        self.Upleftbutton = QtWidgets.QPushButton(self.controlframe)
        self.Upleftbutton.setGeometry(QtCore.QRect(20, 30, 70, 50))
        self.Upleftbutton.setStyleSheet("background-color: rgb(245, 121, 0);")
        self.Upleftbutton.setObjectName("Upleftbutton")
        
        self.Uprightbutton = QtWidgets.QPushButton(self.controlframe)
        self.Uprightbutton.setGeometry(QtCore.QRect(180, 30, 70, 50))
        self.Uprightbutton.setStyleSheet("background-color: rgb(245, 121, 0);")
        self.Uprightbutton.setObjectName("Uprightbutton")
        
        self.downleftbutton = QtWidgets.QPushButton(self.controlframe)
        self.downleftbutton.setGeometry(QtCore.QRect(20, 150, 70, 50))
        self.downleftbutton.setStyleSheet("background-color: rgb(245, 121, 0);")
        self.downleftbutton.setObjectName("downleftbutton")
        
        self.downrightbutton = QtWidgets.QPushButton(self.controlframe)
        self.downrightbutton.setGeometry(QtCore.QRect(180, 150, 70, 50))
        self.downrightbutton.setStyleSheet("background-color: rgb(245, 121, 0);")
        self.downrightbutton.setObjectName("downrightbutton")
        #Manuak Control Buttons Disabled 
        self.Upbutton.setDisabled(True)
        self.downbutton.setDisabled(True)
        self.leftbutton.setDisabled(True)
        self.rightbutton.setDisabled(True)
        self.stopbutton.setDisabled(True)
        self.Upleftbutton.setDisabled(True)
        self.Uprightbutton.setDisabled(True)
        self.downleftbutton.setDisabled(True)
        self.downrightbutton.setDisabled(True)
        #Manual Control Codes 
        self.Upbutton.clicked.connect(lambda: self.clicked("Robot is Moving Forward"))
        self.Upbutton.clicked.connect(lambda: self.control(1,0))
        self.downbutton.clicked.connect(lambda: self.clicked("Robot is Moving Backward"))
        self.downbutton.clicked.connect(lambda: self.control(-1,0))
        self.leftbutton.clicked.connect(lambda: self.clicked("Robot is Moving to the Left"))
        self.leftbutton.clicked.connect(lambda: self.control(0,1))
        self.rightbutton.clicked.connect(lambda: self.clicked("Robot is Moving to the Right"))
        self.rightbutton.clicked.connect(lambda: self.control(0,-1))
        self.stopbutton.clicked.connect(lambda: self.clicked("Robot Stopped"))
        self.stopbutton.clicked.connect(lambda: self.control(0,0))
        self.Upleftbutton.clicked.connect(lambda: self.clicked("Robot is Moving Left Forward"))
        self.Upleftbutton.clicked.connect(lambda: self.control(1,1))
        self.Uprightbutton.clicked.connect(lambda: self.clicked("Robot is Moving Right Forward"))
        self.Uprightbutton.clicked.connect(lambda: self.control(1,-1))
        self.downleftbutton.clicked.connect(lambda: self.clicked("Robot is Moving Left Backward"))
        self.downleftbutton.clicked.connect(lambda: self.control(-1,1))
        self.downrightbutton.clicked.connect(lambda: self.clicked("Robot is Moving Right Backward"))
        self.downrightbutton.clicked.connect(lambda: self.control(-1,-1))
        
        self.mnctrllabel = QtWidgets.QLabel(self.controlframe)
        self.mnctrllabel.setGeometry(QtCore.QRect(80, 10, 111, 17))
        self.mnctrllabel.setObjectName("mnctrllabel")
        
        self.speedslider = QSlider(self.controlframe)
        self.speedslider.setGeometry(QtCore.QRect(260, 30, 16, 160))
        self.speedslider.setMinimum(0)
        self.speedslider.setMaximum(200)
        self.speedslider.setSliderPosition(50)
        self.speedslider.setOrientation(QtCore.Qt.Vertical)
        self.speedslider.setTickInterval(10)
        self.speedslider.setObjectName("speedslider")
        self.speedslider.valueChanged.connect(lambda: self.v_change())
        
        self.speedlabel = QtWidgets.QLabel(self.controlframe)
        self.speedlabel.setGeometry(QtCore.QRect(250, 10, 31, 20))
        self.speedlabel.setObjectName("speedlabel")
        
        self.takemancontrol = QtWidgets.QPushButton(self.controlframe)
        self.takemancontrol.setGeometry(QtCore.QRect(300, 30, 61, 61))
        self.takemancontrol.setStyleSheet("background-color: rgb(164, 0, 0);")
        self.takemancontrol.setObjectName("takemancontrol")
        self.takemancontrol.clicked.connect(lambda: self.is_man_control(1))
        
        self.returnbase = QtWidgets.QPushButton(self.controlframe)
        self.returnbase.setGeometry(QtCore.QRect(300, 120, 61, 61))
        self.returnbase.setStyleSheet("\n""background-color: rgb(115, 210, 22);")
        self.returnbase.setObjectName("returnbase")
        self.returnbase.clicked.connect(lambda: self.ReturnBase())
        #Robot Cam
        self.robotcam = QtWidgets.QLabel(self.centralwidget)
        self.robotcam.setGeometry(QtCore.QRect(30, 20, 373, 210))
        self.robotcam.setMinimumSize(QtCore.QSize(210, 150))
        self.robotcam.setMaximumSize(QtCore.QSize(620, 500))
        self.robotcam.setObjectName("robotcam")
        self.robotcam.setPixmap(QPixmap('camera.png'))
        self.robotcam.setScaledContents(True)
        self.robotcamlabel = QtWidgets.QLabel(self.centralwidget)
        self.robotcamlabel.setGeometry(QtCore.QRect(160, 0, 101, 20))
        self.robotcamlabel.setObjectName("robotcamlabel")
        
        self.loglabel = QtWidgets.QLabel(self.centralwidget)
        self.loglabel.setGeometry(QtCore.QRect(1040, 0, 67, 17))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.loglabel.setFont(font)
        self.loglabel.setObjectName("loglabel")
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 270, 411, 238))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        #ComboBoxes
        self.patient1 = QtWidgets.QComboBox(self.formLayoutWidget)
        self.patient1.setMinimumSize(QtCore.QSize(130, 25))
        self.patient1.setMaximumSize(QtCore.QSize(130, 30))
        self.patient1.setStyleSheet("background-color: rgb(138, 226, 52);")
        self.patient1.setObjectName("patient1")
        self.patient1.addItem("Choose Patient")
        self.patient1.addItem("1")
        self.patient1.addItem("2")
        self.patient1.addItem("3")
        self.patient1.addItem("4")
        self.horizontalLayout.addWidget(self.patient1)
        
        self.room1 = QtWidgets.QComboBox(self.formLayoutWidget)
        self.room1.setMinimumSize(QtCore.QSize(80, 25))
        self.room1.setMaximumSize(QtCore.QSize(120, 30))
        self.room1.setStyleSheet("background-color: rgb(117, 80, 123);")
        self.room1.setObjectName("room1")
        self.room1.addItem("Choose Room")
        self.room1.addItem("1")
        self.room1.addItem("2")
        self.room1.addItem("3")
        self.room1.addItem("4")
        self.horizontalLayout.addWidget(self.room1)
        
        self.med1 = QtWidgets.QComboBox(self.formLayoutWidget)
        self.med1.setMinimumSize(QtCore.QSize(145, 25))
        self.med1.setMaximumSize(QtCore.QSize(145, 30))
        self.med1.setStyleSheet("background-color: rgb(78, 239, 191);")
        self.med1.setObjectName("med1")
        self.med1.addItem("Choose Medicine")
        self.med1.addItem("A")
        self.med1.addItem("B")
        self.med1.addItem("C")
        self.med1.addItem("D")
        self.horizontalLayout.addWidget(self.med1)
        
        self.formLayout.setLayout(3, QtWidgets.QFormLayout.LabelRole, self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.patient2 = QtWidgets.QComboBox(self.formLayoutWidget)
        self.patient2.setMinimumSize(QtCore.QSize(130, 25))
        self.patient2.setMaximumSize(QtCore.QSize(130, 30))
        self.patient2.setStyleSheet("background-color: rgb(138, 226, 52);")
        self.patient2.setObjectName("patient2")
        self.patient2.addItem("Choose Patient")
        self.patient2.addItem("1")
        self.patient2.addItem("2")
        self.patient2.addItem("3")
        self.patient2.addItem("4")
        self.horizontalLayout_2.addWidget(self.patient2)
        
        self.room2 = QtWidgets.QComboBox(self.formLayoutWidget)
        self.room2.setMinimumSize(QtCore.QSize(80, 25))
        self.room2.setMaximumSize(QtCore.QSize(120, 30))
        self.room2.setStyleSheet("background-color: rgb(117, 80, 123);")
        self.room2.setObjectName("room2")
        self.room2.addItem("Choose Room")
        self.room2.addItem("1")
        self.room2.addItem("2")
        self.room2.addItem("3")
        self.room2.addItem("4")
        self.horizontalLayout_2.addWidget(self.room2)
        
        self.med2 = QtWidgets.QComboBox(self.formLayoutWidget)
        self.med2.setMinimumSize(QtCore.QSize(145, 25))
        self.med2.setMaximumSize(QtCore.QSize(145, 30))
        self.med2.setStyleSheet("background-color: rgb(78, 239, 191);")
        self.med2.setObjectName("med2")
        self.med2.addItem("Choose Medicine")
        self.med2.addItem("A")
        self.med2.addItem("B")
        self.med2.addItem("C")
        self.med2.addItem("D")
        self.horizontalLayout_2.addWidget(self.med2)
        
        self.formLayout.setLayout(4, QtWidgets.QFormLayout.LabelRole, self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.patient3 = QtWidgets.QComboBox(self.formLayoutWidget)
        self.patient3.setMinimumSize(QtCore.QSize(130, 25))
        self.patient3.setMaximumSize(QtCore.QSize(130, 30))
        self.patient3.setStyleSheet("background-color: rgb(138, 226, 52);")
        self.patient3.setObjectName("patient3")
        self.patient3.addItem("Choose Patient")
        self.patient3.addItem("1")
        self.patient3.addItem("2")
        self.patient3.addItem("3")
        self.patient3.addItem("4")
        self.horizontalLayout_3.addWidget(self.patient3)
        
        self.room3 = QtWidgets.QComboBox(self.formLayoutWidget)
        self.room3.setMinimumSize(QtCore.QSize(80, 25))
        self.room3.setMaximumSize(QtCore.QSize(120, 30))
        self.room3.setStyleSheet("background-color: rgb(117, 80, 123);")
        self.room3.setObjectName("room3")
        self.room3.addItem("Choose Room")
        self.room3.addItem("1")
        self.room3.addItem("2")
        self.room3.addItem("3")
        self.room3.addItem("4")
        self.horizontalLayout_3.addWidget(self.room3)
        
        self.med3 = QtWidgets.QComboBox(self.formLayoutWidget)
        self.med3.setMinimumSize(QtCore.QSize(145, 25))
        self.med3.setMaximumSize(QtCore.QSize(145, 30))
        self.med3.setStyleSheet("background-color: rgb(78, 239, 191);")
        self.med3.setObjectName("med3")
        self.med3.addItem("Choose Medicine")
        self.med3.addItem("A")
        self.med3.addItem("B")
        self.med3.addItem("C")
        self.med3.addItem("D")
        self.horizontalLayout_3.addWidget(self.med3)
        
        self.formLayout.setLayout(5, QtWidgets.QFormLayout.LabelRole, self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.patient4 = QtWidgets.QComboBox(self.formLayoutWidget)
        self.patient4.setMinimumSize(QtCore.QSize(125, 25))
        self.patient4.setMaximumSize(QtCore.QSize(130, 30))
        self.patient4.setStyleSheet("background-color: rgb(138, 226, 52);")
        self.patient4.setObjectName("patient4")
        self.patient4.addItem("Choose Patient")
        self.patient4.addItem("1")
        self.patient4.addItem("2")
        self.patient4.addItem("3")
        self.patient4.addItem("4")
        self.horizontalLayout_4.addWidget(self.patient4)
        
        self.room4 = QtWidgets.QComboBox(self.formLayoutWidget)
        self.room4.setMinimumSize(QtCore.QSize(80, 25))
        self.room4.setMaximumSize(QtCore.QSize(120, 30))
        self.room4.setStyleSheet("background-color: rgb(117, 80, 123);")
        self.room4.setObjectName("room4")
        self.room4.addItem("Choose Room")
        self.room4.addItem("1")
        self.room4.addItem("2")
        self.room4.addItem("3")
        self.room4.addItem("4")
        self.horizontalLayout_4.addWidget(self.room4)
        
        self.med4 = QtWidgets.QComboBox(self.formLayoutWidget)
        self.med4.setMinimumSize(QtCore.QSize(145, 25))
        self.med4.setMaximumSize(QtCore.QSize(145, 30))
        self.med4.setStyleSheet("background-color: rgb(78, 239, 191);")
        self.med4.setObjectName("med4")
        self.med4.addItem("Choose Medicine")
        self.med4.addItem("A")
        self.med4.addItem("B")
        self.med4.addItem("C")
        self.med4.addItem("D")
        self.horizontalLayout_4.addWidget(self.med4)
        
        self.formLayout.setLayout(6, QtWidgets.QFormLayout.LabelRole, self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)
        
        self.sendbtn = QtWidgets.QPushButton(self.formLayoutWidget)
        self.sendbtn.setMinimumSize(QtCore.QSize(120, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.sendbtn.setFont(font)
        self.sendbtn.setStyleSheet("background-color: rgb(136, 138, 133);")
        self.sendbtn.setObjectName("sendbtn")
        self.horizontalLayout_5.addWidget(self.sendbtn)
        self.sendbtn.clicked.connect(self.combopressed)
        
        spacerItem1 = QtWidgets.QSpacerItem(155, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem1)
        self.formLayout.setLayout(7, QtWidgets.QFormLayout.SpanningRole, self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.patientlabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.patientlabel.setObjectName("patientlabel")
        self.horizontalLayout_6.addWidget(self.patientlabel)
        self.roomlabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.roomlabel.setObjectName("roomlabel")
        self.horizontalLayout_6.addWidget(self.roomlabel)
        self.medlabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.medlabel.setObjectName("medlabel")
        self.horizontalLayout_6.addWidget(self.medlabel)
        spacerItem2 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem2)
        self.formLayout.setLayout(2, QtWidgets.QFormLayout.SpanningRole, self.horizontalLayout_6)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1267, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MOTAR Interface"))
        self.robotmvmtgroupbox.setTitle(_translate("MainWindow", "Robot Movement"))
        self.destinationlabel.setText(_translate("MainWindow", "destination"))
        self.statuslabel.setText(_translate("MainWindow", "status"))
        self.xyzlabel.setText(_translate("MainWindow", "current pose"))
        self.downbutton.setText(_translate("MainWindow", "DOWN"))
        self.leftbutton.setText(_translate("MainWindow", "LEFT"))
        self.rightbutton.setText(_translate("MainWindow", "RIGHT"))
        self.Upbutton.setText(_translate("MainWindow", "UP"))
        self.stopbutton.setText(_translate("MainWindow", "STOP"))
        self.mnctrllabel.setText(_translate("MainWindow", "Manual Controls"))
        self.Upleftbutton.setText(_translate("MainWindow", "UL"))
        self.Uprightbutton.setText(_translate("MainWindow", "UR"))
        self.downleftbutton.setText(_translate("MainWindow", "DL"))
        self.downrightbutton.setText(_translate("MainWindow", "DR"))
        self.speedlabel.setText(_translate("MainWindow", "%50"))
        self.takemancontrol.setText(_translate("MainWindow", "Take\n""Manual\n""Control"))
        self.returnbase.setText(_translate("MainWindow", "Return\n""Base"))
        self.robotcamlabel.setText(_translate("MainWindow", "Robot Camera"))
        self.loglabel.setText(_translate("MainWindow", "LOGS"))
        self.sendbtn.setText(_translate("MainWindow", "SEND"))
        self.patientlabel.setText(_translate("MainWindow", "Patients"))
        self.roomlabel.setText(_translate("MainWindow", "Room"))
        self.medlabel.setText(_translate("MainWindow", "Medicine"))
    
    def is_man_control(self,x):
        if x==1:   
            self.Upbutton.setEnabled(True)
            self.downbutton.setEnabled(True)
            self.leftbutton.setEnabled(True)
            self.rightbutton.setEnabled(True)
            self.stopbutton.setEnabled(True)
            self.Upleftbutton.setEnabled(True)
            self.Uprightbutton.setEnabled(True)
            self.downleftbutton.setEnabled(True)
            self.downrightbutton.setEnabled(True)
        else:
            self.Upbutton.setDisabled(True)
            self.downbutton.setDisabled(True)
            self.leftbutton.setDisabled(True)
            self.rightbutton.setDisabled(True)
            self.stopbutton.setDisabled(True)
            self.Upleftbutton.setDisabled(True)
            self.Uprightbutton.setDisabled(True)
            self.downleftbutton.setDisabled(True)
            self.downrightbutton.setDisabled(True)
          
    def v_change(self):
        x="%"+str(self.speedslider.value())
        self.speedlabel.setText(x)
        self.speedlabel.adjustSize()
        

    def selected(self):
        x=0;y=0;z=0;t=0
        if len(self.patient1.currentText())>1 or len(self.room1.currentText())>1 or len(self.med1.currentText())>1:
            x=1
        if len(self.patient2.currentText())>1 or len(self.room2.currentText())>1 or len(self.med2.currentText())>1:
            y=2
        if len(self.patient3.currentText())>1 or len(self.room3.currentText())>1 or len(self.med3.currentText())>1:
            z=3
        if len(self.patient4.currentText())>1 or len(self.room4.currentText())>1 or len(self.med4.currentText())>1:
            t=4
        return x,y,z,t
        
    
    def combopressed(self):
        x,y,z,t=self.selected()
        self.is_man_control(0)
        if x!=1:
            text = "for patient "+self.patient1.currentText()+" in room "+self.room1.currentText()+" medicine "+self.med1.currentText()+" is being sent."
            self.list.addItem(text)
            self.setPRM(int(self.patient1.currentText()), int(self.room1.currentText()), self.med1.currentText())
        if y!=2:
            text = "for patient "+self.patient2.currentText()+" in room "+self.room2.currentText()+" medicine "+self.med2.currentText()+" is being sent."
            self.list.addItem(text)
            self.setPRM(int(self.patient2.currentText()), int(self.room2.currentText()), self.med2.currentText())
        if z!=3:
            text = "for patient "+self.patient3.currentText()+" in room "+self.room3.currentText()+" medicine "+self.med3.currentText()+" is being sent."
            self.list.addItem(text)
            self.setPRM(int(self.patient3.currentText()), int(self.room3.currentText()), self.med3.currentText())
        if t!=4:
            text = "for patient "+self.patient4.currentText()+" in room "+self.room4.currentText()+" medicine "+self.med4.currentText()+" is being sent."
            self.list.addItem(text)
            self.setPRM(int(self.patient4.currentText()), int(self.room4.currentText()), self.med4.currentText())
    
    def setPRM(self,patient,room,medicine):
        if room==1:
            self.sendRobot(10,10,0,patient,room,medicine)
        elif room==2:
            self.sendRobot(20,20,0,patient,room,medicine)
        elif room==3:
            self.sendRobot(30,30,0,patient,room,medicine)
        else:
            self.sendRobot(40,40,0,patient,room,medicine)
            
    def sendRobot(self,x,y,z,p,r,m):
        rospy.init_node('motar_interface')
        point_pub = rospy.Publisher("motar_mini/dprm", dprm, queue_size=10)
        dest=dprm()
        
        dest.destination.x=x
        dest.destination.y=y
        dest.destination.z=z
        dest.patient=p
        dest.room=r
        dest.medicine=m
        
        point_pub.publish(dest)
        text="("+str(x)+", "+str(y)+", "+str(z)+")"
        self.destinationpose.setText(text)
    
    def clicked(self,text):
        self.status.setText(text)
        
    def control(self,x,th):
        rospy.init_node('motar_interface')
        velocity_pub = rospy.Publisher('cmd_vel', Twist, queue_size = 10)
        control_speed = 0
        control_turn = 0
        twist = Twist()
        target_speed = (float(self.speedslider.value()) * x)/100
        target_turn = turn * th
        control_speed = target_speed
        control_turn = target_turn
    
        twist.linear.x=control_speed
        twist.angular.z=control_turn

        velocity_pub.publish(twist)
        
    def ReturnBase(self):
        self.sendRobot(0,0,0,0,0,"")
        self.clicked("Returning to Base Point")
        self.is_man_control(0)
        
class MyWindow(QtWidgets.QMainWindow):
    def closeEvent(self,event):
        result = QtGui.QMessageBox.question(self,
                      "Confirm Exit...",
                      "Are you sure you want to exit ?",
                      QtGui.QMessageBox.Yes| QtGui.QMessageBox.No)
        event.ignore()

        if result == QtGui.QMessageBox.Yes:
            event.accept()

def odomsub(data):
    x=data.pose.pose.position.x
    y=data.pose.pose.position.y
    z=data.pose.pose.position.z
    
    text="("+"%.5f" % x+", "+"%.5f" % y+", "+"%.5f" % z+")"
    
    ui.xyzpose.setText(text)

if __name__ == "__main__":
    rospy.init_node('motar_interface')
    velocity_pub = rospy.Publisher('cmd_vel', Twist, queue_size = 10)
    point_pub = rospy.Publisher("motar_mini/dprm", dprm, queue_size=10)
    odom_sub = rospy.Subscriber("/odom",Odometry,odomsub)
    #velocity_sub =rospy.Subscriber('motar/point',Point, velocitysub)

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())