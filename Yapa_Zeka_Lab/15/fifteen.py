# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '15.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(609, 428)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.comboBox_birds = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_birds.setGeometry(QtCore.QRect(40, 50, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.comboBox_birds.setFont(font)
        self.comboBox_birds.setObjectName("comboBox_birds")
        self.comboBox_fruits = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_fruits.setGeometry(QtCore.QRect(350, 50, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.comboBox_fruits.setFont(font)
        self.comboBox_fruits.setObjectName("comboBox_fruits")
        self.comboBox_animals = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_animals.setGeometry(QtCore.QRect(40, 210, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.comboBox_animals.setFont(font)
        self.comboBox_animals.setObjectName("comboBox_animals")
        self.comboBox_cars = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_cars.setGeometry(QtCore.QRect(340, 210, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.comboBox_cars.setFont(font)
        self.comboBox_cars.setObjectName("comboBox_cars")
        self.pushButton_show = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_show.setGeometry(QtCore.QRect(220, 300, 151, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_show.setFont(font)
        self.pushButton_show.setObjectName("pushButton_show")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 609, 21))
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
        self.pushButton_show.setText(_translate("MainWindow", "Göster"))
import icons_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
