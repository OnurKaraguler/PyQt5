# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'settings.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_settings(object):
    def setupUi(self, settings):
        settings.setObjectName("settings")
        settings.resize(400, 300)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        settings.setFont(font)
        self.lineEdit_name = QtWidgets.QLineEdit(settings)
        self.lineEdit_name.setGeometry(QtCore.QRect(92, 70, 271, 31))
        self.lineEdit_name.setObjectName("lineEdit_name")
        self.label = QtWidgets.QLabel(settings)
        self.label.setGeometry(QtCore.QRect(30, 70, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.pushButton_add = QtWidgets.QPushButton(settings)
        self.pushButton_add.setGeometry(QtCore.QRect(40, 110, 321, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton_add.setFont(font)
        self.pushButton_add.setObjectName("pushButton_add")

        self.retranslateUi(settings)
        QtCore.QMetaObject.connectSlotsByName(settings)

    def retranslateUi(self, settings):
        _translate = QtCore.QCoreApplication.translate
        settings.setWindowTitle(_translate("settings", "Yeni Kişi Ekle"))
        self.label.setText(_translate("settings", "Ad:"))
        self.pushButton_add.setText(_translate("settings", "Ekle"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    settings = QtWidgets.QWidget()
    ui = Ui_settings()
    ui.setupUi(settings)
    settings.show()
    sys.exit(app.exec_())
