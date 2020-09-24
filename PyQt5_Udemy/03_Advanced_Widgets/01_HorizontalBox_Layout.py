import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont



font = QFont('Times', 14)

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('HorizontalBox Layout')
        self.setGeometry(350,150,400,300)
        self.UI()

    def UI(self):
        hbox = QHBoxLayout()
        btn1 = QPushButton('Button1')
        btn2 = QPushButton('Button2')
        btn3 = QPushButton('Button2')
        hbox.addStretch()
        hbox.addWidget(btn1)
        hbox.addWidget(btn2)
        hbox.addWidget(btn3)
        hbox.addStretch()

        self.setLayout(hbox)





if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())