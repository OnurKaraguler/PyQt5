# https://www.youtube.com/watch?v=rr17NJCUrlE&list=PL1FgJUcJJ03uO70zDLDF3oaTu6s2QLOPa&index=13&frags=wn
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QScrollArea
from PyQt5.QtWidgets import QFrame,QSplitter, QLineEdit, QSlider, QDial
from PyQt5 import QtGui
from PyQt5 import QtCore
from PyQt5.QtCore import Qt

class Window (QWidget):
    def __init__(self):
        super().__init__()

        self.title = "PyQt5 QButton Group"
        self.left = 500
        self.top = 200
        self.width = 500
        self.height = 250
        self.iconName = "Onur_Karaguler.png"

        self.setWindowTitle(self.title)
        self.setWindowIcon(QtGui.QIcon(self.iconName))
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.setStyleSheet('background-color:purple')

        hbox = QVBoxLayout ()



        left = QFrame()
        left.setFrameShape(QFrame.StyledPanel)

        bottom = QFrame()
        bottom.setFrameShape(QFrame.StyledPanel)

        splitter1 = QSplitter (Qt.Horizontal)
        splitter1.setStyleSheet('background-color:red')

        splitter2 = QSplitter (Qt.Vertical)
        splitter2.setStyleSheet('background-color:yellow')

        lineedit = QLineEdit()
        lineedit.setStyleSheet("""QLineEdit{background-color: blue; color: white}""")
        lineedit.setFont(QtGui.QFont("Sanserif",15))

        splitter1.addWidget(left)
        splitter1.addWidget(lineedit)
        splitter1.setSizes([200,200])

        splitter2.addWidget(splitter1)
        splitter2.addWidget(bottom)

        button = QPushButton ("Python")
        button.setFont(QtGui.QFont("Sanserif",15))
        button.setIcon(QtGui.QIcon("Python.png"))
        button.setIconSize(QtCore.QSize(40,40))
        hbox.addWidget(button)

        self.slider = QSlider()
        self.slider.setOrientation(Qt.Horizontal)
        self.slider.setTickPosition(QSlider.TicksBelow)
        self.slider.setTickInterval(10)
        self.slider.setMinimum(0)
        self.slider.setMaximum(100)
        self.slider.valueChanged.connect(self.changedValue)

        self.label = QLabel("0")
        self.label.setFont(QtGui.QFont("Sanserif",15))

        self.label2 = QLabel("0")
        self.label2.setFont(QtGui.QFont("Sanserif",15))

        self.dial = QDial()
        self.dial.setMinimum(0)
        self.dial.setMaximum(100)
        self.dial.setValue(30)
        self.dial.valueChanged.connect(self.dialChanged)

        hbox.addWidget(self.dial)
        hbox.addWidget(self.label2)
        hbox.addWidget(self.slider)
        hbox.addWidget(self.label)

        hbox.addWidget(splitter2)

        self.setLayout(hbox)

        self.show()

    def changedValue(self):
        size = self.slider.value()
        self.label.setText(str(size))

    def dialChanged(self):
        getValue = self.dial.value()
        self.label2.setText("Dial is changing " + str(getValue))

if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())

