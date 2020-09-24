import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QMenuBar, QAction
from PyQt5 import QtGui
from PyQt5.QtGui import QIcon

class Window (QMainWindow):
    def __init__(self):
        super().__init__()

        self.title = "PyQt5 Menubar"
        self.left = 500
        self.top = 200
        self.width = 300
        self.height = 200
        self.iconName = "Onur_Karaguler.png"

        self.setWindowTitle(self.title)
        self.setWindowIcon(QtGui.QIcon(self.iconName))
        self.setGeometry(self.left, self.top, self.width, self.height)


        vbox = QVBoxLayout()

        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu("File")
        editMenu = mainMenu.addMenu("Edit")
        viewMenu = mainMenu.addMenu("View")
        helpMenu = mainMenu.addMenu("Help")

        copyAction = QAction(QIcon("copy.png"),'Copy',self)
        copyAction.setShortcut("Ctrl+C")
        fileMenu.addAction(copyAction)

        cutAction = QAction(QIcon("cut.png"),'Cut',self)
        cutAction.setShortcut("Ctrl+X")
        fileMenu.addAction(cutAction)

        pasteAction = QAction(QIcon("paste.png"),'Paste',self)
        pasteAction.setShortcut("Ctrl+V")
        fileMenu.addAction(pasteAction)

        saveAction = QAction(QIcon("save.png"),'Save',self)
        saveAction.setShortcut("Ctrl+S")
        fileMenu.addAction(saveAction)

        exitAction = QAction(QIcon("exit.jpg"),'Exit',self)
        exitAction.setShortcut("Ctrl+E")
        exitAction.triggered.connect(self.exitWindow)
        editMenu.addAction(exitAction)

        toolbar = self.addToolBar("Toolbar")
        toolbar.addAction(copyAction)
        toolbar.addAction(cutAction)
        toolbar.addAction(pasteAction)
        toolbar.addAction(saveAction)
        toolbar.addAction(exitAction)

        vbox.addWidget(mainMenu)


        self.setLayout(vbox)

        self.show()

    def exitWindow(self):
        self.close()


App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())