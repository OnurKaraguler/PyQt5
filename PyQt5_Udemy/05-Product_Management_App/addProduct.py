import sys,os
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
import sqlite3
from PIL import Image

con = sqlite3.connect('products.db')
cur = con.cursor()

defaultImg="store.png"      # eğer ürünün resmi yok ise standart resim

class AddProduct(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Add Product")
        self.setWindowIcon(QIcon('icons/icon.ico'))
        self.setGeometry(450,150,350,550)
        self.setFixedSize(self.size())
        self.UI()
        self.show()

    def UI(self):
        self.widgets()
        self.layouts()

    def widgets(self):
        ##################Top Layout Widgets##############
        self.addProductImg = QLabel()
        self.img = QPixmap('icons/addproduct.png')
        self.addProductImg.setPixmap(self.img)
        self.titleText =QLabel('Add Product')
        ##################Bottom Layout Widgets##############
        self.nameEntry = QLineEdit()
        self.nameEntry.setPlaceholderText('Enter name of products')
        self.manufacturerEntry = QLineEdit()
        self.manufacturerEntry.setPlaceholderText('Enter name of manufacturer')
        self.priceEntry = QLineEdit()
        self.priceEntry.setPlaceholderText('Enter price of products')
        self.quotaEntry = QLineEdit()
        self.quotaEntry.setPlaceholderText('Enter quota of products')
        self.uploadBtn = QPushButton('Upload')
        self.uploadBtn.clicked.connect(self.uploadImg)
        self.submitBtn = QPushButton('Submit')
        self.submitBtn.clicked.connect(self.addProduct)

    def layouts(self):
        self.mainLayout = QVBoxLayout()

        self.topLayout = QHBoxLayout()
        self.bottomLayout = QFormLayout()
        self.topFrame = QFrame()
        self.bottomFrame = QFrame()

        self.mainLayout.addWidget(self.topFrame)
        self.mainLayout.addWidget(self.bottomFrame)

        self.bottomFrame.setLayout(self.bottomLayout)

        self.setLayout(self.mainLayout)
        ##################Top Layout Widgets##############
        self.topLayout.addWidget(self.addProductImg)
        self.topLayout.addWidget(self.titleText)
        self.topFrame.setLayout(self.topLayout)
        ##################Form Layout Widgets##############
        self.bottomLayout.addRow(QLabel('Name: '),self.nameEntry)
        self.bottomLayout.addRow(QLabel('Manufacturer: '),self.manufacturerEntry)
        self.bottomLayout.addRow(QLabel('Price: '),self.priceEntry)
        self.bottomLayout.addRow(QLabel('Quota: '), self.quotaEntry)
        self.bottomLayout.addRow(QLabel('Upload: '),self.uploadBtn)
        self.bottomLayout.addRow(QLabel(''),self.submitBtn)

    def uploadImg(self):
        global defaultImg
        size = (256,256)
        self.filename,ok = QFileDialog.getOpenFileName(self,'Upload Image','','Image Files (*.jpeg *.jpg *.png)')
        if ok:
            defaultImg = os.path.basename(self.filename)
            img = Image.open(self.filename)
            img = img.resize(size)
            img.save('img/{0}'.format(defaultImg))

    def addProduct(self):

        global defaultImg
        name = self.nameEntry.text()
        manufacturer = self.manufacturerEntry.text()
        price = self.priceEntry.text()
        quota = self.quotaEntry.text()

        if (name and manufacturer and price and quota != ''):
            try:
                query = "INSERT INTO products (product_name,product_manufacturer,product_price,product_qouta,product_img) VALUES(?,?,?,?,?)"
                cur.execute(query,(name, manufacturer, price, quota, defaultImg))
                con.commit()
                QMessageBox.information(self,'Info','Product has been added')
                # con.close()
                self.nameEntry.setText('')
                self.manufacturerEntry.setText('')
                self.priceEntry.setText('')
                self.quotaEntry.setText('')
            except:
                QMessageBox.information(self, 'Info', 'Product has not been added')
        else:
            QMessageBox.information(self,'Info','Fields can not be empty')
