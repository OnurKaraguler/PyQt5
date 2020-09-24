from PyQt5.QtWidgets import *
from nein import Ui_MainWindow
from PyQt5.uic import loadUi

class dersler_9(QMainWindow):
    def __init__(self):
        super().__init__()


        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.action_blue.triggered.connect(self.blue_selected)
        self.ui.action_red.triggered.connect(self.red_selected)
        self.ui.action_green.triggered.connect(self.green_selected)

    def blue_selected(self):
        print("Mavi seçildi")

    def red_selected(self):
        print("Kırmızı seçildi")

    def green_selected(self):
        print("Yeşil seçildi")

uygulama = QApplication ([])
pencere = dersler_9()
pencere.show()
uygulama.exec_()