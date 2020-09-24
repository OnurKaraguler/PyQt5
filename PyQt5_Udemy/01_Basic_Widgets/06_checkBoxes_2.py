import sys, os
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt


class Main(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('RadioButton Demo')
        self.setGeometry(500,150,300,300)
        self.setFixedSize(self.size())          #Ekran ölçüsünü sabitlemek için
        self.UI()
        self.show()

    def UI(self):
        self.window()

    def window(self):
        self.b1 = QCheckBox("Button1")
        self.b1.setChecked(True)
        self.b1.stateChanged.connect(lambda: self.btnstate(self.b1))

        self.b2 = QCheckBox("Button2")
        self.b2.toggled.connect(lambda: self.btnstate(self.b2))


        self.layout = QVBoxLayout()
        self.layout.addWidget(self.b1)
        self.layout.addWidget(self.b2)


        self.mainLayout = QHBoxLayout()
        self.mainLayout.addLayout(self.layout)
        self.setLayout(self.mainLayout)

    def btnstate(self, b):
        if b.text() == "Button1":
            if b.isChecked() == True:
                print(b.text() + " is selected")
        else:
            print(b.text() + " is deselected")
            if b.text() == "Button2":
                if b.isChecked() == True:
                    print(b.text() + " is selected")
            else:
                print(b.text() + " is deselected")


if __name__=='__main__':
    app = QApplication(sys.argv)
    window = Main()
    sys.exit(app.exec_())