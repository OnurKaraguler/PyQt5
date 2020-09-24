# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_page_2.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(480, 360)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_2nd_page = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2nd_page.setMinimumSize(QtCore.QSize(0, 40))
        self.pushButton_2nd_page.setObjectName("pushButton_2nd_page")
        self.gridLayout.addWidget(self.pushButton_2nd_page, 0, 0, 1, 1)
        self.pushButton_3rd_page = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3rd_page.setMinimumSize(QtCore.QSize(0, 40))
        self.pushButton_3rd_page.setObjectName("pushButton_3rd_page")
        self.gridLayout.addWidget(self.pushButton_3rd_page, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 480, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Ana Pencere"))
        self.pushButton_2nd_page.setText(_translate("MainWindow", "2. Pencereyi Aç"))
        self.pushButton_3rd_page.setText(_translate("MainWindow", "3. Pencereyi Aç"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
