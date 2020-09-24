import sys
from PyQt5 import QtWidgets,QtGui

def window():
    app = QtWidgets.QApplication(sys.argv)

    pencere = QtWidgets.QWidget()
    pencere.setWindowTitle("PyQt5 Ders 2")

    etiket1 = QtWidgets.QLabel(pencere)
    etiket2 = QtWidgets.QLabel (pencere)
    etiket2.setPixmap(QtGui.QPixmap("Onur_Karaguler.png"))

    etiket1.setText("Burası bir yazıdır")
    etiket1.move(200,30)
    etiket2.move(200,70)

    pencere.setGeometry(100,100,500,500)
    pencere.show()
    sys.exit(app.exec())

window()
