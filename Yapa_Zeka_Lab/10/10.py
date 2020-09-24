from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from ten import Ui_MainWindow
from PyQt5.uic import loadUi

class dersler_10(QMainWindow):
    def __init__(self):
        super().__init__()


        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.action_blue.triggered.connect(self.blue_selected)
        self.ui.action_red.triggered.connect(self.red_selected)
        self.ui.action_green.triggered.connect(self.green_selected)
        self.ui.action_yellow.triggered.connect(self.yellow_selected)
        self.ui.action_black_white.toggled[bool].connect(self.black_white_selected)

    def blue_selected(self):
        self.ui.label_show.setText("Mavi renk seçildi")
        self.ui.label_show.setStyleSheet("color:rgb(0,0,255)")
        self.ui.frame_show.setStyleSheet("border-image: url(:/icons/icons/2.png);")

    def red_selected(self):
        self.ui.label_show.setText("Kırmızı renk seçildi")
        self.ui.label_show.setStyleSheet("color:rgb(255,0,0)")
        self.ui.frame_show.setStyleSheet("border-image: url(:/icons/icons/Oyun_1.png);")

    def green_selected(self):
        self.ui.label_show.setText("Yeşil renk seçildi")
        self.ui.label_show.setStyleSheet("color:rgb(0,150,0)")
        self.ui.frame_show.setStyleSheet("border-image: url(:/icons/icons/4.png);")

    def yellow_selected(self):
        self.ui.label_show.setText("Sarı renk seçildi")
        self.ui.label_show.setStyleSheet("color:rgb(255,150,0)")
        self.ui.frame_show.setStyleSheet("border-image: url(:/icons/icons/7.png);")

    def black_white_selected(self,state):
        if (state == True):
            self.ui.label_show.setText("Siyah renk seçildi")
            self.ui.label_show.setStyleSheet("color:rgb(0,0,0)")
            self.ui.frame_show.setStyleSheet("border-image: url(:/icons/icons/3.png);")
            self.ui.action_black_white.setText("Beyaz")
            self.ui.action_black_white.setIcon(QIcon(":/icons/icons/6.png"))
            self.ui.action_black_white.setToolTip("Beyaz kuşu seç")
        else:
            self.ui.label_show.setText("Beyaz renk seçildi")
            self.ui.label_show.setStyleSheet("color:rgb(0,0,0)")
            self.ui.frame_show.setStyleSheet("border-image: url(:/icons/icons/6.png);")
            self.ui.action_black_white.setText("Siyah")
            self.ui.action_black_white.setIcon(QIcon(":/icons/icons/3.png"))
            self.ui.action_black_white.setToolTip("Siyah kuşu seç")

uygulama = QApplication ([])
pencere = dersler_10()
pencere.show()
uygulama.exec_()