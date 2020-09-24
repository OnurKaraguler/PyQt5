#https://www.youtube.com/watch?v=TXZkHy2koyo&list=PL1FgJUcJJ03uO70zDLDF3oaTu6s2QLOPa&index=20
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QDial, QLabel, QVBoxLayout
from PyQt5 import QtGui

class Window (QWidget):
    def __init__(self):
        super().__init__()

        self.title = "PyQt5 QDial"
        self.left = 500
        self.top = 200
        self.width = 300
        self.height = 250
        self.iconName = "Onur_Karaguler.png"

        self.setWindowTitle(self.title)
        self.setWindowIcon(QtGui.QIcon(self.iconName))
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.label = QLabel (self)
        self.label.setFont(QtGui.QFont("Sanserif",15))

        vbox = QVBoxLayout()
        self.dial = QDial()
        self.dial.setMinimum(0)
        self.dial.setMaximum(100)
        self.dial.setValue(30)
        self.dial.valueChanged.connect(self.dial_changed)

        vbox.addWidget(self.dial)
        vbox.addWidget(self.label)
        self.setLayout(vbox)

        self.show()

    def dial_changed(self):
        getValue = self.dial.value()
        self.label.setText("Dial is changing " + str(getValue))

App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())