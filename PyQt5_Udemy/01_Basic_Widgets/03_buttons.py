import sys
from PyQt5.QtWidgets import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Using Buttons')
        self.setGeometry(500,200,350,350)
        self.UI()

    def UI(self):
        self.text = QLabel('My Text', self)
        self.text.move(160,50)
        enterButton = QPushButton('Enter',self)
        enterButton.move(100, 80)
        enterButton.clicked.connect(self.enterFunc)
        exitButton = QPushButton('Exit', self)
        exitButton.move(200, 80)
        exitButton.clicked.connect(self.exitFunc)

    def enterFunc(self):
        self.text.setText('You clicked Enter')
        self.text.resize(150,20)

    def exitFunc(self):
        self.text.setText('You clicked Exit')
        self.text.resize(150,20)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
