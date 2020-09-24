import sys
from PyQt5.QtWidgets import QDialog, QPushButton, QApplication, QGroupBox, QVBoxLayout, QGridLayout
from PyQt5 import QtGui
from PyQt5 import QtCore


class Window (QDialog):
    def __init__(self):
        super().__init__()

        self.title = "PyQt5 Grid Layout"
        self.top = 200
        self.left = 500
        self.width = 400
        self.height = 100
        self.iconName = "Onur_Karaguler.png"

        self.InitWindow()

    def InitWindow (self):
        self.setWindowTitle(self.title)
        self.setWindowIcon(QtGui.QIcon(self.iconName))
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.CreateLayout()
        vbox = QVBoxLayout ()
        vbox.addWidget(self.groupBox)

        self.setLayout(vbox)

        self.show()

    def CreateLayout (self):
        self.groupBox = QGroupBox ("What Is Your Favorite Programmin Language?")
        gridLayout = QGridLayout ()

        button = QPushButton ("Python",self)
        button.setIcon(QtGui.QIcon("Onur_Karaguler.png"))
        button.setIconSize(QtCore.QSize(40,40))
        button.setMaximumHeight(40)
        gridLayout.addWidget(button, 0,0)

        button1 = QPushButton ("C++",self)
        button1.setIcon(QtGui.QIcon("Onur_Karaguler.png"))
        button1.setIconSize(QtCore.QSize(40,40))
        button1.setMaximumHeight(40)
        gridLayout.addWidget(button1, 0,1)

        button2 = QPushButton ("Java",self)
        button2.setIcon(QtGui.QIcon("Onur_Karaguler.png"))
        button2.setIconSize(QtCore.QSize(40,40))
        button2.setMaximumHeight(40)
        gridLayout.addWidget(button2, 1,0)

        button3 = QPushButton ("C#",self)
        button3.setIcon(QtGui.QIcon("Onur_Karaguler.png"))
        button3.setIconSize(QtCore.QSize(40,40))
        button3.setMaximumHeight(40)
        gridLayout.addWidget(button3, 1,1)

        self.groupBox.setLayout(gridLayout)

if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window ()   # () koyman gerek
    sys.exit(App.exec())