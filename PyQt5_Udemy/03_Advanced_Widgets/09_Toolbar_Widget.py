import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt

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
        ##################ToolBar####################
        tb = self.addToolBar('My Toolbar')
        tb.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        newTb = QAction(QIcon('images/2.png'), 'New', self)
        tb.addAction(newTb)
        openTb = QAction(QIcon('images/3.png'), 'Open', self)
        tb.addAction(openTb)
        saveTb = QAction(QIcon('images/4.png'), 'Save', self)
        tb.addAction(saveTb)
        exitTb = QAction(QIcon('images/5.png'), 'Exit', self)
        exitTb.triggered.connect(self.exitFunc)
        tb.actionTriggered.connect(self.btnFunc)
        tb.addAction(exitTb)
        self.combo = QComboBox()
        self.combo.addItems(['Spiderman', 'Superman', 'Batman'])
        tb.addWidget(self.combo)


    def exitFunc(self):
        mbox = QMessageBox.information(self,'Warning', 'Are you sure to exit?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if mbox == QMessageBox.Yes:
            sys.exit()

    def btnFunc(self,btn):
        if btn.text() == 'New':
            print('You clicked new button')
        elif btn.text() == 'Open':
            print('You clicked open button')
        else:
            print('You clicked save button')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())