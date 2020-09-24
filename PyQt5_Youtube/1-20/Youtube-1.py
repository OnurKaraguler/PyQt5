import sys
from PyQt5.QtWidgets import QMainWindow,QApplication
from PyQt5 import QtGui   # pencerenin logosunu değiştirmek için


class Window (QMainWindow):
    def __init__(self):
        super ().__init__()

        self.title = "PyQt5 Window"
        self.top = 100
        self.left = 100
        self.width = 400
        self.height =300

        self.initWindow()

    def initWindow (self):
        self.setWindowIcon(QtGui.QIcon ("Onur_Karaguler.png"))   #Pencere logosu
        self.setWindowTitle(self.title)
        self.setGeometry(self.left,self.top, self.width, self.height)

        self.show()

App = QApplication (sys.argv)
window = Window()
sys.exit(App.exec())
