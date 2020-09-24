# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Python_Examples\QT_Designer\Yapa_Zeka_Lab\3.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(708, 585)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_1.setGeometry(QtCore.QRect(10, 20, 691, 23))
        self.pushButton_1.setObjectName("pushButton_1")
        self.radioButton_1 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_1.setGeometry(QtCore.QRect(30, 60, 82, 17))
        self.radioButton_1.setObjectName("radioButton_1")
        self.checkBox_1 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_1.setGeometry(QtCore.QRect(30, 90, 70, 17))
        self.checkBox_1.setObjectName("checkBox_1")
        self.comboBox_1 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_1.setGeometry(QtCore.QRect(10, 0, 691, 22))
        self.comboBox_1.setObjectName("comboBox_1")
        self.label_1 = QtWidgets.QLabel(self.centralwidget)
        self.label_1.setGeometry(QtCore.QRect(10, 420, 691, 121))
        self.label_1.setObjectName("label_1")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 708, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_1.setText(_translate("MainWindow", "PushButton"))
        self.radioButton_1.setText(_translate("MainWindow", "RadioButton"))
        self.checkBox_1.setText(_translate("MainWindow", "CheckBox"))
        self.label_1.setText(_translate("MainWindow", "TextLabel"))
