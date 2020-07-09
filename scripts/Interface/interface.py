#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
import pandas as pd
import numpy as np

from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
from motar_mini.msg import dprm 

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (QMessageBox)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.P = np.array([])
        self.D = np.array([])
        self.DE = np.array([])
        self.R = np.array([])
        self.M = np.array([])
        self.S = np.array([])
        self.Text=np.array([])
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1300, 570)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("QMainWindow{background-color: rgb(52, 101, 164);}")
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.robotcam = QtWidgets.QLabel(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.robotcam.sizePolicy().hasHeightForWidth())
        self.robotcam.setSizePolicy(sizePolicy)
        self.robotcam.setMinimumSize(QtCore.QSize(200, 100))
        self.robotcam.setMaximumSize(QtCore.QSize(800, 400))
        self.robotcam.setSizeIncrement(QtCore.QSize(0, 0))
        self.robotcam.setBaseSize(QtCore.QSize(400, 200))
        self.robotcam.setText("")
        self.robotcam.setPixmap(QtGui.QPixmap("../Resources/camera.png"))
        self.robotcam.setScaledContents(True)
        self.robotcam.setWordWrap(False)
        self.robotcam.setObjectName("robotcam")
        self.verticalLayout.addWidget(self.robotcam)
        self.verticalLayout_8.addWidget(self.groupBox)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.patientlabel = QtWidgets.QLabel(self.centralwidget)
        self.patientlabel.setObjectName("patientlabel")
        self.verticalLayout_4.addWidget(self.patientlabel)
        self.patient1 = QtWidgets.QComboBox(self.centralwidget)
        self.patient1.setMinimumSize(QtCore.QSize(130, 25))
        self.patient1.setMaximumSize(QtCore.QSize(130, 30))
        self.patient1.setStyleSheet("background-color: rgb(138, 226, 52);")
        self.patient1.setObjectName("patient1")
        self.patient1.addItem("")
        self.patient1.addItem("")
        self.patient1.addItem("")
        self.patient1.addItem("")
        self.patient1.addItem("")
        self.verticalLayout_4.addWidget(self.patient1)
        self.patient2 = QtWidgets.QComboBox(self.centralwidget)
        self.patient2.setMinimumSize(QtCore.QSize(130, 25))
        self.patient2.setMaximumSize(QtCore.QSize(130, 30))
        self.patient2.setStyleSheet("background-color: rgb(138, 226, 52);")
        self.patient2.setObjectName("patient2")
        self.patient2.addItem("")
        self.patient2.addItem("")
        self.patient2.addItem("")
        self.patient2.addItem("")
        self.patient2.addItem("")
        self.verticalLayout_4.addWidget(self.patient2)
        self.patient3 = QtWidgets.QComboBox(self.centralwidget)
        self.patient3.setMinimumSize(QtCore.QSize(130, 25))
        self.patient3.setMaximumSize(QtCore.QSize(130, 30))
        self.patient3.setStyleSheet("background-color: rgb(138, 226, 52);")
        self.patient3.setObjectName("patient3")
        self.patient3.addItem("")
        self.patient3.addItem("")
        self.patient3.addItem("")
        self.patient3.addItem("")
        self.patient3.addItem("")
        self.verticalLayout_4.addWidget(self.patient3)
        self.patient4 = QtWidgets.QComboBox(self.centralwidget)
        self.patient4.setMinimumSize(QtCore.QSize(125, 25))
        self.patient4.setMaximumSize(QtCore.QSize(130, 30))
        self.patient4.setStyleSheet("background-color: rgb(138, 226, 52);")
        self.patient4.setObjectName("patient4")
        self.patient4.addItem("")
        self.patient4.addItem("")
        self.patient4.addItem("")
        self.patient4.addItem("")
        self.patient4.addItem("")
        self.verticalLayout_4.addWidget(self.patient4)
        self.horizontalLayout_2.addLayout(self.verticalLayout_4)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.roomlabel = QtWidgets.QLabel(self.centralwidget)
        self.roomlabel.setObjectName("roomlabel")
        self.verticalLayout_5.addWidget(self.roomlabel)
        self.room1 = QtWidgets.QComboBox(self.centralwidget)
        self.room1.setMinimumSize(QtCore.QSize(120, 25))
        self.room1.setMaximumSize(QtCore.QSize(120, 30))
        self.room1.setStyleSheet("background-color: rgb(117, 80, 123);")
        self.room1.setObjectName("room1")
        self.room1.addItem("")
        self.room1.addItem("")
        self.room1.addItem("")
        self.room1.addItem("")
        self.room1.addItem("")
        self.verticalLayout_5.addWidget(self.room1)
        self.room2 = QtWidgets.QComboBox(self.centralwidget)
        self.room2.setMinimumSize(QtCore.QSize(120, 25))
        self.room2.setMaximumSize(QtCore.QSize(120, 30))
        self.room2.setStyleSheet("background-color: rgb(117, 80, 123);")
        self.room2.setObjectName("room2")
        self.room2.addItem("")
        self.room2.addItem("")
        self.room2.addItem("")
        self.room2.addItem("")
        self.room2.addItem("")
        self.verticalLayout_5.addWidget(self.room2)
        self.room3 = QtWidgets.QComboBox(self.centralwidget)
        self.room3.setMinimumSize(QtCore.QSize(120, 25))
        self.room3.setMaximumSize(QtCore.QSize(120, 30))
        self.room3.setStyleSheet("background-color: rgb(117, 80, 123);")
        self.room3.setObjectName("room3")
        self.room3.addItem("")
        self.room3.addItem("")
        self.room3.addItem("")
        self.room3.addItem("")
        self.room3.addItem("")
        self.verticalLayout_5.addWidget(self.room3)
        self.room4 = QtWidgets.QComboBox(self.centralwidget)
        self.room4.setMinimumSize(QtCore.QSize(120, 25))
        self.room4.setMaximumSize(QtCore.QSize(120, 30))
        self.room4.setStyleSheet("background-color: rgb(117, 80, 123);")
        self.room4.setObjectName("room4")
        self.room4.addItem("")
        self.room4.addItem("")
        self.room4.addItem("")
        self.room4.addItem("")
        self.room4.addItem("")
        self.verticalLayout_5.addWidget(self.room4)
        self.horizontalLayout_2.addLayout(self.verticalLayout_5)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.medlabel = QtWidgets.QLabel(self.centralwidget)
        self.medlabel.setObjectName("medlabel")
        self.verticalLayout_6.addWidget(self.medlabel)
        self.med1 = QtWidgets.QComboBox(self.centralwidget)
        self.med1.setMinimumSize(QtCore.QSize(145, 25))
        self.med1.setMaximumSize(QtCore.QSize(145, 30))
        self.med1.setStyleSheet("background-color: rgb(78, 239, 191);")
        self.med1.setObjectName("med1")
        self.med1.addItem("")
        self.med1.addItem("")
        self.med1.addItem("")
        self.med1.addItem("")
        self.med1.addItem("")
        self.verticalLayout_6.addWidget(self.med1)
        self.med2 = QtWidgets.QComboBox(self.centralwidget)
        self.med2.setMinimumSize(QtCore.QSize(145, 25))
        self.med2.setMaximumSize(QtCore.QSize(145, 30))
        self.med2.setStyleSheet("background-color: rgb(78, 239, 191);")
        self.med2.setObjectName("med2")
        self.med2.addItem("")
        self.med2.addItem("")
        self.med2.addItem("")
        self.med2.addItem("")
        self.med2.addItem("")
        self.verticalLayout_6.addWidget(self.med2)
        self.med3 = QtWidgets.QComboBox(self.centralwidget)
        self.med3.setMinimumSize(QtCore.QSize(145, 25))
        self.med3.setMaximumSize(QtCore.QSize(145, 30))
        self.med3.setStyleSheet("background-color: rgb(78, 239, 191);")
        self.med3.setObjectName("med3")
        self.med3.addItem("")
        self.med3.addItem("")
        self.med3.addItem("")
        self.med3.addItem("")
        self.med3.addItem("")
        self.verticalLayout_6.addWidget(self.med3)
        self.med4 = QtWidgets.QComboBox(self.centralwidget)
        self.med4.setMinimumSize(QtCore.QSize(145, 25))
        self.med4.setMaximumSize(QtCore.QSize(145, 30))
        self.med4.setStyleSheet("background-color: rgb(78, 239, 191);")
        self.med4.setObjectName("med4")
        self.med4.addItem("")
        self.med4.addItem("")
        self.med4.addItem("")
        self.med4.addItem("")
        self.med4.addItem("")
        self.verticalLayout_6.addWidget(self.med4)
        self.horizontalLayout_2.addLayout(self.verticalLayout_6)
        self.verticalLayout_7.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.sendbtn = QtWidgets.QPushButton(self.centralwidget)
        self.sendbtn.setMinimumSize(QtCore.QSize(120, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.sendbtn.setFont(font)
        self.sendbtn.setStyleSheet("background-color: rgb(136, 138, 133);")
        self.sendbtn.setObjectName("sendbtn")
        self.horizontalLayout.addWidget(self.sendbtn)
        spacerItem1 = QtWidgets.QSpacerItem(150, 20, QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout_7.addLayout(self.horizontalLayout)
        self.verticalLayout_8.addLayout(self.verticalLayout_7)
        self.gridLayout_3.addLayout(self.verticalLayout_8, 0, 0, 1, 1)
        self.robotmvmtgroupbox = QtWidgets.QGroupBox(self.centralwidget)
        self.robotmvmtgroupbox.setStyleSheet("")
        self.robotmvmtgroupbox.setObjectName("robotmvmtgroupbox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.robotmvmtgroupbox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.robotpose = QtWidgets.QLabel(self.robotmvmtgroupbox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.robotpose.sizePolicy().hasHeightForWidth())
        self.robotpose.setSizePolicy(sizePolicy)
        self.robotpose.setMinimumSize(QtCore.QSize(200, 130))
        self.robotpose.setMaximumSize(QtCore.QSize(800, 650))
        self.robotpose.setBaseSize(QtCore.QSize(400, 260))
        self.robotpose.setText("")
        self.robotpose.setPixmap(QtGui.QPixmap("../Resources/map_from_top.png"))
        self.robotpose.setScaledContents(True)
        self.robotpose.setObjectName("robotpose")
        self.gridLayout.addWidget(self.robotpose, 0, 0, 1, 2)
        self.xyzlabel = QtWidgets.QLabel(self.robotmvmtgroupbox)
        self.xyzlabel.setObjectName("xyzlabel")
        self.gridLayout.addWidget(self.xyzlabel, 1, 0, 1, 1)
        self.xyzpose = QtWidgets.QLineEdit(self.robotmvmtgroupbox)
        self.xyzpose.setReadOnly(True)
        self.xyzpose.setObjectName("xyzpose")
        self.gridLayout.addWidget(self.xyzpose, 1, 1, 1, 1)
        self.destinationlabel = QtWidgets.QLabel(self.robotmvmtgroupbox)
        self.destinationlabel.setObjectName("destinationlabel")
        self.gridLayout.addWidget(self.destinationlabel, 2, 0, 1, 1)
        self.destinationpose = QtWidgets.QLineEdit(self.robotmvmtgroupbox)
        self.destinationpose.setReadOnly(True)
        self.destinationpose.setObjectName("destinationpose")
        self.gridLayout.addWidget(self.destinationpose, 2, 1, 1, 1)
        self.statuslabel = QtWidgets.QLabel(self.robotmvmtgroupbox)
        self.statuslabel.setObjectName("statuslabel")
        self.gridLayout.addWidget(self.statuslabel, 3, 0, 1, 1)
        self.status = QtWidgets.QLineEdit(self.robotmvmtgroupbox)
        self.status.setReadOnly(True)
        self.status.setObjectName("status")
        self.gridLayout.addWidget(self.status, 3, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.gridLayout_3.addWidget(self.robotmvmtgroupbox, 0, 1, 1, 1)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem2)
        self.SaExit = QtWidgets.QPushButton(self.centralwidget)
        self.SaExit.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.SaExit.setObjectName("SaExit")
        self.horizontalLayout_7.addWidget(self.SaExit)
        self.verticalLayout_3.addLayout(self.horizontalLayout_7)
        self.logbox = QtWidgets.QGroupBox(self.centralwidget)
        self.logbox.setObjectName("logbox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.logbox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.list = QtWidgets.QListWidget(self.logbox)
        self.list.setObjectName("list")
        self.verticalLayout_2.addWidget(self.list)
        self.verticalLayout_3.addWidget(self.logbox)
        self.mancongrpbox = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mancongrpbox.sizePolicy().hasHeightForWidth())
        self.mancongrpbox.setSizePolicy(sizePolicy)
        self.mancongrpbox.setMinimumSize(QtCore.QSize(400, 225))
        self.mancongrpbox.setMaximumSize(QtCore.QSize(16777215, 176))
        self.mancongrpbox.setObjectName("mancongrpbox")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.mancongrpbox)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.splitter_5 = QtWidgets.QSplitter(self.mancongrpbox)
        self.splitter_5.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_5.setObjectName("splitter_5")
        self.splitter = QtWidgets.QSplitter(self.splitter_5)
        self.splitter.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setOpaqueResize(True)
        self.splitter.setChildrenCollapsible(True)
        self.splitter.setObjectName("splitter")
        self.Upleftbutton = QtWidgets.QPushButton(self.splitter)
        self.Upleftbutton.setMinimumSize(QtCore.QSize(50, 45))
        self.Upleftbutton.setMaximumSize(QtCore.QSize(80, 56))
        self.Upleftbutton.setStyleSheet("background-color: rgb(245, 121, 0);")
        self.Upleftbutton.setObjectName("Upleftbutton")
        self.leftbutton = QtWidgets.QPushButton(self.splitter)
        self.leftbutton.setMinimumSize(QtCore.QSize(0, 45))
        self.leftbutton.setMaximumSize(QtCore.QSize(80, 56))
        self.leftbutton.setStyleSheet("background-color: rgb(237, 212, 0);")
        self.leftbutton.setObjectName("leftbutton")
        self.downleftbutton = QtWidgets.QPushButton(self.splitter)
        self.downleftbutton.setMinimumSize(QtCore.QSize(0, 45))
        self.downleftbutton.setMaximumSize(QtCore.QSize(80, 56))
        self.downleftbutton.setStyleSheet("background-color: rgb(245, 121, 0);")
        self.downleftbutton.setObjectName("downleftbutton")
        self.splitter_2 = QtWidgets.QSplitter(self.splitter_5)
        self.splitter_2.setOrientation(QtCore.Qt.Vertical)
        self.splitter_2.setOpaqueResize(True)
        self.splitter_2.setChildrenCollapsible(True)
        self.splitter_2.setObjectName("splitter_2")
        self.Upbutton = QtWidgets.QPushButton(self.splitter_2)
        self.Upbutton.setMinimumSize(QtCore.QSize(0, 0))
        self.Upbutton.setMaximumSize(QtCore.QSize(80, 56))
        self.Upbutton.setStyleSheet("background-color: rgb(237, 212, 0);")
        self.Upbutton.setObjectName("Upbutton")
        self.stopbutton = QtWidgets.QPushButton(self.splitter_2)
        self.stopbutton.setMinimumSize(QtCore.QSize(0, 45))
        self.stopbutton.setMaximumSize(QtCore.QSize(80, 56))
        self.stopbutton.setAutoFillBackground(False)
        self.stopbutton.setStyleSheet("background-color: rgb(204, 0, 0);")
        self.stopbutton.setObjectName("stopbutton")
        self.downbutton = QtWidgets.QPushButton(self.splitter_2)
        self.downbutton.setMinimumSize(QtCore.QSize(0, 45))
        self.downbutton.setMaximumSize(QtCore.QSize(80, 56))
        self.downbutton.setStyleSheet("background-color: rgb(237, 212, 0);")
        self.downbutton.setObjectName("downbutton")
        self.splitter_3 = QtWidgets.QSplitter(self.splitter_5)
        self.splitter_3.setOrientation(QtCore.Qt.Vertical)
        self.splitter_3.setObjectName("splitter_3")
        self.Uprightbutton = QtWidgets.QPushButton(self.splitter_3)
        self.Uprightbutton.setMinimumSize(QtCore.QSize(0, 45))
        self.Uprightbutton.setMaximumSize(QtCore.QSize(80, 56))
        self.Uprightbutton.setStyleSheet("background-color: rgb(245, 121, 0);")
        self.Uprightbutton.setObjectName("Uprightbutton")
        self.rightbutton = QtWidgets.QPushButton(self.splitter_3)
        self.rightbutton.setMinimumSize(QtCore.QSize(0, 45))
        self.rightbutton.setMaximumSize(QtCore.QSize(80, 56))
        self.rightbutton.setStyleSheet("background-color: rgb(237, 212, 0);")
        self.rightbutton.setObjectName("rightbutton")
        self.downrightbutton = QtWidgets.QPushButton(self.splitter_3)
        self.downrightbutton.setMinimumSize(QtCore.QSize(0, 45))
        self.downrightbutton.setMaximumSize(QtCore.QSize(80, 56))
        self.downrightbutton.setStyleSheet("background-color: rgb(245, 121, 0);")
        self.downrightbutton.setObjectName("downrightbutton")
        self.splitter_4 = QtWidgets.QSplitter(self.splitter_5)
        self.splitter_4.setOrientation(QtCore.Qt.Vertical)
        self.splitter_4.setObjectName("splitter_4")
        self.spinBox = QtWidgets.QSpinBox(self.splitter_4)
        self.spinBox.setMaximumSize(QtCore.QSize(55, 25))
        self.spinBox.setMaximum(150)
        self.spinBox.setProperty("value", 50)
        self.spinBox.setObjectName("spinBox")
        self.speedslider = QtWidgets.QSlider(self.splitter_4)
        self.speedslider.setMaximumSize(QtCore.QSize(55, 16777215))
        self.speedslider.setMaximum(150)
        self.speedslider.setProperty("value", 50)
        self.speedslider.setSliderPosition(50)
        self.speedslider.setOrientation(QtCore.Qt.Vertical)
        self.speedslider.setTickInterval(0)
        self.speedslider.setObjectName("speedslider")
        self.controlbtnsplitter = QtWidgets.QSplitter(self.splitter_5)
        self.controlbtnsplitter.setOrientation(QtCore.Qt.Vertical)
        self.controlbtnsplitter.setHandleWidth(20)
        self.controlbtnsplitter.setObjectName("controlbtnsplitter")
        self.takemancontrol = QtWidgets.QPushButton(self.controlbtnsplitter)
        self.takemancontrol.setMaximumSize(QtCore.QSize(80, 80))
        self.takemancontrol.setStyleSheet("background-color: rgb(164, 0, 0);")
        self.takemancontrol.setObjectName("takemancontrol")
        self.returnbase = QtWidgets.QPushButton(self.controlbtnsplitter)
        self.returnbase.setMaximumSize(QtCore.QSize(80, 80))
        self.returnbase.setStyleSheet("\n" "background-color: rgb(115, 210, 22);")
        self.returnbase.setObjectName("returnbase")
        self.horizontalLayout_3.addWidget(self.splitter_5)
        self.verticalLayout_3.addWidget(self.mancongrpbox)
        self.gridLayout_3.addLayout(self.verticalLayout_3, 0, 2, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.spinBox.valueChanged['int'].connect(self.speedslider.setValue)
        self.speedslider.valueChanged['int'].connect(self.spinBox.setValue)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.patient1, self.room1)
        MainWindow.setTabOrder(self.room1, self.med1)
        MainWindow.setTabOrder(self.med1, self.patient2)
        MainWindow.setTabOrder(self.patient2, self.room2)
        MainWindow.setTabOrder(self.room2, self.med2)
        MainWindow.setTabOrder(self.med2, self.patient3)
        MainWindow.setTabOrder(self.patient3, self.room3)
        MainWindow.setTabOrder(self.room3, self.med3)
        MainWindow.setTabOrder(self.med3, self.patient4)
        MainWindow.setTabOrder(self.patient4, self.room4)
        MainWindow.setTabOrder(self.room4, self.med4)
        MainWindow.setTabOrder(self.med4, self.sendbtn)
        MainWindow.setTabOrder(self.sendbtn, self.takemancontrol)
        MainWindow.setTabOrder(self.takemancontrol, self.returnbase)
        MainWindow.setTabOrder(self.returnbase, self.Upleftbutton)
        MainWindow.setTabOrder(self.Upleftbutton, self.Upbutton)
        MainWindow.setTabOrder(self.Upbutton, self.Uprightbutton)
        MainWindow.setTabOrder(self.Uprightbutton, self.leftbutton)
        MainWindow.setTabOrder(self.leftbutton, self.stopbutton)
        MainWindow.setTabOrder(self.stopbutton, self.rightbutton)
        MainWindow.setTabOrder(self.rightbutton, self.downleftbutton)
        MainWindow.setTabOrder(self.downleftbutton, self.downbutton)
        MainWindow.setTabOrder(self.downbutton, self.downrightbutton)
        MainWindow.setTabOrder(self.downrightbutton, self.SaExit)
        MainWindow.setTabOrder(self.SaExit, self.spinBox)
        MainWindow.setTabOrder(self.spinBox, self.speedslider)
        MainWindow.setTabOrder(self.speedslider, self.xyzpose)
        MainWindow.setTabOrder(self.xyzpose, self.destinationpose)
        MainWindow.setTabOrder(self.destinationpose, self.status)
        
        #Manual Control Buttons Disabled 
        self.is_man_control(0)
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
        
        self.takemancontrol.clicked.connect(lambda: self.is_man_control(1))
        self.takemancontrol.clicked.connect(lambda: self.combopressed(0))
        self.returnbase.clicked.connect(lambda: self.ReturnBase())
        self.returnbase.clicked.connect(lambda: self.combopressed(0))
        self.sendbtn.clicked.connect(lambda: self.combopressed(1))
        self.SaExit.clicked.connect(lambda: self.SAE())
        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MOTAR Interface"))
        self.groupBox.setTitle(_translate("MainWindow", "Robot Camera"))
        self.patientlabel.setText(_translate("MainWindow", "Patients"))
        self.patient1.setItemText(0, _translate("MainWindow", "Choose Patient"))
        self.patient1.setItemText(1, _translate("MainWindow", "1"))
        self.patient1.setItemText(2, _translate("MainWindow", "2"))
        self.patient1.setItemText(3, _translate("MainWindow", "3"))
        self.patient1.setItemText(4, _translate("MainWindow", "4"))
        self.patient2.setItemText(0, _translate("MainWindow", "Choose Patient"))
        self.patient2.setItemText(1, _translate("MainWindow", "1"))
        self.patient2.setItemText(2, _translate("MainWindow", "2"))
        self.patient2.setItemText(3, _translate("MainWindow", "3"))
        self.patient2.setItemText(4, _translate("MainWindow", "4"))
        self.patient3.setItemText(0, _translate("MainWindow", "Choose Patient"))
        self.patient3.setItemText(1, _translate("MainWindow", "1"))
        self.patient3.setItemText(2, _translate("MainWindow", "2"))
        self.patient3.setItemText(3, _translate("MainWindow", "3"))
        self.patient3.setItemText(4, _translate("MainWindow", "4"))
        self.patient4.setItemText(0, _translate("MainWindow", "Choose Patient"))
        self.patient4.setItemText(1, _translate("MainWindow", "1"))
        self.patient4.setItemText(2, _translate("MainWindow", "2"))
        self.patient4.setItemText(3, _translate("MainWindow", "3"))
        self.patient4.setItemText(4, _translate("MainWindow", "4"))
        self.roomlabel.setText(_translate("MainWindow", "Room"))
        self.room1.setItemText(0, _translate("MainWindow", "Choose Room"))
        self.room1.setItemText(1, _translate("MainWindow", "1"))
        self.room1.setItemText(2, _translate("MainWindow", "2"))
        self.room1.setItemText(3, _translate("MainWindow", "3"))
        self.room1.setItemText(4, _translate("MainWindow", "4"))
        self.room2.setItemText(0, _translate("MainWindow", "Choose Room"))
        self.room2.setItemText(1, _translate("MainWindow", "1"))
        self.room2.setItemText(2, _translate("MainWindow", "2"))
        self.room2.setItemText(3, _translate("MainWindow", "3"))
        self.room2.setItemText(4, _translate("MainWindow", "4"))
        self.room3.setItemText(0, _translate("MainWindow", "Choose Room"))
        self.room3.setItemText(1, _translate("MainWindow", "1"))
        self.room3.setItemText(2, _translate("MainWindow", "2"))
        self.room3.setItemText(3, _translate("MainWindow", "3"))
        self.room3.setItemText(4, _translate("MainWindow", "4"))
        self.room4.setItemText(0, _translate("MainWindow", "Choose Room"))
        self.room4.setItemText(1, _translate("MainWindow", "1"))
        self.room4.setItemText(2, _translate("MainWindow", "2"))
        self.room4.setItemText(3, _translate("MainWindow", "3"))
        self.room4.setItemText(4, _translate("MainWindow", "4"))
        self.medlabel.setText(_translate("MainWindow", "Medicine"))
        self.med1.setItemText(0, _translate("MainWindow", "Choose Medicine"))
        self.med1.setItemText(1, _translate("MainWindow", "A"))
        self.med1.setItemText(2, _translate("MainWindow", "B"))
        self.med1.setItemText(3, _translate("MainWindow", "C"))
        self.med1.setItemText(4, _translate("MainWindow", "D"))
        self.med2.setItemText(0, _translate("MainWindow", "Choose Medicine"))
        self.med2.setItemText(1, _translate("MainWindow", "A"))
        self.med2.setItemText(2, _translate("MainWindow", "B"))
        self.med2.setItemText(3, _translate("MainWindow", "C"))
        self.med2.setItemText(4, _translate("MainWindow", "D"))
        self.med3.setItemText(0, _translate("MainWindow", "Choose Medicine"))
        self.med3.setItemText(1, _translate("MainWindow", "A"))
        self.med3.setItemText(2, _translate("MainWindow", "B"))
        self.med3.setItemText(3, _translate("MainWindow", "C"))
        self.med3.setItemText(4, _translate("MainWindow", "D"))
        self.med4.setItemText(0, _translate("MainWindow", "Choose Medicine"))
        self.med4.setItemText(1, _translate("MainWindow", "A"))
        self.med4.setItemText(2, _translate("MainWindow", "B"))
        self.med4.setItemText(3, _translate("MainWindow", "C"))
        self.med4.setItemText(4, _translate("MainWindow", "D"))
        self.sendbtn.setText(_translate("MainWindow", "SEND"))
        self.robotmvmtgroupbox.setTitle(_translate("MainWindow", "Robot Movement"))
        self.xyzlabel.setText(_translate("MainWindow", "current pose"))
        self.destinationlabel.setText(_translate("MainWindow", "destination"))
        self.statuslabel.setText(_translate("MainWindow", "status"))
        self.SaExit.setText(_translate("MainWindow", "Save and Exit"))
        self.logbox.setTitle(_translate("MainWindow", "LOGS"))
        self.mancongrpbox.setTitle(_translate("MainWindow", "Manual Controls"))
        self.Upleftbutton.setText(_translate("MainWindow", "UL"))
        self.leftbutton.setText(_translate("MainWindow", "LEFT"))
        self.downleftbutton.setText(_translate("MainWindow", "DL"))
        self.Upbutton.setText(_translate("MainWindow", "UP"))
        self.stopbutton.setText(_translate("MainWindow", "STOP"))
        self.downbutton.setText(_translate("MainWindow", "DOWN"))
        self.Uprightbutton.setText(_translate("MainWindow", "UR"))
        self.rightbutton.setText(_translate("MainWindow", "RIGHT"))
        self.downrightbutton.setText(_translate("MainWindow", "DR"))
        self.takemancontrol.setText(_translate("MainWindow", "Take\n" "Manual\n" "Control"))
        self.returnbase.setText(_translate("MainWindow", "Return\n" "Base"))
        
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
    
    def combopressed(self,a):
        x,y,z,t=self.selected()
        if a==1:
            self.is_man_control(0)
            self.clicked("Delivering Medicine")
            if x!=1:
                text = ("for patient "+self.patient1.currentText()+" in room "+self.room1.currentText()+" medicine "+self.med1.currentText())
                self.Text=np.append(self.Text, text)
                self.list.addItem(text+" is being sent.")
                self.setPRM(int(self.patient1.currentText()), int(self.room1.currentText()), self.med1.currentText())
            if y!=2:
                text = ("for patient "+self.patient2.currentText()+" in room "+self.room2.currentText()+" medicine "+self.med2.currentText())
                self.Text=np.append(self.Text, text)
                self.list.addItem(text+" is being sent.")
                self.setPRM(int(self.patient2.currentText()), int(self.room2.currentText()), self.med2.currentText())
            if z!=3:
                text = ("for patient "+self.patient3.currentText()+" in room "+self.room3.currentText()+" medicine "+self.med3.currentText())
                self.Text=np.append(self.Text, text)
                self.list.addItem(text+" is being sent.")
                self.setPRM(int(self.patient3.currentText()), int(self.room3.currentText()), self.med3.currentText())
            if t!=4:
                text = ("for patient "+self.patient4.currentText()+" in room "+self.room4.currentText()+" medicine "+self.med4.currentText())
                self.Text=np.append(self.Text, text)
                self.list.addItem(text+" is being sent.")
                self.setPRM(int(self.patient4.currentText()), int(self.room4.currentText()), self.med4.currentText())
        if a==0:
            if len(self.Text)>0:
                r=len(self.Text)
                for i in range(r): 
                    text = self.Text[r-i-1]+" sending process has been aborted."
                    self.list.addItem(text)
                    self.Text=np.delete(self.Text, -1)
            self.DE=np.delete(self.DE, np.s_[::1])
            self.destinationpose.setText(str(self.DE))
    
    def setPRM(self,patient,room,medicine):
        if room==1:
            self.sendRobot(-4,9.7,0,0,0,-0.25,0.96,patient,room,medicine)
        elif room==2:
            self.sendRobot(-11,-5,0,0,0,0.7,-0.7,patient,room,medicine)
        elif room==3:
            self.sendRobot(-4,-5,0,0,0,-1,0,patient,room,medicine)
        else:
            self.sendRobot(-11,-9,0,0,0,0.7,0.7,patient,room,medicine)
            
    def sendRobot(self,x,y,z,ox,oy,oz,ow,p,r,m):
        rospy.init_node('motar_interface')
        point_pub = rospy.Publisher("motar_mini/dprm", dprm, queue_size=10)
        dest=dprm()
        
        dest.destination.position.x=x
        dest.destination.position.y=y
        dest.destination.position.z=z
        dest.destination.orientation.x=ox
        dest.destination.orientation.y=oy
        dest.destination.orientation.z=oz
        dest.destination.orientation.w=ow
        dest.patient=p
        dest.room=r
        dest.medicine=m
        
        point_pub.publish(dest)
        text="("+str(x)+", "+str(y)+", "+str(z)+")"
        
        self.P=np.append(self.P,p)
        self.D=np.append(self.D,text)
        self.DE=np.append(self.DE,text)
        self.R=np.append(self.R,r)
        self.M=np.append(self.M,m)
        self.S=np.append(self.S,"Not Reached")
        self.destinationpose.setText(str(self.DE))
    
    def clicked(self,text):
        self.status.setText(text)
        
    def control(self,x,th):
        try:
            rospy.init_node('motar_interface')
            velocity_pub = rospy.Publisher('cmd_vel', Twist, queue_size = 10)
            control_speed = 0
            control_turn = 0
            twist = Twist()
            target_speed = (float(self.speedslider.value()) * x)/100
            target_turn = th
            control_speed = target_speed
            control_turn = target_turn
        
            twist.linear.x=control_speed
            twist.angular.z=control_turn

            velocity_pub.publish(twist)
        except Exception as err:
            print(err)

    def ReturnBase(self):
        self.DE=np.delete(self.DE, np.s_[::1])
        self.sendRobot(0,0,0,0,0,"")
        self.clicked("Returning to Base Point")
        self.is_man_control(0)
        self.destinationpose.setText(str(self.DE))
    
    def SAE(self):
        msg= QMessageBox()
        msg.setWindowTitle('Save And Exit')
        msg.setText('Do You Want to Save Logs Before Exit?')
        msg.setIcon(QMessageBox.Warning)
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel)
        msg.setDefaultButton(QMessageBox.Yes)
        ret = msg.exec_()
        if ret==QMessageBox.Yes:
            data = {"Patient": self.P, 
                    "Room": self.R, 
                    "Medicine": self.M,
                    "Destination": self.D,
                    "Status": self.S};
            df= pd.DataFrame(data)
            df.to_excel('Hospital_data.xlsx', sheet_name='Hospital_data',columns=["Patient","Room","Medicine","Destination","Status"])
            sys.exit()
        if ret==QMessageBox.No:
            sys.exit()
    
def odomsub(data):
    try:
        pose=data.pose.pose.position
        
        text="("+"%.3f" % pose.x+", "+"%.3f" % pose.y+", "+"%.3f" % pose.z+")"
        
        ui.xyzpose.setText(text)
    except Exception as err:
        print(err)        
        
if __name__ == "__main__":
    import sys
    rospy.init_node('motar_interface')
    velocity_pub = rospy.Publisher('cmd_vel', Twist, queue_size = 10)
    point_pub = rospy.Publisher("motar_mini/dprm", dprm, queue_size=10)
    odom_sub = rospy.Subscriber("odom",Odometry,odomsub)
    #velocity_sub =rospy.Subscriber('motar/point',Point, velocitysub)

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

