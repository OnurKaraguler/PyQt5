from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from eleven import Ui_MainWindow
from PyQt5.uic import loadUi

class dersler_11(QMainWindow):

    duration_time = 2000

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
        self.ui.statusBar.showMessage("Mavi renk seçildi",self.duration_time)
        self.ui.statusBar.setStyleSheet("color:rgb(0,0,255)")
        self.ui.frame_show.setStyleSheet("border-image: url(:/icons/icons/2.png);")

    def red_selected(self):
        self.ui.statusBar.showMessage("Kırmızı renk seçildi",self.duration_time)
        self.ui.statusBar.setStyleSheet("color:rgb(255,0,0)")
        self.ui.frame_show.setStyleSheet("border-image: url(:/icons/icons/Oyun_1.png);")

    def green_selected(self):
        self.ui.statusBar.showMessage("Yeşil renk seçildi",self.duration_time)
        self.ui.statusBar.setStyleSheet("color:rgb(0,150,0)")
        self.ui.frame_show.setStyleSheet("border-image: url(:/icons/icons/4.png);")

    def yellow_selected(self):
        self.ui.statusBar.showMessage("Sarı renk seçildi",self.duration_time)
        self.ui.statusBar.setStyleSheet("color:rgb(255,150,0)")
        self.ui.frame_show.setStyleSheet("border-image: url(:/icons/icons/7.png);")

    def black_white_selected(self,state):
        if (state == True):
            self.ui.statusBar.showMessage("Siyah renk seçildi", self.duration_time)
            self.ui.statusBar.setStyleSheet("color:rgb(0,0,0)")
            self.ui.frame_show.setStyleSheet("border-image: url(:/icons/icons/3.png);")
            self.ui.action_black_white.setText("Beyaz")
            self.ui.action_black_white.setIcon(QIcon(":/icons/icons/6.png"))
            self.ui.action_black_white.setToolTip("Beyaz kuşu seç")
        else:
            self.ui.statusBar.showMessage("Beyaz renk seçildi", self.duration_time)
            self.ui.statusBar.setStyleSheet("color:rgb(0,0,0)")
            self.ui.frame_show.setStyleSheet("border-image: url(:/icons/icons/6.png);")
            self.ui.action_black_white.setText("Siyah")
            self.ui.action_black_white.setIcon(QIcon(":/icons/icons/3.png"))
            self.ui.action_black_white.setToolTip("Siyah kuşu seç")

uygulama = QApplication ([])
pencere = dersler_11()
pencere.show()
uygulama.exec_()