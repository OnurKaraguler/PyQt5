import sys, os
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt


class Main(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Input Dialog demo')
        self.setGeometry(500,150,300,300)
        self.setFixedSize(self.size())          #Ekran ölçüsünü sabitlemek için
        self.UI()
        self.show()

    def UI(self):
        self.window()

    def window(self):
        self.btn = QPushButton("Choose from list")
        self.btn.clicked.connect(self.getItem)
        self.btn1 = QPushButton("get name")
        self.btn1.clicked.connect(self.gettext)
        self.btn2 = QPushButton("Enter an integer")
        self.btn2.clicked.connect(self.getint)
        self.btn3 = QPushButton("Enter an float")
        self.btn3.clicked.connect(self.getDouble)

        self.le = QLineEdit()
        self.le1 = QLineEdit()
        self.le2 = QLineEdit()
        self.le3 = QLineEdit()

        self.layout = QFormLayout()
        self.layout.addRow(self.btn,self.le)
        self.layout.addRow(self.btn1,self.le1)
        self.layout.addRow(self.btn2,self.le2)
        self.layout.addRow(self.btn3,self.le3)

        self.mainLayout = QHBoxLayout()
        self.mainLayout.addLayout(self.layout)
        self.setLayout(self.mainLayout)

    def getItem(self):
        items = ("C", "C++", "Java", "Python")

        item, ok = QInputDialog.getItem(self, "select input dialog",
                                    "list of languages", items, 0, False)
        if ok and item:
            self.le.setText(item)

    def gettext(self):
        text, ok = QInputDialog.getText(self, 'Text Input Dialog', 'Enter your name:')

        if ok:
            self.le1.setText(str(text))

    def getint(self):
        num, ok = QInputDialog.getInt(self, "integer input dualog", "enter a number")

        if ok:
            self.le2.setText(str(num))

    def getDouble(self):
        num, ok = QInputDialog.getDouble(self, "float input dualog", "enter a number")

        if ok:
            self.le3.setText(str(num))

if __name__=='__main__':
    app = QApplication(sys.argv)
    window = Main()
    sys.exit(app.exec_())