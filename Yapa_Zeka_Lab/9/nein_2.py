# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'nein_2.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 300)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(70, 40, 231, 131))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setFrameShape(QtWidgets.QFrame.Box)
        self.label.setText("")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 400, 21))
        self.menubar.setObjectName("menubar")
        self.menuRenkler = QtWidgets.QMenu(self.menubar)
        self.menuRenkler.setObjectName("menuRenkler")
        MainWindow.setMenuBar(self.menubar)
        self.action_blue = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/logos/icons/blue.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_blue.setIcon(icon)
        self.action_blue.setObjectName("action_blue")
        self.action_red = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/logos/icons/red.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_red.setIcon(icon1)
        self.action_red.setObjectName("action_red")
        self.action_green = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/logos/icons/green.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_green.setIcon(icon2)
        self.action_green.setObjectName("action_green")
        self.menuRenkler.addAction(self.action_blue)
        self.menuRenkler.addSeparator()
        self.menuRenkler.addAction(self.action_red)
        self.menuRenkler.addAction(self.action_green)
        self.menubar.addAction(self.menuRenkler.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menuRenkler.setTitle(_translate("MainWindow", "Renkler"))
        self.action_blue.setText(_translate("MainWindow", "Mavi"))
        self.action_blue.setShortcut(_translate("MainWindow", "Shift+B"))
        self.action_red.setText(_translate("MainWindow", "Kırmızı"))
        self.action_green.setText(_translate("MainWindow", "Yeşil"))
        self.action_green.setShortcut(_translate("MainWindow", "Shift+G"))
import icons


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
