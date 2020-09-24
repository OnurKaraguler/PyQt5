import sys, os
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
from PIL import Image


class Main(QMainWindow):
    count = 0
    def __init__(self,parent=None):
        super(Main, self).__init__(parent)
        self.setWindowTitle('Dock demo')
        self.setGeometry(500,150,400,400)
        # self.setFixedSize(self.size())
        self.UI()
        self.show()

    def UI(self):
        self.window()

    def window(self):

        bar = self.menuBar()
        file = bar.addMenu("File")
        file.addAction("New")
        file.addAction("save")
        file.addAction("quit")
        self.items = QDockWidget("Dockable", self)
        self.listWidget = QListWidget()
        self.listWidget.addItem("item1")
        self.listWidget.addItem("item2")
        self.listWidget.addItem("item3")
        self.listWidget2 = QListWidget()
        self.listWidget2.addItem("item3")
        self.listWidget2.addItem("item4")
        self.listWidget2.addItem("item5")
        self.items.setWidget(self.listWidget2)
        self.items.setFloating(False)
        self.setCentralWidget(QTextEdit())
        self.addDockWidget(Qt.RightDockWidgetArea, self.items)

        layout = QHBoxLayout()
        self.mainLayout = QVBoxLayout()
        self.mainLayout.addLayout(layout)
        self.setLayout(self.mainLayout)

if __name__=='__main__':
    app = QApplication(sys.argv)
    window = Main()
    sys.exit(app.exec_())