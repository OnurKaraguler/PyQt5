from PyQt5.QtWidgets import *
from nein_2 import Ui_MainWindow

class dersler_9(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.action_blue.triggered.connect(self.blue_selected)
        self.ui.action_red.triggered.connect(self.red_selected)
        self.ui.action_green.triggered.connect(self.green_selected)


    def blue_selected(self):
        #print("Mavi seçildi")
        self.ui.label.setStyleSheet("background-color: white; color : blue")
        self.ui.label.setText("Mavi seçildi")

    def red_selected(self):
        #print("Kırmızı seçildi")
        self.ui.label.setStyleSheet("background-color: white; color : red")
        self.ui.label.setText("Kırmızı seçildi")

    def green_selected(self):
        #print("Yeşil seçildi")
        self.ui.label.setStyleSheet("background-color: white; color : green")
        self.ui.label.setText("Yeşil seçildi")

uygulama = QApplication ([])
pencere = dersler_9()
pencere.show()
uygulama.exec_()