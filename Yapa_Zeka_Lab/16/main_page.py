from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi

from second_page import SecondPage

class MainPage(QMainWindow):

    def __init__(self):
        super().__init__()

        loadUi("main_page.ui",self)

        self.pushButton_2nd_page.clicked.connect(self.open_second_page)

        self.second_page = SecondPage()

    def open_second_page (self):
        self.second_page.show()

