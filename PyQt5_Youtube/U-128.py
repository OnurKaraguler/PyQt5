import sys
from PyQt5 import QtWidgets,QtGui

def window ():
    app = QtWidgets.QApplication (sys.argv)
    okay = QtWidgets.QPushButton("Tamam")
    cancel = QtWidgets.QPushButton("İptal")
    ileri = QtWidgets.QPushButton("İleri")
    geri = QtWidgets.QPushButton("Geri")

    h_box = QtWidgets.QHBoxLayout()
    v_box = QtWidgets.QVBoxLayout()

    h_box.addWidget(okay)
    h_box.addStretch()
    h_box.addWidget(cancel)

    v_box.addStretch()
    v_box.addWidget(ileri)
    v_box.addWidget(geri)

    pencere = QtWidgets.QWidget()
    pencere.setWindowTitle("PyQt5 Ders 4")

    pencere.setGeometry(100,100,500,500)

    pencere.setLayout(v _box)

    pencere.show()
    sys.exit(app.exec())
window()