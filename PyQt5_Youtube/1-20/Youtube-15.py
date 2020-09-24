# https://www.youtube.com/watch?v=bJBwSyHUobg&list=PL1FgJUcJJ03uO70zDLDF3oaTu6s2QLOPa&index=15

import sys
from PyQt5.QtWidgets import QApplication, QWidget,QVBoxLayout, QSizeGrip
from PyQt5 import QtGui
from PyQt5 import QtCore

class Window (QWidget):
    def __init__(self):
        super().__init__()

        self.title = "PyQt5 Frameless Window"
        self.left = 500
        self.top = 200
        self.width = 300
        self.height = 250
        self.iconName = "Onur_Karaguler.png"

        self.setWindowTitle(self.title)
        self.setWindowIcon(QtGui.QIcon(self.iconName))
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setStyleSheet('background-color:yellow')

        flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
        self.setWindowFlags(flags)

        vboxlayout = QVBoxLayout()
        sizegrip = QSizeGrip(self)
        # sizegrip.setVisible(True)
        vboxlayout.addWidget(sizegrip)
        self.setLayout(vboxlayout)

        self.show()

if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())