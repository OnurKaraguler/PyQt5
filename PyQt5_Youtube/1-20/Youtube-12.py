# https://www.youtube.com/watch?v=4-nwosP-sDw&list=PL1FgJUcJJ03uO70zDLDF3oaTu6s2QLOPa&index=12
import sys
from PyQt5.QtWidgets import QApplication, QLineEdit, QWidget, QHBoxLayout, QLabel
from PyQt5 import QtGui

class Window (QWidget):
    def __init__(self):
        super().__init__()

        self.title = "PyQt5 Line Edit"
        self.left = 500
        self.top = 200
        self.width = 300
        self.height = 250
        self.iconName = "Onur_Karaguler.png"

        self.setWindowTitle(self.title)
        self.setWindowIcon(QtGui.QIcon(self.iconName))
        self.setGeometry(self.left, self.top, self.width, self.height)

        hbox = QHBoxLayout()

        self.lineedit = QLineEdit (self)
        self.lineedit.setFont(QtGui.QFont("Sanserif",15))
        self.lineedit.returnPressed.connect(self.onPressed)  # returnPressed
        hbox.addWidget (self.lineedit)

        self.label = QLabel(self)
        self.label.setFont(QtGui.QFont("Sanserif",15))
        hbox.addWidget (self.label)


        self.setLayout(hbox)

        self.show()

    def onPressed(self):
        self.label.setText(self.lineedit.text())


if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())