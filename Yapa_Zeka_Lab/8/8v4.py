from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSlot, pyqtSignal
from eightv2 import Ui_MainWindow


class dersler_8V4(QMainWindow):

    my_signal = pyqtSignal (int)

    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.horizontalSlider.valueChanged[int].connect(self.my_signal[int])

        self.my_signal[int].connect(self.my_slot)

    def my_slot(self,index):
        self.ui.label.setText("değer = " + str(index))

uygulama = QApplication ([])
pencere = dersler_8V4()
pencere.show()
uygulama.exec_()