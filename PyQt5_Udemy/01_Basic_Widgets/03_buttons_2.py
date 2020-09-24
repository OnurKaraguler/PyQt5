import sys, os
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt


class Main(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Button demo')
        self.setGeometry(500,150,300,300)
        self.setFixedSize(self.size())          #Ekran ölçüsünü sabitlemek için
        self.UI()
        self.show()

    def UI(self):
        self.window()

    def window(self):
        self.b1 = QPushButton("Button1")
        self.b1.setCheckable(True)
        self.b1.toggle()
        self.b1.clicked.connect(lambda: self.whichbtn(self.b1))
        self.b1.clicked.connect(self.btnstate)

        self.b2 = QPushButton("Button2")
        self.b2.setIcon(QIcon(QPixmap("images/1.png")))
        self.b2.clicked.connect(lambda: self.whichbtn(self.b2))

        self.b3 = QPushButton("Disabled")
        self.b3.setEnabled(False)

        self.b4 = QPushButton("&Default")
        self.b4.setDefault(True)
        self.b4.clicked.connect(lambda: self.whichbtn(self.b4))


        self.layout = QVBoxLayout()
        self.layout.addWidget(self.b1)
        self.layout.addWidget(self.b2)
        self.layout.addWidget(self.b3)
        self.layout.addWidget(self.b4)


        self.mainLayout = QHBoxLayout()
        self.mainLayout.addLayout(self.layout)
        self.setLayout(self.mainLayout)


    def btnstate(self):
        if self.b1.isChecked():
            print("button pressed")
        else:
            print("button released")

    def whichbtn(self, b):
        print("clicked button is " + b.text())

    def isChecked(self):
        print("clicked button is checked")

if __name__=='__main__':
    app = QApplication(sys.argv)
    window = Main()
    sys.exit(app.exec_())