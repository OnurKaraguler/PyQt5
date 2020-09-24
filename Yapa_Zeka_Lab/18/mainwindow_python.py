# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_mainwindow(object):
    def setupUi(self, mainwindow):
        mainwindow.setObjectName("mainwindow")
        mainwindow.resize(400, 300)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        mainwindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(mainwindow)
        self.centralwidget.setObjectName("centralwidget")
        self.comboBox_users = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_users.setGeometry(QtCore.QRect(40, 110, 131, 41))
        self.comboBox_users.setObjectName("comboBox_users")
        self.pushButton_add_new_users = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_add_new_users.setGeometry(QtCore.QRect(210, 110, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton_add_new_users.setFont(font)
        self.pushButton_add_new_users.setObjectName("pushButton_add_new_users")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 70, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        mainwindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(mainwindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 400, 27))
        self.menubar.setObjectName("menubar")
        mainwindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(mainwindow)
        self.statusbar.setObjectName("statusbar")
        mainwindow.setStatusBar(self.statusbar)

        self.retranslateUi(mainwindow)
        QtCore.QMetaObject.connectSlotsByName(mainwindow)

    def retranslateUi(self, mainwindow):
        _translate = QtCore.QCoreApplication.translate
        mainwindow.setWindowTitle(_translate("mainwindow", "mainwindow"))
        self.pushButton_add_new_users.setText(_translate("mainwindow", "Yeni Kişi Ekle"))
        self.label.setText(_translate("mainwindow", "Kullanıcılar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainwindow = QtWidgets.QMainWindow()
    ui = Ui_mainwindow()
    ui.setupUi(mainwindow)
    mainwindow.show()
    sys.exit(app.exec_())
