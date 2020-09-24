import sys, os
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
from PIL import Image


class Main(QWidget):
    def __init__(self,parent=None):
        super(Main, self).__init__(parent)
        self.setWindowTitle('File Dialog demo')
        self.setGeometry(500,150,400,400)
        self.setFixedSize(self.size())
        self.UI()
        self.show()

    def UI(self):
        self.window()

    def window(self):
        self.btn = QPushButton("QFileDialog static method demo")
        self.btn.clicked.connect(self.getfile)
        self.btn1 = QPushButton("QFileDialog object")
        self.btn1.clicked.connect(self.getfiles)

        self.le = QLabel("Hello")
        self.le.setAlignment(Qt.AlignCenter)

        self.contents = QTextEdit()

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.btn)
        self.layout.addWidget(self.le)
        self.layout.addWidget(self.btn1)
        self.layout.addWidget(self.contents)

        self.mainLayout = QHBoxLayout()
        self.mainLayout.addLayout(self.layout)
        self.setLayout(self.mainLayout)

    def getfile(self):
        size = (256,256)
        self.filename,ok = QFileDialog.getOpenFileName(self,'Open file','','Image Files (*.jpeg *.jpg *.png)')
        if ok:
            defaultImg = os.path.basename(self.filename)
            img = Image.open(self.filename)
            img = img.resize(size)
            img.save(f'img/{defaultImg}')
            self.le.setPixmap(QPixmap(f'img/{defaultImg}'))


    def getfiles(self):
        self.filename,ok = QFileDialog.getOpenFileName(self,'Open file','','Text Files (*.txt)')
        print(self.filename)
        if ok:
            file = open(self.filename, 'r', encoding='utf-8')
            data = file.read()
            self.contents.setText(data)



if __name__=='__main__':
    app = QApplication(sys.argv)
    window = Main()
    sys.exit(app.exec_())