from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QKeySequence
from fourteen import Ui_MainWindow
from PyQt5.uic import loadUi

class dersler_14(QMainWindow):


    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton_name.setText("Yeni isim")
        self.ui.pushButton_close.setIcon(QIcon(":\icons\icons/2.png"))

        self.ui.pushButton_name.setStyleSheet("background-color: rgb(255, 255, 255,0)")

        self.ui.pushButton_open.setToolTip("F6'ya bas")

        self.ui.pushButton_camera.setShortcut(QKeySequence("F5"))

        self.ui.pushButton_start_stop.clicked.connect(self.start_button_clicked_slot)
        self.ui.pushButton_camera.clicked["bool"].connect(self.bool_function)

        self.ui.pushButton_close.pressed.connect(self.pressed_slot)
        self.ui.pushButton_close.released.connect(self.released_slot)

    def start_button_clicked_slot (self):
        print("tuşa basıldı")

    def bool_function (self,state):
        print("state : ", state)

        if state:
            self.ui.pushButton_camera.setText("Stop")

        else:
            self.ui.pushButton_camera.setText("Close")

    def pressed_slot (self):
        self.ui.pushButton_close.setIcon(QIcon(":\icons\icons/3.png"))
        self.ui.pushButton_close.setStyleSheet("background-color: rgb(255,0,0)")

    def released_slot (self):
        self.ui.pushButton_close.setIcon(QIcon(":\icons\icons/4.png"))
        self.ui.pushButton_close.setStyleSheet("background-color: rgb(0,255,0)")

uygulama = QApplication ([])
pencere = dersler_14()
pencere.show()
uygulama.exec_()