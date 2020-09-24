from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSlot
from eightv2 import Ui_MainWindow


class dersler_8V3(QMainWindow):
    def __init__(self):
        super().__init__()


        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

    @pyqtSlot(int)
    def on_horizontalSlider_valueChanged(self,index):

        self.ui.label.setText("Değer = " + str(index))

uygulama = QApplication ([])
pencere = dersler_8V3()
pencere.show()
uygulama.exec_()