import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('File Dialogs')
        self.setGeometry(350,120,400,400)
        self.UI()

    def UI(self):
        vbox = QVBoxLayout()
        hbox = QHBoxLayout()
        self.editor = QTextEdit()
        fileButton = QPushButton('Open File')
        fileButton.clicked.connect(self.openFile)

        vbox.addWidget(self.editor)
        vbox.addLayout(hbox)
        hbox.addStretch()
        hbox.addWidget(fileButton)
        hbox.addStretch()
        self.setLayout(vbox)


        self.setLayout(vbox)

    def openFile(self):
        url = QFileDialog.getOpenFileName(self,'Open a file','','All Files(*);;*txt')
        print(url)
        fileURL = url[0]
        print(fileURL)
        file = open(fileURL,'r')
        content = file.read()
        self.editor.setText(content)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())