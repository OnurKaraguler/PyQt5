import sys
from PyQt5.QtWidgets import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Using CheckBoxes')
        self.setGeometry(500,200,500,500)
        self.UI()

    def UI(self):
        self.name = QLineEdit(self)
        self.name.setPlaceholderText('Enter your name')
        self.surname = QLineEdit(self)
        self.surname.setPlaceholderText('Enter your surname')
        self.name.move(150, 50)
        self.surname.move(150,80)
        self.remember = QCheckBox('remember me', self)
        self.remember.move(150, 110)
        button = QPushButton('Submit', self)
        button.move(200,140)
        button.clicked.connect(self.submit)

    def submit(self):
        if (self.remember.isChecked()):
            print('Name: ' + self.name.text() + '\nSurname: ' + self.surname.text() + '\nRemember me checked')
        else:
            print('Name: ' + self.name.text() + '\nSurname: ' + self.surname.text() + '\nRemember me not checked')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
