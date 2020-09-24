import sys, os
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
from PIL import Image


class Main(QWidget):
    def __init__(self,parent=None):
        super(Main, self).__init__(parent)
        self.setWindowTitle('Tab demo')
        self.setGeometry(500,150,400,400)
        self.setFixedSize(self.size())
        self.UI()
        self.show()

    def UI(self):
        self.window()

    def window(self):
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tab3 = QWidget()


        self.tab1UI()
        self.tab2UI()
        self.tab3UI()

        self.tabs = QTabWidget()
        # self.tabs.setTabPosition(QTabWidget.North)
        # self.tabs.setTabPosition(QTabWidget.South)
        self.tabs.setTabPosition(QTabWidget.West)
        # self.tabs.setTabPosition(QTabWidget.East)
        self.tabs.addTab(self.tab1, "Contact Details")
        self.tabs.addTab(self.tab2, "Personal Details")
        self.tabs.addTab(self.tab3, "Education Details")

        self.tabs.currentChanged.connect(self.currentTabChange)

        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.tabs)
        self.setLayout(mainLayout)


    def tab1UI(self):
        layout = QFormLayout()
        layout.addRow("Name", QLineEdit())
        layout.addRow("Address", QLineEdit())
        # self.setTabText(0, "Contact Details")
        self.tab1.setLayout(layout)

    def tab2UI(self):
        layout = QFormLayout()

        sex = QHBoxLayout()
        sex.addWidget(QRadioButton("Male"))
        sex.addWidget(QRadioButton("Female"))
        layout.addRow(QLabel("Sex"), sex)
        layout.addRow("Date of Birth", QLineEdit())
        # self.setTabText(1, "Personal Details")
        self.tab2.setLayout(layout)

    def tab3UI(self):
        layout=QHBoxLayout()
        layout.addWidget(QLabel("subjects"))
        layout.addWidget(QCheckBox("Physics"))
        layout.addWidget(QCheckBox("Maths"))
        # self.setTabText(2,"Education Details")
        self.tab3.setLayout(layout)

    def currentTabChange(self):
        print('currentTabChange')

if __name__=='__main__':
    app = QApplication(sys.argv)
    window = Main()
    sys.exit(app.exec_())