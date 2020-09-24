from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QKeySequence
from fifteen import Ui_MainWindow
from PyQt5.uic import loadUi

class dersler_15(QMainWindow):


    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.comboBox_birds.addItem("Kırmızı Kuş")
        self.ui.comboBox_birds.addItem("Mavi Kuş",100)
        self.ui.comboBox_birds.addItem(QIcon("icons/4.png"), "Yeşil Kuş")
        self.ui.comboBox_birds.addItem(QIcon("icons/7.png"), "Yeşil Kuş", 500)

        self.ui.comboBox_fruits.addItems(("Seçiniz", "Elma", "Armut", "Kiraz", "Karpuz"))

        self.ui.comboBox_birds.insertItem(0, "Seçiniz")

        #self.ui.comboBox_fruits.clear()
        #self.ui.comboBox_birds.removeItem(0)

        self.ui.comboBox_animals.addItems(["Keçi", "Koç", "İnek"])
        self.ui.comboBox_cars.addItems(["Citroen", "Renault", "Peugeot", "Skoda"])

        self.ui.pushButton_show.clicked.connect(self.show_result)

        self.ui.comboBox_birds.activated["int"].connect(self.birds_activated)
        self.ui.comboBox_fruits.currentIndexChanged["int"].connect(self.fruits_index_changed)
        self.ui.comboBox_animals.currentIndexChanged["QString"].connect(self.animals_index_changed)
        self.ui.comboBox_cars.highlighted["int"].connect(self.highlighted_car)

    def highlighted_car (self, highlighted_index):

        print("current text : ", highlighted_index)

    def animals_index_changed(self,current_text):

        print("current text : ", current_text)

    def fruits_index_changed(self, current_index):

        if (current_index !=0):
            print("current index : ", current_index)
            print("item text : ", self.ui.comboBox_fruits.itemText(current_index))
            print("current text : ", self.ui.comboBox_fruits.currentText())

    def birds_activated(self, activated_index):
            print("activated index : ", activated_index)
            print("item text : ", self.ui.comboBox_fruits.itemText(current_index))
            print("current text : ", self.ui.comboBox_fruits.currentText())

    def show_result(self):
        #self.ui.comboBox_fruits.clear()

        selected_items = self.ui.comboBox_birds.currentText()
        selected_index = self.ui.comboBox_birds.currentIndex()
        selected_data = self.ui.comboBox_birds.currentData()

        print("text : ", selected_items)
        print("text : ", selected_index)
        print("text : ", selected_data)

uygulama = QApplication ([])
pencere = dersler_15()
pencere.show()
uygulama.exec_()