import sys
from PyQt5 import QtWidgets,QtGui

def window ():
    app = QtWidgets.QApplication (sys.argv)


    pencere = QtWidgets.QWidget()
    pencere.setWindowTitle("PyQt5 Ders 3")
    pencere.setGeometry(100,100,500,500)

    buton = QtWidgets.QPushButton (pencere)
    buton.setText("Burası bir butondur")

    etiket = QtWidgets.QLabel(pencere)
    etiket.setText("Merhaba Dünya")

    buton.move(200,80)
    etiket.move(200,30)


    pencere.show()
    sys.exit(app.exec())
window()