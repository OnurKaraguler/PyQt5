import sys
from PyQt5.QtWidgets import QDialog,QApplication, QPushButton, QGroupBox, QHBoxLayout, QVBoxLayout, QLabel
from PyQt5.QtWidgets import QRadioButton, QCheckBox, QLineEdit
from PyQt5 import QtGui   # pencerenin logosunu değiştirmek için
from PyQt5 import QtCore
from PyQt5.QtGui import QPixmap

class Window (QDialog):
    def __init__(self):
        super ().__init__()

        self.title = "PyQt5 Push Button"
        self.top = 200
        self.left = 500
        self.width = 500
        self.height =100
        self.iconName = "Onur_Karaguler.png"

        self.initWindow()       # Pencereyi boyutlandırmak için

        self.createLayout()     # Butonların olduğu zemini oluşturdun
        vbox = QVBoxLayout()
        vbox.addWidget(self.groupbox)

        self.label = QLabel (self)   # Checkbutton veya radiobutona basıldığında
        self.label.setFont(QtGui.QFont("Sanserif",15))
        self.label.setStyleSheet('color:blue')
        vbox.addWidget(self.label)

        label1 = QLabel ("PyQt5")   # Yazı ekledin
        vbox.addWidget(label1)

        label2 = QLabel ("This is PyQt5 GUI Application Development.")   # 2.Yazı ekledin
        label2.setFont(QtGui.QFont("Sanserif",15))  # Yazının tipi ve yüksekliği
        label2.setStyleSheet('color:red')   # Yazının rengi
        vbox.addWidget(label2)


        labelImage = QLabel (self)          #*********************
        pixmap = QPixmap ("Python.png")     #Resim eklendi
        labelImage.setPixmap(pixmap)
        vbox.addWidget(labelImage)          #*********************

        self.setLayout(vbox)

        self.show ()

    def initWindow(self):
        self.setWindowTitle(self.title)
        self.setWindowIcon(QtGui.QIcon(self.iconName))
        self.setGeometry(self.left, self.top, self.width, self.height)

    def createLayout (self):
        self.groupbox = QGroupBox ("Click on a button...")
        hboxlayout = QHBoxLayout()

        self.button = QPushButton ("Click Me",self)
        self.button.setMaximumHeight(40)
        self.button.setMaximumWidth(100)
        hboxlayout.addWidget(self.button)

        self.button2 = QPushButton("Onur Karagüler", self)
        self.button2.setIcon(QtGui.QIcon("Onur_Karaguler.png"))      # Butona ikon/resim ekleme
        self.button2.setIconSize(QtCore.QSize(40,40))
        self.button2.setToolTip("<h2>This is click me button<h2>")   # Butonun üzerinde beklediğinde
        self.button2.setMaximumHeight(40)
        self.button2.setMaximumWidth(100)
        hboxlayout.addWidget(self.button2)

        self.button3 = QPushButton("Onur Karagüler", self)
        self.button3.clicked.connect(self.ClickMe)
        self.button3.setMaximumHeight(40)
        self.button3.setMaximumWidth(100)
        hboxlayout.addWidget(self.button3)

        #self.button4 = QPushButton("Ekrana Yazar", self)
        #self.button4.setMaximumHeight(40)
        #self.button4.setMaximumWidth(100)
        #hboxlayout.addWidget(self.button4)

        self.radiobutton = QRadioButton ("Java")
        self.radiobutton.setIcon(QtGui.QIcon("Java.png"))
        self.radiobutton.setIconSize(QtCore.QSize(40, 40))
        self.radiobutton.setFont(QtGui.QFont("Samnserif", 13))
        self.radiobutton.toggled.connect(self.OnButton)
        hboxlayout.addWidget(self.radiobutton)

        self.checkbutton = QCheckBox("C++")
        self.checkbutton.setIcon(QtGui.QIcon("C++.png"))
        self.checkbutton.setIconSize(QtCore.QSize(40, 40))
        self.checkbutton.setFont(QtGui.QFont("Sanserif", 15))
        self.checkbutton.toggled.connect(self.OnButton)
        hboxlayout.addWidget(self.checkbutton)

        self.lineedit = QLineEdit (self)
        self.lineedit.setFont(QtGui.QFont("Sanserif", 15))
        self.lineedit.returnPressed.connect(self.onPressed)   # yazdığın yazıyı basıyor
        hboxlayout.addWidget(self.lineedit)

        self.button4 = QPushButton("Close Me", self)
        self.button4.clicked.connect(self.CloseMe)
        self.button4.setMaximumHeight(40)
        self.button4.setMaximumWidth(100)
        hboxlayout.addWidget(self.button4)

        self.groupbox.setLayout(hboxlayout)

    def OnButton (self):
        radioBtn = self.sender()

        if radioBtn.isChecked():
            self.label.setText("You have selected " + radioBtn.text())

    def ClickMe(self):
        print("Onur Karagüler")

    def CloseMe(self):
        sys.exit()

    def onPressed(self):
        self.label.setText(self.lineedit.text())

if __name__ == "__main__":
    app = QApplication (sys.argv)
    window = Window ()
    sys.exit(app.exec())