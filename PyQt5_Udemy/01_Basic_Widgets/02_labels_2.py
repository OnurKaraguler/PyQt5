import sys, os
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt


class Main(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('QLabel Demo')
        self.setGeometry(100,100,300,300)
        self.setFixedSize(self.size())          #Ekran ölçüsünü sabitlemek için
        self.UI()
        self.show()

    def UI(self):
        self.window()

    def window(self):
        self.l1=QLabel()
        self.l1.setText("Hello World")
        self.l1.setAlignment(Qt.AlignCenter)
        self.l1.setOpenExternalLinks(True)
        self.l1.setTextInteractionFlags(Qt.TextSelectableByMouse)
        # self.l1.selectedText()        # anlamadım

        self.l2=QLabel()
        self.l2.setText("<a href='#'>welcome to Python GUI Programming</a>")
        self.l2.linkHovered.connect(self.hovered)

        self.l3=QLabel()
        self.l3.setAlignment(Qt.AlignCenter)
        self.l3.setPixmap(QPixmap("images/1.png"))

        self.l4=QLabel()
        self.l4.setText("<A href='www.TutorialsPoint.com'>TutorialsPoint</a>")
        self.l4.setAlignment(Qt.AlignRight)
        self.l4.linkActivated.connect(self.clicked)

        self.mainLayout = QHBoxLayout()
        self.vbox=QVBoxLayout()
        self.vbox.addWidget(self.l1)
        self.vbox.addStretch()
        self.vbox.addWidget(self.l2)
        self.vbox.addStretch()
        self.vbox.addWidget(self.l3)
        self.vbox.addStretch()
        self.vbox.addWidget(self.l4)

        self.mainLayout.addLayout(self.vbox)
        self.setLayout(self.mainLayout)


    def hovered(self):
        print("hovering")
        self.l3.setPixmap(QPixmap("images/2.png"))

    def clicked(self):
        print("clicked")
        self.l3.setPixmap(QPixmap("images/1.png"))

    def selected(self):
        print("clicked")

if __name__=='__main__':
    app = QApplication(sys.argv)
    window = Main()
    sys.exit(app.exec_())