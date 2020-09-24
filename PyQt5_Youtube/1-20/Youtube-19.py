#https://www.youtube.com/watch?v=TXZkHy2koyo&list=PL1FgJUcJJ03uO70zDLDF3oaTu6s2QLOPa&index=19
import sys
from PyQt5.QtWidgets import QApplication,QPushButton, QWidget,QFormLayout, QLabel,QVBoxLayout, QGroupBox, QScrollArea
from PyQt5 import QtGui

class Window (QWidget):
    def __init__(self,val):
        super().__init__()

        self.title = "PyQt5 QScroll Area"
        self.left = 500
        self.top = 200
        self.width = 300
        self.height = 250
        self.iconName = "Onur_Karaguler.png"

        self.setWindowTitle(self.title)
        self.setWindowIcon(QtGui.QIcon(self.iconName))
        self.setGeometry(self.left, self.top, self.width, self.height)

        formLayout = QFormLayout ()
        groupbox = QGroupBox ("This is Groupbox")

        labelList = []
        buttonList = []

        for i in range (val):
            labelList.append(QLabel("Label"))
            buttonList.append(QPushButton("Click Me"))
            formLayout.addRow(labelList[i], buttonList[i])

        groupbox.setLayout(formLayout)
        scroll = QScrollArea()
        scroll.setWidget(groupbox)
        scroll.setWidgetResizable(True)
        scroll.setFixedHeight(400)

        layout = QVBoxLayout()
        layout.addWidget(scroll)

        self.setLayout(layout)

        self.show()

    def changedValue(self):
        size = self.slider.value()
        self.label.setText(str(size))

App = QApplication(sys.argv)
window = Window(20)
sys.exit(App.exec())