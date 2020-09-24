import sys,os
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap
import sqlite3
from PIL import Image
from PyQt5.QtCore import *

con = sqlite3.connect('oks.db')
cur = con.cursor()
person_id=None

class Main(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('OKS')
        self.setGeometry(430,120,600,450)
        self.UI()
        self.show()

    def UI(self):
        self.mainDesign()
        self.layouts()
        self.getStudents()
        self.displayFirstRecord()

    def mainDesign(self):
        self.setStyleSheet('font-size:12pt;font-family:Arial Bold;')
        self.studentList = QListWidget()
        self.studentList.itemClicked.connect(self.singleClick)      # listeden bir item tıklandığında
        self.btnNew = QPushButton('New')
        self.btnNew.clicked.connect(self.addStudent)
        self.btnUpdate = QPushButton('Update')
        self.btnUpdate.clicked.connect(self.updateStudent)
        self.btnDelete = QPushButton('Delete')
        self.btnDelete.clicked.connect(self.deleteStudent)
        self.img = QLabel()
        self.img.setPixmap(QPixmap('1.png'))
        self.name = QLabel()
        self.surname = QLabel()
        self.phone = QLabel()
        self.email = QLabel()
        self.email.setFixedWidth(220)
        self.address = QLabel()
        self.address.setWordWrap(True)          # Yazı alana kendisini sığdırıyor
        self.address.setFixedSize(150,100)
        self.address.setAlignment(Qt.AlignTop|Qt.AlignLeft)
        self.not1 = QLabel()
        self.not2 = QLabel()
        self.not3 = QLabel()

    def layouts(self):
        ###################Creating Main Layouts###############
        self.mainLayout = QHBoxLayout()
        self.leftLayout = QFormLayout()
        self.rightLayout = QVBoxLayout()
        self.rightTopLayout = QVBoxLayout()
        self.rightBottomLayout = QHBoxLayout()
        ###########Adding child layouts to main layout###########
        self.leftLayout.setVerticalSpacing(15)
        self.leftLayout.addRow('', self.img)
        self.leftLayout.addRow('Name: ', self.name)
        self.leftLayout.addRow('Surname : ', self.surname)
        self.leftLayout.addRow('Score-1: ', self.not1)
        self.leftLayout.addRow('Score-2: ', self.not2)
        self.leftLayout.addRow('Score-3: ', self.not3)
        self.leftLayout.addRow('Phone: ', self.phone)
        self.leftLayout.addRow('Email: ', self.email)
        self.leftLayout.addRow('Address: ', self.address)
        self.rightLayout.addLayout(self.rightTopLayout)
        self.rightLayout.addLayout(self.rightBottomLayout)
        self.mainLayout.addLayout(self.leftLayout,40)
        self.mainLayout.addLayout(self.rightLayout,60)
        ############Adding wigdets to layouts#############
        self.rightTopLayout.addWidget(self.studentList)
        self.rightBottomLayout.addWidget(self.btnNew)
        self.rightBottomLayout.addWidget(self.btnUpdate)
        self.rightBottomLayout.addWidget(self.btnDelete)
        ###########setting main window layout#############
        self.setLayout(self.mainLayout)

    def addStudent(self):
        self.newstudent = AddStudent()
        self.close()

    def updateStudent(self):
        global person_id
        if self.studentList.selectedItems():
            person = self.studentList.currentItem().text()
            person_id = person.split('-')[0]
            self.updateWindow = UpdateStudent()
            self.close()
        else:
            QMessageBox.information(self,'Warning!!!','Please select a person to update')

    def getStudents(self):
        query = "SELECT id,name,surname FROM oks"
        students = cur.execute(query).fetchall()
        for student in students:
            self.studentList.addItem(str(student[0])+'-'+student[1]+' '+student[2] )

    def displayFirstRecord(self):
        query = "SELECT * FROM oks ORDER BY ROWID ASC LIMIT 1"
        student = cur.execute(query).fetchone()
        self.name.setText(student[1])
        self.surname.setText(student[2])
        self.not1.setText(str(student[3]))
        self.not2.setText(str(student[4]))
        self.not3.setText(str(student[5]))
        self.phone.setText(student[6])
        self.email.setText(student[7])
        self.address.setText(student[8])
        self.img.setText(self.img.setPixmap(QPixmap('images/'+student[9])))

    def singleClick(self):
        student = self.studentList.currentItem().text()
        id = student.split('-')[0]
        query = ("SELECT * FROM oks WHERE id=?")
        person = cur.execute(query,(id,)).fetchone()
        self.name.setText(person[1])
        self.surname.setText(person[2])
        self.not1.setText(str(person[3]))
        self.not2.setText(str(person[4]))
        self.not3.setText(str(person[5]))
        self.phone.setText(person[6])
        self.email.setText(person[7])
        self.address.setText(person[8])
        self.img.setText(self.img.setPixmap(QPixmap('images/'+person[9])))

    def deleteStudent(self):
        if self.studentList.selectedItems():
            person = self.studentList.currentItem().text()
            id = person.split('-')[0]
            mbox = QMessageBox.question(self,'Warning','Are you sure to delete this student',QMessageBox.Yes|QMessageBox.No,QMessageBox.No)
            if mbox == QMessageBox.Yes:
                try:
                    query = "DELETE FROM oks WHERE id=?"
                    cur.execute(query,(id,))
                    con.commit()
                    QMessageBox.information(self,'Info!!!','Student has been deleted')
                    self.close()            # Pencereyi güncellemek için
                    self.main = Main()
                except:
                    QMessageBox.information(self,'Warning!!!','Student has not been deleted')

class AddStudent(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Add Student')
        self.setGeometry(600,130,350,500)
        self.show()
        self.UI()

        self.uploadedImg = '1.png'
    def UI(self):
        self.mainDesign()
        self.layouts()

    def closeEvent(self, event):            ##### ekranı kapattığında ana ekranın geri gelmesi
        self.main = Main()

    def mainDesign(self):
        ################Top Layout widgets#######################
        self.setStyleSheet('background-color:white;font-size:12pt;font-family:Times;')
        self.title = QLabel('Add Person')
        self.title.setStyleSheet('color:red;font-size:24pt;font-family:Times;')
        self.img = QLabel()
        self.img.setPixmap(QPixmap('icons/1.png'))
        self.not1 = QLineEdit()
        self.not1.setPlaceholderText('1st Note')
        self.not2 = QLineEdit()
        self.not2.setPlaceholderText('2nd Note')
        self.not3 = QLineEdit()
        self.not3.setPlaceholderText('3rd Note')
        ################Bottom Layout Widgets####################
        self.btnBrowse = QPushButton('Browse')
        self.btnBrowse.setStyleSheet('background-color: orange; font-size: 10;')
        self.btnBrowse.clicked.connect(self.uploadImage)
        self.btnAdd = QPushButton('Add')
        self.btnAdd.clicked.connect(self.addStudent)
        self.btnAdd.setStyleSheet('background-color: red; font-size: 10;')
        self.name = QLineEdit()
        self.name.setPlaceholderText('Enter Student Name')
        self.surname = QLineEdit()
        self.surname.setPlaceholderText('Enter Student surname')
        self.phone = QLineEdit()
        self.phone.setPlaceholderText('Enter Student Phone Number')
        self.email = QLineEdit()
        self.email.setPlaceholderText('Enter Student Email')
        self.address = QTextEdit()
        self.address.setPlaceholderText('Enter Student Address')

    def layouts(self):

        ###################Creating Main Layouts###############
        self.mainLayout = QVBoxLayout()
        self.topImgLayout = QFormLayout()
        self.topNoteLayout = QHBoxLayout()
        self.bottontLayout = QFormLayout()
        ###########Adding child layouts to main layout###########
        self.mainLayout.addLayout(self.topImgLayout)
        self.mainLayout.addLayout(self.bottontLayout)
        ############Adding wigdets to layouts#############
        self.bottontLayout.addRow('', self.title)
        self.bottontLayout.addRow('', self.img)
        self.bottontLayout.addRow('Name: ',self.name)
        self.bottontLayout.addRow('Surname: ',self.surname)
        self.topNoteLayout.addWidget(self.not1)
        self.topNoteLayout.addWidget(self.not2)
        self.topNoteLayout.addWidget(self.not3)
        self.bottontLayout.addRow('Notes: ',self.topNoteLayout)
        self.bottontLayout.addRow('Phone: ',self.phone)
        self.bottontLayout.addRow('Email: ',self.email)
        self.bottontLayout.addRow('Picture: ',self.btnBrowse)
        self.bottontLayout.addRow('Address: ',self.address)
        self.bottontLayout.addRow('',self.btnAdd)
        ###########setting main window layout#############
        self.setLayout(self.mainLayout)

    def uploadImage(self):
        size=(128,128)
        self.fileName,ok = QFileDialog.getOpenFileName(self,'Upload Image','','Image Files(*.jpg *.png')

        if ok:
            self.uploadedImg=os.path.basename(self.fileName)
            img=Image.open(self.fileName)
            img=img.resize(size)
            img.save(f'images/{self.uploadedImg}')

    def addStudent(self):
        img=self.uploadedImg
        name=self.name.text()
        surname=self.surname.text()
        not1=self.not1.text()
        not2=self.not2.text()
        not3=self.not3.text()
        phone=self.phone.text()
        email=self.email.text()
        address=self.address.toPlainText()

        if (name and surname and phone !=""):
            try:
                query = "INSERT INTO oks (name,surname,not1,not2,not3,phone,email,address,img) VALUES(?,?,?,?,?,?,?,?,?)"
                cur.execute(query,(name,surname,not1,not2,not3,phone,email,address,img))
                con.commit()
                QMessageBox.information(self,'Success','Student has been added')
                self.close()
                self.main=Main()
            except:
                QMessageBox.information(self,'Warning','Student has not been added')
        else:
            QMessageBox.information(self, 'Warning', 'Fields can not be empty')

    # def noteCalculate(self):
    #     pass
    #
    #     global person_id
    #     query="SELECT * FROM oks WHERE id=?"
    #     student = cur.execute(query,(person_id,)).fetchone()
    #     # print(student)
    #     self.name_sql=student[1]
    #     self.surname_sql=student[2]
    #     self.not1_sql=str(student[3])
    #     self.not2_sql=str(student[4])
    #     self.not3_sql=str(student[5])
    #     self.phone_sql=student[6]
    #     self.email_sql=student[7]
    #     self.address_sql=student[8]
    #     self.img_sql=student[9]

        # if ortalama >= 90 and self.ortalama < 100:
        #     harf = 'AA'
        # elif ortalama >= 85 and self.ortalama < 89:
        #     harf = 'BA'
        # elif ortalama >= 80 and self.ortalama < 84:
        #     harf = 'BB'
        # elif ortalama >= 75 and self.ortalama < 79:
        #     harf = 'CB'
        # elif ortalama >= 70 and self.ortalama < 74:
        #     harf = 'CC'
        # elif ortalama >= 65 and self.ortalama < 69:
        #     harf = 'DC'
        # elif ortalama >= 60 and self.ortalama < 64:
        #     harf = 'DD'
        # elif ortalama >= 50 and self.ortalama < 59:
        #     harf = 'FD'
        # else:
        #     harf = 'FF'
        #
        # return harf

class UpdateStudent(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Update Student')
        self.setGeometry(600,130,350,500)
        self.show()
        self.UI()

        self.uploadedImg = '1.png'
    def UI(self):
        self.getPerson()
        self.mainDesign()
        self.layouts()

    def closeEvent(self, event):            ##### ekranı kapattığında ana ekranın geri gelmesi
        self.main = Main()

    def getPerson(self):
        global person_id
        query="SELECT * FROM oks WHERE id=?"
        student = cur.execute(query,(person_id,)).fetchone()
        # print(student)
        self.name_sql=student[1]
        self.surname_sql=student[2]
        self.not1_sql=str(student[3])
        self.not2_sql=str(student[4])
        self.not3_sql=str(student[5])
        self.phone_sql=student[6]
        self.email_sql=student[7]
        self.address_sql=student[8]
        self.img_sql=student[9]

    def mainDesign(self):
        ################Top Layout widgets#######################
        self.setStyleSheet('background-color:white;font-size:12pt;font-family:Times;')
        self.title = QLabel('Update Person')
        self.title.setStyleSheet('color:red;font-size:24pt;font-family:Times;')
        self.img = QLabel()
        self.img.setPixmap(QPixmap(f'images/{self.img_sql}'))       #Dikkat
        self.name = QLineEdit(self.name_sql)
        self.surname = QLineEdit(self.surname_sql)
        self.not1 = QLineEdit(self.not1_sql)
        self.not1.setPlaceholderText('1st Note')
        self.not2 = QLineEdit(self.not2_sql)
        self.not2.setPlaceholderText('2nd Note')
        self.not3 = QLineEdit(self.not3_sql)
        self.not3.setPlaceholderText('3rd Note')
        self.phone = QLineEdit(self.phone_sql)
        self.email = QLineEdit(self.email_sql)
        self.address = QTextEdit(self.address_sql)
        # self.address.setFixedWidth(180)
        ################Bottom Layout Widgets####################
        self.btnBrowse = QPushButton('Browse')
        self.btnBrowse.setStyleSheet('background-color: orange; font-size: 10;')
        self.btnBrowse.clicked.connect(self.uploadImage)
        self.btnUpdate = QPushButton('Update')
        self.btnUpdate.clicked.connect(self.updateStudent)
        self.btnUpdate.setStyleSheet('background-color: red; font-size: 10;')

    def layouts(self):
        ###################Creating Main Layouts###############
        self.mainLayout = QVBoxLayout()
        self.topImgLayout = QFormLayout()
        self.topNoteLayout = QHBoxLayout()
        self.bottontLayout = QFormLayout()
        ###########Adding child layouts to main layout###########
        self.mainLayout.addLayout(self.topImgLayout)
        self.mainLayout.addLayout(self.bottontLayout)
        ############Adding wigdets to layouts#############
        self.bottontLayout.addRow('', self.title)
        self.bottontLayout.addRow('', self.img)
        self.bottontLayout.addRow('Name: ',self.name)
        self.bottontLayout.addRow('Surname: ',self.surname)
        self.topNoteLayout.addWidget(self.not1)
        self.topNoteLayout.addWidget(self.not2)
        self.topNoteLayout.addWidget(self.not3)
        self.bottontLayout.addRow('Notes: ',self.topNoteLayout)
        self.bottontLayout.addRow('Phone: ',self.phone)
        self.bottontLayout.addRow('Email: ',self.email)
        self.bottontLayout.addRow('Picture: ',self.btnBrowse)
        self.bottontLayout.addRow('Address: ',self.address)
        self.bottontLayout.addRow('',self.btnUpdate)
        ###########setting main window layout#############
        self.setLayout(self.mainLayout)

    def uploadImage(self):
        size = (128, 128)
        self.fileName, ok = QFileDialog.getOpenFileName(self, 'Upload Image', '', 'Image Files(*.jpg *.png')

        if ok:
            self.uploadedImg = os.path.basename(self.fileName)
            img = Image.open(self.fileName)
            img = img.resize(size)
            img.save(f'images/{self.uploadedImg}')

    def updateStudent(self):
        global person_id
        img=self.uploadedImg
        name=self.name.text()
        surname=self.surname.text()
        not1=self.not1.text()
        not2=self.not2.text()
        not3=self.not3.text()
        phone=self.phone.text()
        email=self.email.text()
        address=self.address.toPlainText()

        if (name and surname and phone !=""):
            try:
                query="UPDATE oks set name=?, surname=?, not1=?, not2=?, not3=?, phone=?, email=?, address=?, img=? WHERE id=?"
                cur.execute(query,(name,surname,not1,not2,not3,phone,email,address,img,person_id))      # id yi koymayı unutma
                con.commit()
                QMessageBox.information(self,'Success','Student has been updated')
                self.close()
                self.main=Main()
            except:
                QMessageBox.information(self,'Warning','Student has not been updated')
        else:
            QMessageBox.information(self, 'Warning', 'Fields can not be empty')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Main()
    sys.exit(app.exec_())
