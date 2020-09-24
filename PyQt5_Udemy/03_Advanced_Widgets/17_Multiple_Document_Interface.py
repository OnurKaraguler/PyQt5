import sys, os
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
from PIL import Image


class Main(QMainWindow):
    count = 0
    def __init__(self,parent=None):
        super(Main, self).__init__(parent)
        self.setWindowTitle('MDI demo')
        self.setGeometry(500,150,400,400)
        # self.setFixedSize(self.size())
        self.UI()
        self.show()

    def UI(self):
        self.window()

    def window(self):
        self.mdi = QMdiArea()
        self.setCentralWidget(self.mdi)
        self.bar = self.menuBar()
        self.file = self.bar.addMenu("File")
        self.file.addAction("New")
        self.file.addAction("cascade")
        self.file.addAction("Tiled")
        self.file.triggered[QAction].connect(self.windowaction)

        mainLayout = QVBoxLayout()
        # self.mdi.setLayout(mainLayout)
        self.setLayout(mainLayout)

    def windowaction(self, q):
        print("triggered")
        if q.text() == "New":
            # MainWindow.count = MainWindow.count + 1
            sub = QMdiSubWindow()
            sub.setWidget(QTextEdit())
            # sub.setWindowTitle("subwindow" + str(MainWindow.count))
            sub.setWindowTitle("subwindow")
            self.mdi.addSubWindow(sub)
            sub.show()
        if q.text() == "cascade":
            self.mdi.cascadeSubWindows()
        if q.text() == "Tiled":
            self.mdi.tileSubWindows()

if __name__=='__main__':
    app = QApplication(sys.argv)
    window = Main()
    sys.exit(app.exec_())