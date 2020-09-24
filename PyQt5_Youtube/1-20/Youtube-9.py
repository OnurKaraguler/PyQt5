# https://www.youtube.com/watch?v=N-PmjWip51k&list=PL1FgJUcJJ03uO70zDLDF3oaTu6s2QLOPa&index=9

import sys
from PyQt5.QtWidgets import QApplication, QLabel, QDialog, QVBoxLayout, QGroupBox, QRadioButton, QHBoxLayout
from PyQt5 import QtGui
from PyQt5 import QtCore

class Window (QDialog):
    def __init__(self):
        super().__init__()

        self.title = "PyQt5 Radio Button"
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

        self.radioButton()

        vbox = QVBoxLayout()
        vbox.addWidget(self.groupBox)

        self.label = QLabel (self)
        self.label.setFont(QtGui.QFont("Sanserif",15))
        vbox.addWidget(self.label)


        self.setLayout(vbox)

        self.show()

    def radioButton (self):
        self.groupBox = QGroupBox ("What is your favorite programming language?")
        self.groupBox.setFont(QtGui.QFont("Sanserif",13))

        hboxlayout = QHBoxLayout()

        self.radiobutton1 = QRadioButton ("Football")
        self.radiobutton1.setChecked(True)
        self.radiobutton1.setIcon(QtGui.QIcon("Onur_Karaguler.png"))
        self.radiobutton1.setIconSize(QtCore.QSize(40,40))
        self.radiobutton1.setFont(QtGui.QFont("Samnserif",13))
        self.radiobutton1.toggled.connect(self.OnRadioButton)
        hboxlayout.addWidget(self.radiobutton1)

        self.radiobutton2 = QRadioButton ("Crciket")
        self.radiobutton2.setIcon(QtGui.QIcon("Onur_Karaguler.png"))
        self.radiobutton2.setIconSize(QtCore.QSize(40,40))
        self.radiobutton2.setFont(QtGui.QFont("Samnserif",13))
        self.radiobutton2.toggled.connect(self.OnRadioButton)
        hboxlayout.addWidget(self.radiobutton2)

        self.radiobutton3 = QRadioButton ("Tennis")
        self.radiobutton3.setIcon(QtGui.QIcon("Onur_Karaguler.png"))
        self.radiobutton3.setIconSize(QtCore.QSize(40,40))
        self.radiobutton3.setFont(QtGui.QFont("Samnserif",13))
        self.radiobutton3.toggled.connect(self.OnRadioButton)
        hboxlayout.addWidget(self.radiobutton3)



        self.groupBox.setLayout(hboxlayout)

    def OnRadioButton (self):
        radioBtn = self.sender()

        if radioBtn.isChecked():
            self.label.setText("You have selected " + radioBtn.text())


if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window ()
    sys.exit(App.exec())

