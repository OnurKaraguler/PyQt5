# https://www.youtube.com/watch?v=rr17NJCUrlE&list=PL1FgJUcJJ03uO70zDLDF3oaTu6s2QLOPa&index=13&frags=wn
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QLabel, QButtonGroup, QPushButton
from PyQt5 import QtGui
from PyQt5 import QtCore

class Window (QWidget):
    def __init__(self):
        super().__init__()

        self.title = "PyQt5 QButton Group"
        self.left = 500
        self.top = 200
        self.width = 300
        self.height = 250
        self.iconName = "Onur_Karaguler.png"

        self.setWindowTitle(self.title)
        self.setWindowIcon(QtGui.QIcon(self.iconName))
        self.setGeometry(self.left, self.top, self.width, self.height)

        hbox = QHBoxLayout ()

        self.label = QLabel (self)
        self.label.setFont(QtGui.QFont("Sanserif",20))
        hbox.addWidget(self.label)

        self.buttongroup = QButtonGroup ()
        self.buttongroup.buttonClicked[int].connect(self.on_button_clicked)

        button = QPushButton ("Python")
        self.buttongroup.addButton(button,1)
        button.setFont(QtGui.QFont("Sanserif",15))
        button.setIcon(QtGui.QIcon("Python.png"))
        button.setIconSize(QtCore.QSize(40,40))
        hbox.addWidget(button)

        button = QPushButton ("Java")
        self.buttongroup.addButton(button,2)
        button.setFont(QtGui.QFont("Sanserif",15))
        button.setIcon(QtGui.QIcon("Java.png"))
        button.setIconSize(QtCore.QSize(40,40))
        hbox.addWidget(button)

        button = QPushButton ("C++")
        self.buttongroup.addButton(button,3)
        button.setFont(QtGui.QFont("Sanserif",15))
        button.setIcon(QtGui.QIcon("C++.png"))
        button.setIconSize(QtCore.QSize(40,40))
        hbox.addWidget(button)

        self.setLayout(hbox)

        self.show()

    def on_button_clicked(self,id):
        for button in self.buttongroup.buttons():
            if button is self.buttongroup.button(id):
                self.label.setText(button.text() + " Was Clicked")


if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())