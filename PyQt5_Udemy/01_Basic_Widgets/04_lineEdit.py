import sys
from PyQt5.QtWidgets import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Using lineEdits')
        self.setGeometry(500,200,350,350)
        self.UI()

    def UI(self):
        self.nameTextBox = QLineEdit(self)
        self.nameTextBox.setPlaceholderText('Please enter you name')
        self.nameTextBox.move(120,50)
        self.passTextBox = QLineEdit(self)
        self.passTextBox.setPlaceholderText('please enter your password')
        self.passTextBox.setEchoMode(QLineEdit.Password)
        self.passTextBox.move(120,80)
        button = QPushButton('Save', self)
        button.move(170,110)
        button.clicked.connect(self.getValues)

    def getValues(self):
        name = self.nameTextBox.text()
        password = self.passTextBox.text()
        self.setWindowTitle("Your name is: "+ name+ " Your password is: "+ password)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
