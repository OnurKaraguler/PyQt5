import sys
from PyQt5.QtWidgets import QDialog, QPushButton, QApplication, QGroupBox, QHBoxLayout, QVBoxLayout
from PyQt5 import QtGui
from PyQt5.QtCore import QRect
from PyQt5 import QtCore

# The QDialog class is the base class of dialog windows. A dialog window is a top-level window mostly used
# for short-term tasks and brief communications with the user. QDialogs may be modal or modeless.
# QDialogs can provide a return value, and they can have default buttons.

class Window (QDialog):
    def __init__(self):
        super().__init__()

        self.title = "PyQt5 Layout Management"
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

        self.createLayout()
        vbox = QVBoxLayout ()
        vbox.addWidget(self.groupBox)  # Bu satır olmadığında pencere oluşuyor ancak
        self.setLayout(vbox)

        self.show()

    def createLayout (self):
        self.groupBox = QGroupBox ("What Is Your Favorite Sport?")
        hboxlayout = QHBoxLayout ()

        button = QPushButton ("Football",self)
        button.setGeometry(QRect(100,100,150,50))
        button.setIcon(QtGui.QIcon("Onur_Karaguler.png"))
        button.setIconSize(QtCore.QSize(40,40))
        button.setMaximumHeight(40)   # Butonun maksimum yüksekliği
        button.setMaximumWidth(100)   # Butonun maksimum genişliği
        hboxlayout.addWidget(button)   # Pencere boyutu değiştiğinde kendini adapte eder

        button1 = QPushButton ("Cricket",self)
        button1.setIcon(QtGui.QIcon("Onur_Karaguler.png"))
        button1.setIconSize(QtCore.QSize(40,40))
        button1.setMaximumHeight(40)
        button1.setMaximumWidth(100)
        hboxlayout.addWidget(button1)

        button2 = QPushButton ("Tennis",self)
        button2.setIcon(QtGui.QIcon("Onur_Karaguler.png"))
        button2.setIconSize(QtCore.QSize(40,40))
        button2.setMaximumHeight(40)
        button2.setMaximumWidth(100)
        hboxlayout.addWidget(button2)


        self.groupBox.setLayout(hboxlayout)

if __name__ == "__main__":
    App = QApplication (sys.argv)
    window = Window()
    sys.exit(App.exec())