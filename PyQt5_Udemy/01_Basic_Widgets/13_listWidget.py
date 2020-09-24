import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont

font = QFont('Times', 14)

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Using ListWidget')
        self.setGeometry(250,150,500,500)
        self.UI()

    def UI(self):
        self.addRecord = QLineEdit(self)
        self.addRecord.move(100,50)
        self.listWidget = QListWidget(self)
        self.listWidget.move(100,80)
        # self.listWidget.setSelectionMode(QListWidget.MultiSelection)       # listeden çoklu seçim için (ctrl)
        self.listWidget.setSelectionMode(QListWidget.ExtendedSelection)      # listeden çoklu seçim( ctrl veya shift)
        ###########################################
        list1 = ['Batman', 'Superman', 'Spiderman']
        self.listWidget.addItems(list1)
        self.listWidget.addItem('Heman')

        # for number in range(5,11):
        #     self.listWidget.addItem(str(number))
        ###########################################
        btnAdd = QPushButton('Add',self)
        btnAdd.move(360, 80)
        btnAdd.clicked.connect(self.funcAdd)
        btnDelete = QPushButton('Delete',self)
        btnDelete.move(360, 110)
        btnDelete.clicked.connect(self.funcDelete)
        btnGet = QPushButton('Get',self)
        btnGet.move(360, 140)
        btnGet.clicked.connect(self.funcGet)
        btnDeleteAll = QPushButton('Delete All',self)
        btnDeleteAll.move(360, 170)
        btnDeleteAll.clicked.connect(self.funcDeleteAll)

    def funcAdd(self):
        val = self.addRecord.text()
        self.listWidget.addItem(val)
        self.addRecord.setText('')

    # def funcDelete(self):
    #     id = self.listWidget.currentRow()       # listede seçili olan id no
    #     self.listWidget.takeItem(id)            # seçili olanın silinmesi

    def funcDelete(self):
        id = self.listWidget.selectedItems()
        for j in id:
            deleted_items = self.listWidget.row(j)
            self.listWidget.takeItem(deleted_items)    # çoklu seçimi silme

    def funcGet(self):
        val = self.listWidget.currentItem().text()
        print(val)

    def funcDeleteAll(self):
        self.listWidget.clear()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
