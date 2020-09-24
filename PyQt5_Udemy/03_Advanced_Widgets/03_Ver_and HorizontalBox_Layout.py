import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont

font = QFont('Times', 14)

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Ver_and HorizontalBox_Layout')
        self.setGeometry(350,150,400,300)
        self.UI()

    def UI(self):
        mainLayout = QVBoxLayout()
        topLayout = QHBoxLayout()
        bottomLayout = QHBoxLayout()
        mainLayout.addLayout(topLayout)
        mainLayout.addLayout(bottomLayout)

        cbox = QCheckBox()
        rbtn = QRadioButton()
        combo = QComboBox()
        btn1 = QPushButton()
        btn2 = QPushButton()

        topLayout.setContentsMargins(150,10,20,20)      #left, top, right, bottom
        topLayout.addWidget(cbox)
        topLayout.addWidget(rbtn)
        topLayout.addWidget(combo)
        bottomLayout.setContentsMargins(150, 10,150,10)
        bottomLayout.addWidget(btn1)
        bottomLayout.addWidget(btn2)


        self.setLayout(mainLayout)





if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())