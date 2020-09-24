import sys
from PyQt5 import QtWidgets

def window():
    app = QtWidgets.QApplication(sys.argv)

    pencere = QtWidgets.QWidget()
    pencere.setWindowTitle("PyQt5 Ders Oyun_1")

    pencere.show()
    sys.exit(app.exec())

window()

