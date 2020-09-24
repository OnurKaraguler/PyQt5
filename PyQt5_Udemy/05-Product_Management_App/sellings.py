import sys,os
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
import sqlite3
from PIL import Image
import style

con = sqlite3.connect('products.db')
cur = con.cursor()

defaultImg="store.png"      # eğer ürünün resmi yok ise standart resim

class SellProducts(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sell Products")
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
        self.sellProductImg = QLabel()
        self.img = QPixmap('icons/shop.png')
        self.sellProductImg.setPixmap(self.img)
        self.sellProductImg.setAlignment(Qt.AlignCenter)
        self.titleText =QLabel('Sell Product')
        self.titleText.setAlignment(Qt.AlignCenter)
        ##################Bottom Layout Widgets##############
        self.productCombo = QComboBox()
        self.productCombo.currentIndexChanged.connect(self.changeCombovalue)
        self.memberCombo = QComboBox()
        self.quantityCombo = QComboBox()
        self.submitBtn = QPushButton('Submit')
        self.submitBtn.clicked.connect(self.sellProduct)
#
        query1 =("SELECT * FROM products WHERE product_availability= ?")
        products=cur.execute(query1,('Available',)).fetchall()
        query2 = ("SELECT member_id, member_name FROM members")
        members=cur.execute(query2).fetchall()
        quantity=products[0][4]

        for product in products:
            self.productCombo.addItem(product[1],product[0])        # product[0] hidden value

        for member in members:
            self.memberCombo.addItem(member[1],member[0])

        for i in range(1,quantity+1):               # sistemde ne kadar ürün var
            self.quantityCombo.addItem(str(i))     # range den gelen sayıyı stringe çevirme

    def layouts(self):
        self.mainLayout = QVBoxLayout()

        self.topLayout = QHBoxLayout()
        self.bottomLayout = QFormLayout()
        self.topFrame = QFrame()
        self.topFrame.setStyleSheet(style.sellProductTopFrame())     # style
        self.bottomFrame = QFrame()
        self.bottomFrame.setStyleSheet(style.sellProductBottomFrame())     # style

        self.mainLayout.addWidget(self.topFrame)
        self.mainLayout.addWidget(self.bottomFrame)

        self.bottomFrame.setLayout(self.bottomLayout)

        self.setLayout(self.mainLayout)
        ##################Top Layout Widgets##############
        self.topLayout.addWidget(self.titleText)
        self.topLayout.addWidget(self.sellProductImg)
        self.topFrame.setLayout(self.topLayout)
        ##################Form Layout Widgets##############
        self.bottomLayout.addRow(QLabel('Product: '),self.productCombo)
        self.bottomLayout.addRow(QLabel('Member: '),self.memberCombo)
        self.bottomLayout.addRow(QLabel('Quantity: '),self.quantityCombo)
        self.bottomLayout.addRow(QLabel(''),self.submitBtn)

    def changeCombovalue(self):
        self.quantityCombo.clear()                          # ilk açıldığında silmiyor. sonra siliyor
        product_id = self.productCombo.currentData()        # currentData is a hidden value
        query = ("SELECT product_qouta FROM products WHERE product_id=?")
        qouta = cur.execute(query, (product_id,)).fetchone()
        for i in range(1,qouta[0]+1):
            self.quantityCombo.addItem(str(i))

    def sellProduct(self):
        global productName, productId, memberName, memberId, quantity
        productName = self.productCombo.currentText()
        productId=self.productCombo.currentData()       # hidden value
        memberName = self.memberCombo.currentText()
        memberId = self.memberCombo.currentData()
        quantity = int(self.quantityCombo.currentText())
        self.confirm = ConfirmWindow()
        self.close()

##############################################################################
##############################################################################
class ConfirmWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sell Product")
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
        self.sellProductImg = QLabel()
        self.img = QPixmap('icons/shop.png')
        self.sellProductImg.setPixmap(self.img)
        self.sellProductImg.setAlignment(Qt.AlignCenter)      # Resimi merkezlemek
        self.titleText =QLabel('Sell Product')
        ##################Bottom Layout Widgets##############
        global productName, productId, memberName, memberId, quantity       # ÖNEMLİ!!!
        priceQuery = ("SELECT product_price FROM products WHERE product_id=?")
        price = cur.execute(priceQuery,(productId,)).fetchone()
        self.amount = quantity * price[0]

        self.productName = QLabel()
        self.productName.setText(productName)
        self.memberName = QLabel()
        self.memberName.setText(memberName)
        self.amountLabel = QLabel()
        self.amountLabel.setText(str(price[0]) + 'x' + str(quantity) + '=' + str(self.amount))
        self.confirmBtn = QPushButton('Confirm')
        self.confirmBtn.clicked.connect(self.funcConfirm)

    def layouts(self):
        self.mainLayout = QVBoxLayout()

        self.topLayout = QVBoxLayout()
        self.bottomLayout = QFormLayout()
        self.topFrame = QFrame()
        self.topFrame.setStyleSheet(style.confirmProductTopFrame())     # style
        self.bottomFrame = QFrame()
        self.bottomFrame.setStyleSheet(style.confirmProductBottomFrame())     # style

        self.mainLayout.addWidget(self.topFrame)
        self.mainLayout.addWidget(self.bottomFrame)

        self.bottomFrame.setLayout(self.bottomLayout)

        self.setLayout(self.mainLayout)
        ##################Top Layout Widgets##############
        self.topLayout.addWidget(self.titleText)
        self.topLayout.addWidget(self.sellProductImg)
        self.topFrame.setLayout(self.topLayout)
        ##################Form Layout Widgets##############
        self.bottomLayout.addRow(QLabel('Product: '),self.productName)
        self.bottomLayout.addRow(QLabel('Member: '),self.memberName)
        self.bottomLayout.addRow(QLabel('Amount: '),self.amountLabel)
        self.bottomLayout.addRow(QLabel(''),self.confirmBtn)

    def funcConfirm(self):
        global productName, productId, memberName, memberId, quantity
        try:
            sellQuery = ("INSERT INTO 'sellings' (selling_product_id, selling_member_id, selling_quantity, selling_amount) VALUES (?,?,?,?)")
            cur.execute(sellQuery,(productId, memberId, quantity, self.amount))
            qoutaQuery = ("SELECT product_qouta FROM products WHERE product_id=?")
            qouta = cur.execute(qoutaQuery, (productId,)).fetchone()
            con.commit()


            if (quantity == qouta[0]):
                updateQuotaQuery = ("UPDATE products set product_qouta=?, product_availability=? WHERE product_id=?")
                cur.execute(updateQuotaQuery,(0,'Unavailable',productId))
                con.commit()
                ################## buraya kadar çalıştı####################
            else:
                newQouta = (qouta[0] - quantity)
                updateQuotaQuery = ("UPDATE products set product_qouta=? WHERE product_id=?")
                cur.execute(updateQuotaQuery,(newQouta,productId))
                con.commit()

            QMessageBox.information(self, 'Info', 'Success')
        except:
            QMessageBox.information(self, 'Info', 'Something went wrong!!!')
#