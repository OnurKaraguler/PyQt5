# https://www.youtube.com/watch?v=0WgllDCdAl8&list=PL1FgJUcJJ03uO70zDLDF3oaTu6s2QLOPa&index=8

import sys
from PyQt5.QtWidgets import QApplication, QLabel, QDialog, QVBoxLayout
from PyQt5 import QtGui
from PyQt5.QtGui import QPixmap   # Resim eklemek için

class Window (QDialog):
    def __init__(self):
        super().__init__()

        self.title = "PyQt5 Window"
        self.left = 500
        self.top = 200
        self.width = 500
        self.height = 400
        self.iconName = "Onur_Karaguler.png"

        self.InitWindow()

    def InitWindow (self):
        self.setWindowIcon(QtGui.QIcon(self.iconName))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        vbox = QVBoxLayout ()
        labelImage = QLabel (self)
        pixmap = QPixmap ("Onur_Karaguler.png")
        labelImage.setPixmap(pixmap)

        vbox.addWidget(labelImage)

        self.setLayout(vbox)

        self.show()



if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window ()
    sys.exit(App.exec())
