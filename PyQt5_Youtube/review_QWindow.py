import sys
from PyQt5.QtWidgets import QMainWindow,QApplication, QPushButton, QGroupBox, QHBoxLayout, QVBoxLayout
from PyQt5 import QtGui   # pencerenin logosunu değiştirmek için
from PyQt5.QtCore import QRect
from PyQt5 import QtCore

class Window (QMainWindow):
    def __init__(self):
        super ().__init__()

        self.title = "PyQt5 Push Button"
        self.top = 200
        self.left = 500
        self.width = 500
        self.height =500
        self.iconName = "Onur_Karaguler.png"

        self.initWindow()       # Pencereyi boyutlandırmak için

        self.UiComponents()     # PushButton için
        self.UiComponents2()    # PushButton'a reesim eklemek için
        self.UiComponents3()    # PushButton'a reesim eklemek için
        self.UiComponents4()    # PushButton'a reesim eklemek için

        self.show ()

    def initWindow(self):
        self.setWindowTitle(self.title)
        self.setWindowIcon(QtGui.QIcon(self.iconName))
        self.setGeometry(self.left, self.top, self.width, self.height)

    def UiComponents(self):
        button = QPushButton ("Click Me",self)
        #button.move (50,50)   # PushButton pozisyonu
        button.setGeometry(QRect(100,75,110,50))   # PushButton posisyon ve ölçüleri


    def UiComponents2(self):
        button2 = QPushButton("Click Me", self)
        button2.setGeometry(QRect(100,150,110,50))
        button2.setIcon(QtGui.QIcon("Onur_Karaguler.png"))      # Butona ikon/resim ekleme
        button2.setIconSize(QtCore.QSize(40,40))
        button2.setToolTip("<h2>This is click me button<h2>")   # Butonun üzerinde beklediğinde

    def UiComponents3(self):
        button3 = QPushButton("Onur Karagüler", self)
        button3.setGeometry(QRect(100, 225, 110, 50))
        button3.clicked.connect(self.ClickMe)

    def ClickMe(self):
        print("Onur Karagüler")

    def UiComponents4(self):
        button4 = QPushButton("Close Me", self)
        button4.setGeometry(QRect(100, 300, 110, 50))
        button4.clicked.connect(self.CloseMe)

    def CloseMe(self):
        sys.exit()



if __name__ == "__main__":
    app = QApplication (sys.argv)
    window = Window ()
    sys.exit(app.exec())