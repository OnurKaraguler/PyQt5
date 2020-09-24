import sys
from PyQt5.QtWidgets import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Using RadioButtons')
        self.setGeometry(250,150,500,500)
        self.UI()

    def UI(self):
        self.name = QLineEdit(self)
        self.name.move(150,50)
        self.name.setPlaceholderText('Enter your name')
        self.surname = QLineEdit(self)
        self.surname.move(150,80)
        self.surname.setPlaceholderText('Enter your surname')
        self.male = QRadioButton('Male', self)
        self.male.setChecked(True)          # başlangıçta male seçili olması için
        self.female = QRadioButton('Female', self)
        self.male.move(150,110)
        self.female.move(200,110)
        button = QPushButton('Submit',self)
        button.clicked.connect(self.getValues)
        button.move(200,140)

    def getValues(self):
        name = self.name.text()
        surname = self.surname.text()
        if self.male.isChecked():
            print(name + ' ' + surname + ' You are a male')
        else:
            print(name + ' ' + surname + ' You are a female')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
