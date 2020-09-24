import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont

font = QFont('Times', 16)

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Using SpinBox')
        self.setGeometry(250,150,500,500)
        self.UI()

    def UI(self):
        self.spinBox = QSpinBox(self)
        self.spinBox.move(150, 100)
        self.spinBox.setFont(font)
        # self.spinBox.setMinimum(25)
        # self.spinBox.setMaximum(110)
        self.spinBox.setRange(25,110)
        # self.spinBox.setPrefix('$')
        self.spinBox.setSuffix('cm')
        self.spinBox.setSingleStep(5)
        self.spinBox.valueChanged.connect(self.getValue)
        button = QPushButton('Send', self)
        button.move(150,140)
        button.clicked.connect(self.getValue2)

    def getValue(self):
        value = self.spinBox.value()
        print(value)

    def getValue2(self):
        value = self.spinBox.value()
        print(value)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
