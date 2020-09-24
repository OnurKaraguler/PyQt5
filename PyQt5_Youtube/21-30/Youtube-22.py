#https://www.youtube.com/watch?v=TXZkHy2koyo&list=PL1FgJUcJJ03uO70zDLDF3oaTu6s2QLOPa&index=20
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QSpinBox, QLabel, QVBoxLayout, QLCDNumber, QPushButton
from PyQt5 import QtGui
from PyQt5.QtCore import Qt
from random import randint

class Window (QWidget):
    def __init__(self):
        super().__init__()

        self.title = "PyQt5 QLCD Number"
        self.left = 500
        self.top = 200
        self.width = 300
        self.height = 250
        self.iconName = "Onur_Karaguler.png"

        self.setWindowTitle(self.title)
        self.setWindowIcon(QtGui.QIcon(self.iconName))
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.setStyleSheet('background-color:#420')

        vbox = QVBoxLayout()

        self.lcd = QLCDNumber()
        vbox.addWidget(self.lcd)
        self.lcd.setStyleSheet("""QLCDNumber{background-color: gray; color : red}""")
        #self.lcd.display(60)

        self.button = QPushButton("Random Number Generator")
        self.button.setFont(QtGui.QFont("sanserif",13))
        self.button.setStyleSheet("""QPushButton{background-color: blue; color : white}""")
        self.button.clicked.connect(self.LCDHandler)
        vbox.addWidget(self.button)

        self.spinBox = QSpinBox()
        self.spinBox.setStyleSheet('background-color:green')
        self.spinBox.valueChanged.connect(self.spin_changed)
        vbox.addWidget(self.spinBox)

        self.label = QLabel()
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setFont(QtGui.QFont("sanserif",15))
        self.label.setStyleSheet('color : red')
        vbox.addWidget(self.label)

        self.setLayout(vbox)

        self.show()

    def spin_changed(self):
        spinValue = self.spinBox.value()
        self.label.setText("Current value is: " + str(spinValue))

    def dial_changed(self):
        getValue = self.dial.value()
        self.label.setText("Dial is changing " + str(getValue))

    def LCDHandler(self):
        random = randint(1,200)
        self.lcd.display(random)

App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())