from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSignal
from settings_python import Ui_settings

class NewPerson(QWidget):

    new_user_signal = pyqtSignal(str)

    def __init__(self):
        super().__init__()

        self.ui = Ui_settings()
        self.ui.setupUi(self)

        self.ui.pushButton_add.clicked.connect(self.new_name_added)

    def new_name_added(self):
        new_name = self.ui.lineEdit_name.text()
        #print("new name : ", new_name)

        self.new_user_signal.emit(new_name)

    def clear_lineEdit(self):
        self.ui.lineEdit_name.clear()