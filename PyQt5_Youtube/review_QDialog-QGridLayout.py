import sys
from PyQt5.QtWidgets import QDialog,QApplication, QPushButton, QGroupBox, QGridLayout, QVBoxLayout
from PyQt5 import QtGui
from PyQt5 import QtCore

class Window (QDialog):
    def __init__(self):
        super ().__init__()

        self.title = "PyQt5 Push Button"
        self.top = 200
        self.left = 500
        self.width = 500
        self.height =100
        self.iconName = "Onur_Karaguler.png"

        self.initWindow()       # Pencereyi boyutlandırmak için

        self.createLayout()     # Zemini oluşturdun
        vbox = QVBoxLayout()
        vbox.addWidget(self.groupbox)
        self.setLayout(vbox)

        self.show ()

    def initWindow(self):
        self.setWindowTitle(self.title)
        self.setWindowIcon(QtGui.QIcon(self.iconName))
        self.setGeometry(self.left, self.top, self.width, self.height)

    def createLayout (self):
        self.groupbox = QGroupBox ("Click on a button...")
        gridlayout = QGridLayout()

        button = QPushButton ("Click Me",self)
        button.setMaximumHeight(40)
        button.setMaximumWidth(100)
        gridlayout.addWidget(button,0,0)

        button2 = QPushButton("Click Me", self)
        button2.setIcon(QtGui.QIcon("Onur_Karaguler.png"))      # Butona ikon/resim ekleme
        button2.setIconSize(QtCore.QSize(40,40))
        button2.setToolTip("<h2>This is click me button<h2>")   # Butonun üzerinde beklediğinde
        button2.setMaximumHeight(40)
        button2.setMaximumWidth(100)
        gridlayout.addWidget(button2,0,1)

        button3 = QPushButton("Onur Karagüler", self)
        button3.clicked.connect(self.ClickMe)
        button3.setMaximumHeight(40)
        button3.setMaximumWidth(100)
        gridlayout.addWidget(button3,1,0)

        button4 = QPushButton("Close Me", self)
        button4.clicked.connect(self.CloseMe)
        button4.setMaximumHeight(40)
        button4.setMaximumWidth(100)
        gridlayout.addWidget(button4,1,1)

        self.groupbox.setLayout(gridlayout)

    def ClickMe(self):
        print("Onur Karagüler")


    def CloseMe(self):
        sys.exit()


if __name__ == "__main__":
    app = QApplication (sys.argv)
    window = Window ()
    sys.exit(app.exec())