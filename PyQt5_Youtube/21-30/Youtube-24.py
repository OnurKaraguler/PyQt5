import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QToolBox, QLabel
from PyQt5 import QtGui

class Window (QWidget):
    def __init__(self):
        super().__init__()

        self.title = "PyQt5 ToolBox"
        self.left = 500
        self.top = 200
        self.width = 300
        self.height = 100
        self.iconName = "Onur_Karaguler.png"

        self.setWindowTitle(self.title)
        self.setWindowIcon(QtGui.QIcon(self.iconName))
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setStyleSheet("background-color:green")


        vbox = QVBoxLayout()

        toolbox = QToolBox()
        toolbox.setStyleSheet("background-color:white")
        vbox.addWidget(toolbox)

        label = QLabel()
        toolbox.addItem(label,"Onur Karagüler")

        label = QLabel()
        toolbox.addItem(label,"İlkay Karagüler")

        label = QLabel()
        toolbox.addItem(label,"Umut Karagüler")

        label = QLabel()
        toolbox.addItem(label,"Defne Karagüler")

        self.setLayout(vbox)

        self.show()

App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())