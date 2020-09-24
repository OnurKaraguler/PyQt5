import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Menu Widget')
        self.setGeometry(350,120,600,600)
        self.UI()

    def UI(self):
        ###################Main Menu##################
        menubar = self.menuBar()
        file = menubar.addMenu('File')
        edit = menubar.addMenu('Edit')
        code = menubar.addMenu('Code')
        help_ = menubar.addMenu('Help')
        ##################Sub Menu Items####################
        new = QAction('New Project', self)
        new.setShortcut('Ctrl+o')
        file.addAction(new)
        open = QAction('Open', self)
        file.addAction(open)
        exit = QAction('Exit', self)
        exit.setIcon(QIcon('images/1.png'))
        exit.triggered.connect(self.exitFunc)
        file.addAction(exit)


    def exitFunc(self):
        mbox = QMessageBox.information(self,'Warning', 'Are you sure to exit?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if mbox == QMessageBox.Yes:
            sys.exit()
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())