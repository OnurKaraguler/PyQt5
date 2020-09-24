# https://www.youtube.com/watch?v=GwnGmCdKbAg&list=PL1FgJUcJJ03uO70zDLDF3oaTu6s2QLOPa&index=18
import sys
from PyQt5.QtWidgets import QApplication, QWidget,QSlider, QLabel,QHBoxLayout
from PyQt5 import QtGui
from PyQt5.QtCore import Qt

class Window (QWidget):
    def __init__(self):
        super().__init__()

        self.title = "PyQt5 Sliders"
        self.left = 500
        self.top = 200
        self.width = 300
        self.height = 250
        self.iconName = "Onur_Karaguler.png"

        self.setWindowTitle(self.title)
        self.setWindowIcon(QtGui.QIcon(self.iconName))
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setStyleSheet('background-color:green')

        hbox = QHBoxLayout()

        self.slider = QSlider()
        self.slider.setOrientation(Qt.Horizontal)
        self.slider.setTickPosition(QSlider.TicksBelow)
        self.slider.setTickInterval(10)
        self.slider.setMinimum(0)
        self.slider.setMaximum(100)
        self.slider.valueChanged.connect(self.changedValue)

        self.label = QLabel ("0")
        self.label.setFont(QtGui.QFont("Sanserif",15) )

        hbox.addWidget(self.slider)
        hbox.addWidget(self.label)

        self.setLayout(hbox)

        self.show()

    def changedValue(self):
        size = self.slider.value()
        self.label.setText(str(size))

App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())