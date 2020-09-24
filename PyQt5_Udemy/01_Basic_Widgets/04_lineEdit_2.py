import sys, os
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt


class Main(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('QLabel Demo')
        self.setGeometry(500,150,300,300)
        self.setFixedSize(self.size())          #Ekran ölçüsünü sabitlemek için
        self.UI()
        self.show()

    def UI(self):
        self.window()

    def window(self):
        self.e1 = QLineEdit()
        self.e1.setValidator(QIntValidator())         # only number
        # self.e1.setValidator(QRegExpValidator())        # only text
        self.e1.setMaxLength(4)                         # set character
        self.e1.setAlignment(Qt.AlignRight)
        self.e1.setFont(QFont("Arial", 20))

        self.e2 = QLineEdit()
        self.e2.setValidator(QDoubleValidator(0.99, 99.99, 2))

        self.e3 = QLineEdit()
        self.e3.setInputMask('+99_999_9999999')
        print(type(self.e3))

        self.e4 = QLineEdit()
        self.e4.textChanged.connect(self.textchanged)

        self.e5 = QLineEdit()
        self.e5.setEchoMode(QLineEdit.Password)
        self.e5.editingFinished.connect(self.enterPress)

        self.e6 = QLineEdit("Hello Python")
        self.e6.setReadOnly(True)

        self.e7 = QLineEdit("Hello Onur")
        self.e7.cursorPositionChanged.connect((self.cursorPositionChanged))

        self.e8 = QLineEdit("Hello İlkay")
        self.e8.editingFinished.connect((self.editingFinished))

        self.e9 = QLineEdit("Hello Umut")
        self.e9.returnPressed.connect((self.returnPressed))

        self.e10 = QLineEdit("Hello Defne")
        self.e10.selectionChanged.connect((self.selectionChanged))

        self.flo = QFormLayout()
        self.flo.addRow("integer validator", self.e1)
        self.flo.addRow("Double validator", self.e2)
        self.flo.addRow("Input Mask", self.e3)
        self.flo.addRow("Text changed", self.e4)
        self.flo.addRow("Password", self.e5)
        self.flo.addRow("Read Only", self.e6)
        self.flo.addRow("Cursor position change", self.e7)
        self.flo.addRow("Cursor position change", self.e8)
        self.flo.addRow("Returnpressed", self.e9)
        self.flo.addRow("Selectionchanged", self.e10)

        self.mainLayout = QHBoxLayout()
        self.mainLayout.addLayout(self.flo)
        self.setLayout(self.mainLayout)


    def textchanged(self,text):
        print ("contents of text box: " + text)

    def enterPress(self):
        print ("edited")

    def cursorPositionChanged(self):
        print ("Cursor position has been changed")

    def editingFinished(self):
        print ("Editing has been finished")

    def returnPressed(self):
        print ("Enter has been pressed")

    def selectionChanged(self):
        print ("Selection has been changed")

if __name__=='__main__':
    app = QApplication(sys.argv)
    window = Main()
    sys.exit(app.exec_())