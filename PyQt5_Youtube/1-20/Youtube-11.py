# https://www.youtube.com/watch?v=NARkgTlI3_0&list=PL1FgJUcJJ03uO70zDLDF3oaTu6s2QLOPa&index=11

import sys
from PyQt5.QtWidgets import QApplication, QPushButton, QWidget, QHBoxLayout, QLabel
from PyQt5 import QtGui

class Window (QWidget):
    def __init__(self):
        super().__init__()

        self.title = "PyQt5 WhatIsThis Class"
        self.left = 500
        self.top = 200
        self.width = 300
        self.height = 250
        self.iconName = "Onur_Karaguler.png"

        self.setWindowTitle(self.title)
        self.setWindowIcon(QtGui.QIcon(self.iconName))
        self.setGeometry(self.left, self.top, self.width, self.height)

        hbox = QHBoxLayout()

        label = QLabel("Focus and Press SHIFT + F1")
        hbox.addWidget(label)

        button = QPushButton("Click ME", self)
        button.setWhatsThis("This is a button that you can click on this")
        # SHIFT + F1'e basıldığında bu notu veriyor
        hbox.addWidget(button)

        self.setLayout(hbox)


        self.show()


if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())