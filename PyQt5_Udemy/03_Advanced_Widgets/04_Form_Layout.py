import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont

font = QFont('Times', 14)

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Form Layout')
        self.setGeometry(350,150,400,300)
        self.UI()

    def UI(self):
        formLayout = QFormLayout()
        # formLayout.setRowWrapPolicy(QFormLayout.WrapAllRows)        # üst üste yerleştirir
        name_txt = QLabel('Name: ')
        name_input = QLineEdit()
        pass_text = QLabel('Password: ')
        pass_input = QLineEdit()

        hbox = QHBoxLayout()
        hbox.addStretch()
        hbox.addWidget(QPushButton('Enter'))
        hbox.addWidget(QPushButton('Exit'))

        hbox1 = QHBoxLayout()
        hbox1.addWidget(QLineEdit())
        hbox1.addWidget(QLineEdit())

        formLayout.addRow(name_txt,hbox1)
        # formLayout.addRow(name_txt,name_input)
        formLayout.addRow(pass_text,pass_input)
        formLayout.addRow(QLabel('Country: '), QComboBox())
        # formLayout.addRow(QPushButton('Enter'), QPushButton('Exit'))  # problem yaratıyor
        formLayout.addRow(hbox)

        self.setLayout(formLayout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())