import sys
from PyQt5.QtWidgets import QMainWindow,QApplication, QPushButton
from PyQt5 import QtGui
from PyQt5.QtCore import QRect
from PyQt5 import QtCore

class Window (QMainWindow):
    def __init__(self):
        super ().__init__()

        title = "PyQt5 Events And Signals"
        top = 200
        left = 500
        width = 300
        height =250
        iconName = "Onur_Karaguler.png"

        self.setWindowTitle(title)
        self.setWindowIcon(QtGui.QIcon(iconName))
        self.setGeometry(left, top, width, height)

        self.CreateButton()
        self.CreateButton2()

        self.show ()


    def CreateButton(self):
        button = QPushButton ("Click Me",self)
        #button.move (50,50)
        button.setGeometry(QRect(100,50,110,50))
        button.setIcon(QtGui.QIcon("Onur_Karaguler.png"))
        button.setIconSize(QtCore.QSize(40,40))
        button.clicked.connect(self.ClickMe)   # Butona tıklandığında bir sinyal oluşturmak

    def CreateButton2(self):
        button = QPushButton ("Close Application",self)
        button.setGeometry(QRect(100,150,110,50))
        button.setIconSize(QtCore.QSize(40,40))
        button.clicked.connect(self.CloseMe)   # Butona tıklandığında bir sinyal oluşturmak

    def ClickMe (self):
        print("Onur Karagüler")   # Butona tıklandığında "Onur Karagüler" yazacaktır

    def CloseMe (self):
        sys.exit()   # Butona tıklandığında program kapatılacaktır.

if __name__ == "__main__":
    app = QApplication (sys.argv)
    window = Window ()
    sys.exit(app.exec())