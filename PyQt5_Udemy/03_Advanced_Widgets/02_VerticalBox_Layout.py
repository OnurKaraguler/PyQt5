import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont



font = QFont('Times', 14)

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('VerticalBox Layout')
        self.setGeometry(350,150,400,300)
        self.UI()

    def UI(self):
        vbox = QVBoxLayout()
        btn1 = QPushButton(''
                           'Save')
        btn2 = QPushButton('Exit')
        btn3 = QPushButton('Hello')
        vbox.addStretch()
        vbox.addWidget(btn1)
        vbox.addWidget(btn2)
        vbox.addWidget(btn3)

        self.setLayout(vbox)





if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())