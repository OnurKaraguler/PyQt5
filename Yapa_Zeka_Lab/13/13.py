from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QIntValidator
from thirteen import Ui_MainWindow
from PyQt5.uic import loadUi

class dersler_13(QMainWindow):


    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.lineEdit_signal_slot.returnPressed.connect(self.process)
        self.ui.lineEdit_read.returnPressed.connect(self.process)

        self.ui.lineEdit_only_integer.setValidator(QIntValidator(0,10,self))

    def process(self):
        received_text = self.ui.lineEdit_signal_slot.text()
        received_text_2 = self.ui.lineEdit_read.text()

        print("alınan yazı : ", received_text + " " + received_text_2)

        self.ui.lineEdit_write.setText(received_text + " " + received_text_2)

        self.ui.lineEdit_signal_slot.clear()
        self.ui.lineEdit_read.clear()


uygulama = QApplication ([])
pencere = dersler_13()
pencere.show()
uygulama.exec_()