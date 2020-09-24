import sys, os
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
from PIL import Image


class Main(QWidget):
    def __init__(self,parent=None):
        super(Main, self).__init__(parent)
        self.setWindowTitle('StackedWidget demo')
        self.setGeometry(500,150,400,400)
        self.setFixedSize(self.size())
        self.UI()
        self.show()

    def UI(self):
        self.window()

    def window(self):
        self.leftlist = QListWidget()
        self.leftlist.insertItem(0, 'Contact')
        self.leftlist.insertItem(1, 'Personal')
        self.leftlist.insertItem(2, 'Educational')

        self.stack1 = QWidget()
        self.stack2 = QWidget()
        self.stack3 = QWidget()

        self.stack1UI()
        self.stack2UI()
        self.stack3UI()

        self.Stack = QStackedWidget(self)
        self.Stack.addWidget(self.stack1)
        self.Stack.addWidget(self.stack2)
        self.Stack.addWidget(self.stack3)

        self.hbox = QHBoxLayout(self)
        self.hbox.addWidget(self.leftlist)
        self.hbox.addWidget(self.Stack)
        self.leftlist.currentRowChanged.connect(self.display)


        mainLayout = QVBoxLayout()
        mainLayout.addLayout(self.hbox)
        self.setLayout(mainLayout)



    def stack1UI(self):
        layout = QFormLayout()

        layout.addRow("Name", QLineEdit())
        layout.addRow("Address", QLineEdit())
        # self.setTabText(0,"Contact Details")
        self.stack1.setLayout(layout)

    def stack2UI(self):
        layout = QFormLayout()

        sex = QHBoxLayout()
        sex.addWidget(QRadioButton("Male"))
        sex.addWidget(QRadioButton("Female"))
        layout.addRow(QLabel("Sex"), sex)
        layout.addRow("Date of Birth", QLineEdit())
        self.stack2.setLayout(layout)

    def stack3UI(self):
        layout = QHBoxLayout()

        layout.addWidget(QLabel("subjects"))
        layout.addWidget(QCheckBox("Physics"))
        layout.addWidget(QCheckBox("Maths"))
        self.stack3.setLayout(layout)

    def display(self, i):
        self.Stack.setCurrentIndex(i)

if __name__=='__main__':
    app = QApplication(sys.argv)
    window = Main()
    sys.exit(app.exec_())