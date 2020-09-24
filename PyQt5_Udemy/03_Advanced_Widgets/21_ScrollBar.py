import sys, os
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
from PIL import Image


class Main(QWidget):
    count = 0
    def __init__(self,parent=None):
        super(Main, self).__init__(parent)
        self.setWindowTitle('QSplitter demo')
        self.setGeometry(500,150,400,400)
        # self.setFixedSize(self.size())
        self.UI()
        self.show()

    def UI(self):
        self.window()

    def window(self):
        self.vbox = QVBoxLayout()
        self.hbox = QHBoxLayout()
        self.l1 = QLabel("Drag scrollbar sliders to change color")
        self.l1.setFont(QFont("Arial", 16))

        self.hbox.addWidget(self.l1)
        self.s1 = QScrollBar()
        self.s1.setMaximum(255)
        self.s1.sliderMoved.connect(self.sliderval)
        self.s2 = QScrollBar()
        self.s2.setMaximum(255)
        self.s2.sliderMoved.connect(self.sliderval)
        self.s3 = QScrollBar()
        self.s3.setMaximum(255)
        self.s3.sliderMoved.connect(self.sliderval)
        self.hbox.addWidget(self.s1)
        self.hbox.addWidget(self.s2)
        self.hbox.addWidget(self.s3)

        self.mainLayout = QVBoxLayout()
        self.mainLayout.addLayout(self.vbox)
        self.mainLayout.addLayout(self.hbox)
        self.setLayout(self.mainLayout)

    def sliderval(self):
        print(self.s1.value(), self.s2.value(), self.s3.value())

        palette = QPalette()
        c = QColor(self.s1.value(), self.s2.value(), self.s3.value(), 255)
        palette.setColor(QPalette.Foreground, c)
        self.l1.setPalette(palette)

if __name__=='__main__':
    app = QApplication(sys.argv)
    window = Main()
    sys.exit(app.exec_())