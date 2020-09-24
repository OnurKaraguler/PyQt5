import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QTimer

count = 0
class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Grid Layout')
        self.setGeometry(350,120,600,600)

        self.UI()

    def UI(self):
        vbox = QVBoxLayout()
        hbox = QHBoxLayout()
        self.progressBar = QProgressBar()
        btnStart = QPushButton('Start')
        btnStart.clicked.connect(self.timerStart)
        btnStop = QPushButton('Stop')
        btnStop.clicked.connect(self.timerStop)
        self.timer = QTimer()
        self.timer.setInterval(50)
        self.timer.timeout.connect(self.runProgressBar)

        vbox.addWidget(self.progressBar)
        vbox.addLayout(hbox)
        hbox.addWidget(btnStart)
        hbox.addWidget(btnStop)
        self.setLayout(vbox)

    def runProgressBar(self):
        global count
        count += 1
        # print(count)
        self.progressBar.setValue(count)
        if count == 100:
            self.timer.stop()

    def timerStart(self):
        self.timer.start()

    def timerStop(self):
        self.timer.stop()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())