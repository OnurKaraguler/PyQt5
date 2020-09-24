import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QAction, QTextEdit, QFontDialog
from PyQt5 import QtGui
from PyQt5.QtGui import QIcon

class Window (QMainWindow):
    def __init__(self):
        super().__init__()

        self.title = "PyQt5 TextEdit"
        self.left = 500
        self.top = 200
        self.width = 500
        self.height = 400
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

        exitAction = QAction(QIcon("exit.jpg"),'Exit',self)
        exitAction.setShortcut("Ctrl+E")
        exitAction.triggered.connect(self.exitWindow)
        fileMenu.addAction(exitAction)

        copyAction = QAction(QIcon("copy.png"),'Copy',self)
        copyAction.setShortcut("Ctrl+C")
        editMenu.addAction(copyAction)

        cutAction = QAction(QIcon("cut.png"),'Cut',self)
        cutAction.setShortcut("Ctrl+X")
        editMenu.addAction(cutAction)

        pasteAction = QAction(QIcon("paste.png"),'Paste',self)
        pasteAction.setShortcut("Ctrl+V")
        editMenu.addAction(pasteAction)

        saveAction = QAction(QIcon("save.png"),'Save',self)
        saveAction.setShortcut("Ctrl+S")
        editMenu.addAction(saveAction)

        fontAction = QAction(QIcon("font.png"),"Font",self)
        fontAction.setShortcut("Ctrl+F")
        fontAction.triggered.connect(self.fontDialog)
        viewMenu.addAction(fontAction)

        toolbar = self.addToolBar("Toolbar")
        toolbar.addAction(copyAction)
        toolbar.addAction(cutAction)
        toolbar.addAction(pasteAction)
        toolbar.addAction(saveAction)
        toolbar.addAction(exitAction)
        toolbar.addAction(fontAction)

        self.textedit = QTextEdit()
        self.textedit.setFont(QtGui.QFont("sanserif",15))
        self.setCentralWidget(self.textedit)


        vbox.addWidget(mainMenu)


        self.setLayout(vbox)

        self.show()

    def fontDialog(self):
        font, ok = QFontDialog.getFont()

        if ok:
            self.textedit.setFont(font)

    def exitWindow(self):
        self.close()


App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())