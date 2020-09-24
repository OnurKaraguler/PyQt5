# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '14.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(574, 562)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_name = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_name.setGeometry(QtCore.QRect(90, 80, 131, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_name.setFont(font)
        self.pushButton_name.setObjectName("pushButton_name")
        self.pushButton_camera = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_camera.setGeometry(QtCore.QRect(330, 70, 161, 91))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_camera.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/Oyun_1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_camera.setIcon(icon)
        self.pushButton_camera.setIconSize(QtCore.QSize(64, 64))
        self.pushButton_camera.setCheckable(True)
        self.pushButton_camera.setObjectName("pushButton_camera")
        self.pushButton_close = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_close.setGeometry(QtCore.QRect(80, 210, 161, 91))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_close.setFont(font)
        self.pushButton_close.setText("")
        self.pushButton_close.setIcon(icon)
        self.pushButton_close.setIconSize(QtCore.QSize(80, 80))
        self.pushButton_close.setObjectName("pushButton_close")
        self.pushButton_open = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_open.setGeometry(QtCore.QRect(310, 210, 161, 91))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_open.setFont(font)
        self.pushButton_open.setToolTip("")
        self.pushButton_open.setStyleSheet("background-color: rgb(255, 255, 255,0);")
        self.pushButton_open.setText("")
        self.pushButton_open.setIcon(icon)
        self.pushButton_open.setIconSize(QtCore.QSize(80, 80))
        self.pushButton_open.setObjectName("pushButton_open")
        self.pushButton_start_stop = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_start_stop.setGeometry(QtCore.QRect(220, 380, 161, 61))
        self.pushButton_start_stop.setObjectName("pushButton_start_stop")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 574, 21))
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
        self.pushButton_name.setText(_translate("MainWindow", "Tuş"))
        self.pushButton_camera.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_close.setShortcut(_translate("MainWindow", "Shift+N"))
        self.pushButton_start_stop.setText(_translate("MainWindow", "PushButton"))
import icons_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
