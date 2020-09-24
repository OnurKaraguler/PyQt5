# https://www.youtube.com/watch?v=5g-gugyZWCk&list=PL1FgJUcJJ03uO70zDLDF3oaTu6s2QLOPa&index=10

import sys
from PyQt5.QtWidgets import QApplication, QLabel, QDialog, QVBoxLayout, QGroupBox, QCheckBox, QHBoxLayout
from PyQt5 import QtGui
from PyQt5 import QtCore

class Window (QDialog):
    def __init__(self):
        super().__init__()

        self.title = "PyQt5 Check Box"
        self.left = 300
        self.top = 400
        self.width = 400
        self.height = 100
        self.iconName = "Onur_Karaguler.png"

        self.InitWindow()

    def InitWindow (self):
        self.setWindowIcon(QtGui.QIcon(self.iconName))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.CreateCheckBox()

        vbox = QVBoxLayout()
        vbox.addWidget(self.groupbox)
        self.setLayout(vbox)

        self.label = QLabel("Hello")
        self.label.setFont(QtGui.QFont("Sanserif",13))
        vbox.addWidget(self.label)

        self.show()

    def CreateCheckBox (self):
        self.groupbox = QGroupBox("What is your favorite programming language?")
        self.groupbox.setFont(QtGui.QFont("Sanserif",13))
        hboxLayout = QHBoxLayout()

        self.check1 = QCheckBox ("Python")
        self.check1.setIcon(QtGui.QIcon("Onur_Karaguler.png"))
        self.check1.setIconSize(QtCore.QSize(40,40))
        self.check1.setFont(QtGui.QFont("Sanserif",13))
        self.check1.toggled.connect(self.OnCheckBox_Toggled)
        hboxLayout.addWidget(self.check1)

        self.check2 = QCheckBox ("Java")
        self.check2.setIcon(QtGui.QIcon("Onur_Karaguler.png"))
        self.check2.setIconSize(QtCore.QSize(40,40))
        self.check2.setFont(QtGui.QFont("Sanserif",13))
        self.check2.toggled.connect(self.OnCheckBox_Toggled)
        hboxLayout.addWidget(self.check2)

        self.check3 = QCheckBox ("C++")
        self.check3.setIcon(QtGui.QIcon("Onur_Karaguler.png"))
        self.check3.setIconSize(QtCore.QSize(40,40))
        self.check3.setFont(QtGui.QFont("Sanserif",13))
        self.check3.toggled.connect(self.OnCheckBox_Toggled)
        hboxLayout.addWidget(self.check3)

        self.groupbox.setLayout(hboxLayout)


    def OnCheckBox_Toggled(self):
        if self.check1.isChecked():
            self.label.setText("You have selected " + self.check1.text())

        if self.check2.isChecked():
            self.label.setText("You have selected " + self.check2.text())

        if self.check3.isChecked():
            self.label.setText("You have selected " + self.check3.text())

if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())

