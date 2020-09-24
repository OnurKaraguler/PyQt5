from PyQt5.QtWidgets import *
from third_page_2 import Ui_MainWindow


class ThirdPage(QMainWindow):

    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)