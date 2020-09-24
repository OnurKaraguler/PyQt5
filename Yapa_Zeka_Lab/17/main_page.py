from PyQt5.QtWidgets import *
from main_page_2 import Ui_MainWindow

from second_page import SecondPage
from third_page import ThirdPage

class MainPage(QMainWindow):

    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton_2nd_page.clicked.connect(self.open_2nd_page)
        self.ui.pushButton_3rd_page.clicked.connect(self.open_3nd_page)

        self.second_page = SecondPage()
        self.third_page = ThirdPage()

    def open_2nd_page(self):
        self.second_page.show()

    def open_3nd_page(self):
        self.third_page.show()
