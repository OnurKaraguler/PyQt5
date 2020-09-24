import sys, os
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
from PIL import Image


class Main(QMainWindow):
    count = 0
    def __init__(self,parent=None):
        super(Main, self).__init__(parent)
        self.setWindowTitle('QStatusBar Example')
        self.setGeometry(500,150,400,400)
        # self.setFixedSize(self.size())
        self.UI()
        self.show()

    def UI(self):
        self.window()

    def window(self):
        self.bar = self.menuBar()
        file = self.bar.addMenu("File")
        file.addAction("show")
        file.addAction("add")
        file.addAction("remove")
        file.triggered[QAction].connect(self.processtrigger)
        self.setCentralWidget(QTextEdit())
        self.statusBar = QStatusBar()
        self.b = QPushButton("click here")
        self.setStatusBar(self.statusBar)

        # layout = QVBoxLayout()
        # layout.addWidget(self.bar)
        # self.mainLayout = QVBoxLayout()
        # self.mainLayout.addLayout(layout)
        # self.setLayout(self.mainLayout)

    def processtrigger(self,q):
        if (q.text()=="show"):
            self.statusBar.showMessage(q.text()+" is clicked",2000)
        if q.text()=="add":
            self.statusBar.addWidget(self.b)
        if q.text()=="remove":
            self.statusBar.removeWidget(self.b)
            self.statusBar.show()

if __name__=='__main__':
    app = QApplication(sys.argv)
    window = Main()
    sys.exit(app.exec_())