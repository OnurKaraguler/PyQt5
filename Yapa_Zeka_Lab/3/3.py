from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSlot
from PyQt5.uic import loadUi

class dersler_3(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("3.ui",self)

        self.pushButton_1.setText("dersler_3")

uygulama = QApplication ([])
pencere = dersler_3()
pencere.show()
uygulama.exec_()