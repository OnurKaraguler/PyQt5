from PyQt5.QtWidgets import *
from eightv2 import Ui_MainWindow


class dersler_8V2(QMainWindow):
    def __init__(self):
        super().__init__()


        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.horizontalSlider.valueChanged[int].connect(self.benim_slot)

    def benim_slot(self,index):

        self.ui.label.setText("Değer = " + str(index))

uygulama = QApplication ([])
pencere = dersler_8V2()
pencere.show()
uygulama.exec_()