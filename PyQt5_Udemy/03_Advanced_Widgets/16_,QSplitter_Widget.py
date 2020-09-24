import sys, os
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
from PIL import Image


class Main(QWidget):
    def __init__(self,parent=None):
        super(Main, self).__init__(parent)
        self.setWindowTitle('QSplitter demo')
        self.setGeometry(500,150,400,400)
        # self.setFixedSize(self.size())
        self.UI()
        self.show()

    def UI(self):
        self.window()

    def window(self):
        self.topleft = QFrame()
        self.topleft.setFrameShape(QFrame.StyledPanel)
        self.bottom = QFrame()
        self.bottom.setFrameShape(QFrame.StyledPanel)
        self.textedit = QTextEdit()

        self.splitter1 = QSplitter(Qt.Horizontal)
        self.splitter1.addWidget(self.topleft)
        self.splitter1.addWidget(self.textedit)
        self.splitter1.setSizes([100, 200])

        self.splitter2 = QSplitter(Qt.Vertical)
        self.splitter2.addWidget(self.splitter1)
        self.splitter2.addWidget(self.bottom)

        QApplication.setStyle(QStyleFactory.create('Cleanlooks'))

        self.hbox = QHBoxLayout(self)
        self.hbox.addWidget(self.splitter2)


        mainLayout = QVBoxLayout()
        mainLayout.addLayout(self.hbox)
        self.setLayout(mainLayout)


if __name__=='__main__':
    app = QApplication(sys.argv)
    window = Main()
    sys.exit(app.exec_())