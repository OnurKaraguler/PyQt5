import sys
from PyQt5.QtWidgets import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Using Labels')
        self.setGeometry(500,200,350,350)
        self.UI()

    def UI(self):
        text1 = QLabel('Hello Python', self)
        text1.move(100,50)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
