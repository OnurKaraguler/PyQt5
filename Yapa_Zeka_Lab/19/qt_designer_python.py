# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qt_designer.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 500)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/Onur_Karaguler.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_warning = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_warning.setGeometry(QtCore.QRect(440, 40, 80, 80))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_warning.setFont(font)
        self.pushButton_warning.setAutoFillBackground(False)
        self.pushButton_warning.setStyleSheet("")
        self.pushButton_warning.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/icons/warning.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_warning.setIcon(icon1)
        self.pushButton_warning.setIconSize(QtCore.QSize(60, 60))
        self.pushButton_warning.setObjectName("pushButton_warning")
        self.comboBox_numbers = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_numbers.setGeometry(QtCore.QRect(388, 360, 141, 22))
        self.comboBox_numbers.setObjectName("comboBox_numbers")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(450, 130, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.pushButton_information = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_information.setGeometry(QtCore.QRect(180, 40, 80, 80))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_information.setFont(font)
        self.pushButton_information.setAutoFillBackground(False)
        self.pushButton_information.setStyleSheet("")
        self.pushButton_information.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/icons/information.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_information.setIcon(icon2)
        self.pushButton_information.setIconSize(QtCore.QSize(60, 60))
        self.pushButton_information.setObjectName("pushButton_information")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(70, 130, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(430, 330, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(160, 270, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.pushButton_about = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_about.setGeometry(QtCore.QRect(150, 180, 80, 80))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_about.setFont(font)
        self.pushButton_about.setAutoFillBackground(False)
        self.pushButton_about.setStyleSheet("")
        self.pushButton_about.setText("")
        self.pushButton_about.setIcon(icon)
        self.pushButton_about.setIconSize(QtCore.QSize(60, 60))
        self.pushButton_about.setObjectName("pushButton_about")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(170, 130, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.pushButton_question = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_question.setGeometry(QtCore.QRect(310, 40, 80, 80))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_question.setFont(font)
        self.pushButton_question.setAutoFillBackground(False)
        self.pushButton_question.setStyleSheet("")
        self.pushButton_question.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/icons/question.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_question.setIcon(icon3)
        self.pushButton_question.setIconSize(QtCore.QSize(60, 60))
        self.pushButton_question.setObjectName("pushButton_question")
        self.pushButton_numbers = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_numbers.setGeometry(QtCore.QRect(230, 320, 80, 80))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_numbers.setFont(font)
        self.pushButton_numbers.setAutoFillBackground(False)
        self.pushButton_numbers.setStyleSheet("")
        self.pushButton_numbers.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/icons/numbers.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_numbers.setIcon(icon4)
        self.pushButton_numbers.setIconSize(QtCore.QSize(60, 60))
        self.pushButton_numbers.setObjectName("pushButton_numbers")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(320, 270, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(320, 130, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.pushButton_about_qt = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_about_qt.setGeometry(QtCore.QRect(310, 180, 80, 80))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_about_qt.setFont(font)
        self.pushButton_about_qt.setAutoFillBackground(False)
        self.pushButton_about_qt.setStyleSheet("")
        self.pushButton_about_qt.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icons/icons/about_qt.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_about_qt.setIcon(icon5)
        self.pushButton_about_qt.setIconSize(QtCore.QSize(60, 60))
        self.pushButton_about_qt.setObjectName("pushButton_about_qt")
        self.pushButton_critical = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_critical.setGeometry(QtCore.QRect(60, 40, 80, 80))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_critical.setFont(font)
        self.pushButton_critical.setAutoFillBackground(False)
        self.pushButton_critical.setStyleSheet("")
        self.pushButton_critical.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/icons/icons/critical.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_critical.setIcon(icon6)
        self.pushButton_critical.setIconSize(QtCore.QSize(60, 60))
        self.pushButton_critical.setObjectName("pushButton_critical")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(220, 410, 111, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Ders_19"))
        self.label_4.setText(_translate("MainWindow", "Warning"))
        self.label.setText(_translate("MainWindow", "Critical"))
        self.label_8.setText(_translate("MainWindow", "Sayılar"))
        self.label_5.setText(_translate("MainWindow", "About"))
        self.label_2.setText(_translate("MainWindow", "Information"))
        self.label_6.setText(_translate("MainWindow", "About Qt"))
        self.label_3.setText(_translate("MainWindow", "Question"))
        self.label_7.setText(_translate("MainWindow", "Özel Kullanım"))
import icons_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
