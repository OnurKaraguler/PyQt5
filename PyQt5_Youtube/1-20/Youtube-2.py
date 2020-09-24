import sys
from PyQt5.QtWidgets import QMainWindow,QApplication, QPushButton
# QPushButton eklendi
from PyQt5.QtCore import QRect

class Window (QMainWindow):
    def __init__(self):
        super ().__init__()

        title = "PyQt5 Push Button"
        top = 200
        left = 500
        width = 300
        height =250

        self.setWindowTitle(title)
        self.setGeometry(left, top, width, height)

        self.UiComponents()   # PushButton için

    def UiComponents(self):
        button = QPushButton ("Click Me",self)
        #button.move (50,50)   # PushButton pozisyonu
        button.setGeometry(QRect(100,100,110,50))   # PushButton posisyon ve ölçüleri

        self.show ()

if __name__ == "__main__":
    app = QApplication (sys.argv)
    window = Window ()
    sys.exit(app.exec())