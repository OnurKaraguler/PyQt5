import sys, os
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt


class Main(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('combo box demo')
        self.setGeometry(500,150,300,300)
        self.setFixedSize(self.size())          #Ekran ölçüsünü sabitlemek için
        self.UI()
        self.show()

    def UI(self):
        self.window()

    def window(self):
        self.cb = QComboBox()
        self.cb.addItem("C")
        self.cb.addItem("C++")
        self.cb.addItems(["Java", "C#", "Python"])
        self.cb.currentIndexChanged.connect(self.selectionchange)
        print(self.cb.count())
        print(self.cb.itemText(2))
        self.cb.setItemText(2,'Onur')
        # self.cb.activated[str].connect(self.activated)
        self.cb.highlighted[str].connect(self.activated)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.cb)

        self.mainLayout = QHBoxLayout()
        self.mainLayout.addLayout(self.layout)
        self.setLayout(self.mainLayout)

    def selectionchange(self, i):
        pass
        # print("Items in the list are :")
        # for count in range(self.cb.count()):
        #     print(self.cb.itemText(count))
        # print("Current index", i, "selection changed ", self.cb.currentText())
        # self.cb.clear()

    def activated(self,text):
        print(text)



if __name__=='__main__':
    app = QApplication(sys.argv)
    window = Main()
    sys.exit(app.exec_())