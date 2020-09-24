import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt



class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Table Widget')
        self.setGeometry(350,150,400,400)
        self.UI()

    def UI(self):
        vbox = QVBoxLayout()
        self.table = QTableWidget()
        btn = QPushButton('Get')
        self.table.setRowCount(5)
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderItem(0,QTableWidgetItem('Name'))
        self.table.setHorizontalHeaderItem(1,QTableWidgetItem('Surname'))
        self.table.setHorizontalHeaderItem(2,QTableWidgetItem('Adress'))
        # self.table.horizontalHeader().hide()
        # self.table.verticalHeader().hide()
        self.table.setItem(0,0,QTableWidgetItem('1th Item'))
        self.table.setItem(0,1,QTableWidgetItem('2th Item'))
        self.table.setItem(1,2,QTableWidgetItem('3th Item'))
        self.table.setItem(4,2,QTableWidgetItem('4th Item'))
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)    #hücreleri el ile değiştirmeye kapatıyot

        self.table.doubleClicked.connect(self.doubleClicked)

        btn.clicked.connect(self.getValue)

        vbox.addWidget(self.table)
        vbox.addWidget(btn)

        self.setLayout(vbox)

    def getValue(self):
        for item in self.table.selectedItems():
            print(item.text(), item.row(), item.column())

    def doubleClicked(self):
        for item in self.table.selectedItems():
            print(item.text(), item.row(), item.column())



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())