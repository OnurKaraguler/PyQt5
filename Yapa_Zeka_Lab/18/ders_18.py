from PyQt5.QtWidgets import *
from mainwindow_python import Ui_mainwindow
from settings import NewPerson

class Ders18 (QMainWindow):

    def __init__(self):
        super().__init__()

        self.ui = Ui_mainwindow()
        self.ui.setupUi(self)

        self.settings_object = NewPerson()

        self.ui.pushButton_add_new_users.clicked.connect(self.open_new_window)

        self.settings_object.new_user_signal.connect(self.add_new_user)

    def open_new_window(self):

        self.settings_object.show()

    def add_new_user(self,name):

        self.ui.comboBox_users.addItem(name)
        self.settings_object.close()

app = QApplication([])
window = Ders18()
window.show()
app.exec_()