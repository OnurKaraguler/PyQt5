import sys, os
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
from PIL import Image


class Main(QMainWindow):
    count = 0
    def __init__(self,parent=None):
        super(Main, self).__init__(parent)
        self.setWindowTitle('Draw demo')
        self.setGeometry(500,150,400,400)
        # self.setFixedSize(self.size())
        self.UI()
        self.show()

    def paintEvent(self, event):
        qp = QPainter()

        qp.begin(self)
        qp.setPen(QColor(Qt.red))
        qp.setFont(QFont('Arial', 20))
        qp.drawText(10, 50, "hello Python")
        qp.setPen(QColor(Qt.blue))
        qp.drawLine(10, 100, 100, 100)
        qp.drawRect(10, 150, 150, 100)
        qp.setPen(QColor(Qt.yellow))
        qp.drawEllipse(100, 50, 100, 50)
        qp.drawPixmap(220, 10, QPixmap("img/1.png"))
        qp.fillRect(200, 175, 150, 100, QBrush(Qt.SolidPattern))
        qp.end()

    def UI(self):
        self.window()

    def window(self):

        self.mainLayout = QVBoxLayout()
        self.setLayout(self.mainLayout)



if __name__=='__main__':
    app = QApplication(sys.argv)
    window = Main()
    sys.exit(app.exec_())