import sys, os
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt


class Main(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Slider demo')
        self.setGeometry(500,150,300,300)
        self.setFixedSize(self.size())          #Ekran ölçüsünü sabitlemek için
        self.UI()
        self.show()

    def UI(self):
        self.window()

    def window(self):
        self.l1 = QLabel("Hello")
        self.l1.setAlignment(Qt.AlignCenter)

        self.sl = QSlider(Qt.Horizontal)
        self.sl.setMinimum(10)
        self.sl.setMaximum(30)
        self.sl.setValue(20)
        # self.sl.setTickPosition(QSlider.TicksBelow)
        # self.sl.setTickPosition(QSlider.TicksAbove)
        self.sl.setTickPosition(QSlider.TicksLeft)
        # self.sl.setTickPosition(QSlider.TicksRight)
        # self.sl.setTickPosition(QSlider.TicksBothSides)
        self.sl.setTickInterval(5)
        self.sl.setValue(20)
        # self.sl.valueChanged.connect(self.valuechange)
        # self.sl.sliderPressed.connect(self.sliderchange)
        # self.sl.sliderMoved.connect(self.slidermoved)
        self.sl.sliderReleased.connect(self.sliderreleased)


        self.layout = QVBoxLayout()
        self.layout.addWidget(self.l1)
        self.layout.addWidget(self.sl)

        self.mainLayout = QHBoxLayout()
        self.mainLayout.addLayout(self.layout)
        self.setLayout(self.mainLayout)

    # def valuechange(self):
    #     size = self.sl.value()
    #     print(size)

        # self.l1.setFont(QFont("Arial", size))

    # def sliderchange(self):
    #     size = self.sl.value()
    #     print(size)

    # def slidermoved(self):
    #     size = self.sl.value()
    #     print(size)

    def sliderreleased(self):
        size = self.sl.value()
        print(size)

if __name__=='__main__':
    app = QApplication(sys.argv)
    window = Main()
    sys.exit(app.exec_())