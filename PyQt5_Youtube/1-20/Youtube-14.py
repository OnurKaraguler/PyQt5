# https://www.youtube.com/watch?v=IXjNGRCCfxw&list=PL1FgJUcJJ03uO70zDLDF3oaTu6s2QLOPa&index=14

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout,QVBoxLayout, QRadioButton, QGroupBox
from PyQt5 import QtGui

class Window (QWidget):
    def __init__(self):
        super().__init__()

        self.title = "PyQt5 QGroupBox"
        self.left = 500
        self.top = 200
        self.width = 300
        self.height = 250
        self.iconName = "Onur_Karaguler.png"

        self.setWindowTitle(self.title)
        self.setWindowIcon(QtGui.QIcon(self.iconName))
        self.setGeometry(self.left, self.top, self.width, self.height)

        groupbox = QGroupBox ("Select Your Favorite Fruit")
        groupbox.setFont(QtGui.QFont("Sanserif",15))

        hbox = QHBoxLayout()
        hbox.addWidget(groupbox)
        self.setLayout(hbox)

        vbox = QVBoxLayout ()

        rad1 = QRadioButton ("Apple")
        vbox.addWidget(rad1)

        rad2 = QRadioButton ("Banana")
        vbox.addWidget(rad2)

        rad3 = QRadioButton ("Melon")
        vbox.addWidget(rad3)

        groupbox.setLayout(vbox)

        self.show()


if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())