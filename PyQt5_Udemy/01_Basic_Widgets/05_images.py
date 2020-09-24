import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Using Images')
        self.setGeometry(500,200,500,500)
        self.UI()

    def UI(self):
        self.image = QLabel(self)
        self.image.setPixmap(QPixmap('images/1.png'))
        self.image.move(150,50)
        removeButton = QPushButton('Remove', self)
        removeButton.move(150,220)
        removeButton.clicked.connect(self.removeImg)
        showButton = QPushButton('Show', self)
        showButton.move(260, 220)
        showButton.clicked.connect(self.showImage)

    def removeImg(self):
        self.image.close()

    def showImage(self):
        self.image.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
