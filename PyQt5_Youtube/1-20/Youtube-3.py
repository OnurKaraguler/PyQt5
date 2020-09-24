import sys
from PyQt5.QtWidgets import QMainWindow,QApplication, QPushButton
from PyQt5 import QtGui
from PyQt5.QtCore import QRect
from PyQt5 import QtCore # Butonu boyutlandırmak için

class Window (QMainWindow):
    def __init__(self):
        super ().__init__()

        title = "PyQt5 Push Button"
        top = 200
        left = 500
        width = 300
        height =250
        iconName = "Onur_Karaguler.png"

        self.setWindowTitle(title)
        self.setWindowIcon(QtGui.QIcon(iconName))
        self.setGeometry(left, top, width, height)

        self.UiComponents()

    def UiComponents(self):
        button = QPushButton ("Click Me",self)
        button.setGeometry(QRect(100,100,110,50))
        button.setIcon(QtGui.QIcon("Onur_Karaguler.png"))   # Butona resim ekleme
        button.setIconSize(QtCore.QSize(40,40))   # Butondaki resmi boyutlandırma
        button.setToolTip("<h2>This Is Click Me Button <h2>")
        # Butonun üzerinde beklediğinde açıklama yazısı gelmektedir. <h2> yazının kalınlığı

        self.show ()

if __name__ == "__main__":
    app = QApplication (sys.argv)
    window = Window ()
    sys.exit(app.exec())