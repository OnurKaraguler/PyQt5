from PyQt5.QtWidgets import *
from eight import Ui_MainWindow
from PyQt5.uic import loadUi

class dersler_8(QMainWindow):
    def __init__(self):
        super().__init__()


        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

    def benim_slot(self,index):

        self.ui.label.setText("Değer = " + str(index))

uygulama = QApplication ([])
pencere = dersler_8()
pencere.show()
uygulama.exec_()