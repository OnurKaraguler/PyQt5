# https://www.youtube.com/watch?v=xff2_XeFipc&list=PL1FgJUcJJ03uO70zDLDF3oaTu6s2QLOPa&index=16
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QFrame,QHBoxLayout, QPushButton
from PyQt5 import QtGui

class Window (QWidget):
    def __init__(self):
        super().__init__()

        self.title = "PyQt5 Frame"
        self.left = 500
        self.top = 200
        self.width = 300
        self.height = 250
        self.iconName = "Onur_Karaguler.png"

        self.setWindowTitle(self.title)
        self.setWindowIcon(QtGui.QIcon(self.iconName))
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setStyleSheet('background-color:yellow')

        hbox = QHBoxLayout()

        btn = QPushButton ("Click Me")
        btn.setStyleSheet('color:white')
        btn.setStyleSheet('background-color:green')

        frame = QFrame ()
        frame.setFrameShape(QFrame.StyledPanel)
        frame.setStyleSheet('background-color:red')
        frame.setLineWidth(0.6)


        hbox.addWidget(frame)
        hbox.addWidget(btn)

        self.setLayout(hbox)


        self.show()

if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())