#https://www.youtube.com/watch?v=TXZkHy2koyo&list=PL1FgJUcJJ03uO70zDLDF3oaTu6s2QLOPa&index=21
import sys
from PyQt5.QtWidgets import QApplication, QDialog, QVBoxLayout, QPushButton, QProgressBar
from PyQt5 import QtGui
from PyQt5.QtCore import Qt, QThread, pyqtSignal
import time

class MyThread(QThread):
    change_value = pyqtSignal(int)

    def run(self):
        cnt = 0
        while cnt < 100:
            cnt += 1

            time.sleep(0.3)
            self.change_value.emit(cnt)

class Window (QDialog):
    def __init__(self):
        super().__init__()

        self.title = "PyQt5 Progress Bar"
        self.left = 500
        self.top = 200
        self.width = 300
        self.height = 100
        self.iconName = "Onur_Karaguler.png"

        self.setWindowTitle(self.title)
        self.setWindowIcon(QtGui.QIcon(self.iconName))
        self.setGeometry(self.left, self.top, self.width, self.height)


        vbox = QVBoxLayout()

        self.progressbar = QProgressBar()
        self.progressbar.setMaximum(100)
        self.progressbar.setStyleSheet("QProgressBar {border: 2px solid grey; border-radius: 8px; padding: 1px}"
                                       "QProgressBar::chunk {background:green}")

        #self.progressbar.setOrientation(Qt.Vertical)
        self.progressbar.setTextVisible(False)

        vbox.addWidget(self.progressbar)

        self.button = QPushButton("Run Progressbar")
        self.button.clicked.connect(self.startProgressBar)
        self.button.setFont(QtGui.QFont("sanserif",13))
        self.button.setStyleSheet("""QPushButton{background-color: yellow; color : brown}""")
        vbox.addWidget(self.button)

        self.setLayout(vbox)

        self.show()

    def startProgressBar(self):
        self.thread = MyThread()
        self.thread.change_value.connect(self.setProgressVal)
        self.thread.start()

    def setProgressVal(self, val):
        self.progressbar.setValue(val)

App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())