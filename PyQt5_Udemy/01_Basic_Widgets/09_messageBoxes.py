import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont

font = QFont('Times', 12)

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Using MessageBoxes')
        self.setGeometry(250,150,500,500)
        self.UI()

    def UI(self):
        button = QPushButton('Click ME!', self)
        button.setFont(font)
        button.move(200,150)
        button.clicked.connect(self.messageBox)

# 1
    # def messageBox(self):
    #     mbox = QMessageBox.question(self, 'Warning!!', 'Are you sure to exit',
    #                                 QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel, QMessageBox.No)
    #     if mbox == QMessageBox.Yes:
    #         sys.exit()
    #     elif mbox == QMessageBox.No:
    #         print('You clicked No Button')

# 2
    def messageBox(self):
        mbox = QMessageBox.information(self, 'Information!!', 'You Logged Out')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
