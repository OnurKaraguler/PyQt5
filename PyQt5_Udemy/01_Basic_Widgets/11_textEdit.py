import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont

font = QFont('Times', 14)

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Using Text Editor')
        self.setGeometry(250,150,500,500)
        self.UI()

    def UI(self):
        self.editor = QTextEdit(self)
        self.editor.move(150,80)
        button = QPushButton('Send', self)
        self.editor.setAcceptRichText(False)        # Default is True(kopyalanan font özelliklerini alır. False almaz
        button.move(330,280)
        button.clicked.connect(self.getValue)

    def getValue(self):
        text = self.editor.toPlainText()        # Text in font una bakmaksızın alır
        print(text)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
