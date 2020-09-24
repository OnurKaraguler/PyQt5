import sys,os
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap
import sqlite3
from PIL import Image
from PyQt5.QtCore import *
from PyQt5 import QtCore

con = sqlite3.connect('oks.db')
cur = con.cursor()
person_id=None
class Main(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('OKS')
        self.setGeometry(430,120,610,510)
        self.setFixedSize(610,510)
        self.UI()
        self.show()

    def UI(self):
        self.mainDesign()
        self.layouts()
        self.getStudents()
        self.displayFirstRecord()

    def mainDesign(self):
        self.setStyleSheet("background-color: brown;")
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
        self.TCNo = QLabel()
        self.name = QLabel()
        self.surname = QLabel()
        self.phone = QLabel()
        self.email = QLabel()
        # self.email.setFixedWidth(220)
        self.address = QLabel()
        self.address.setWordWrap(True)          # Yazı alana kendisini sığdırıyor
        # self.address.setFixedSize(150,100)
        self.address.setAlignment(Qt.AlignTop|Qt.AlignLeft)

        self.scoreQlb = QLabel('Scores: ')
        self.scoreQlb_1 = QLabel('1.')
        self.scoreQlb_2 = QLabel('2.')
        self.scoreQlb_3 = QLabel('3.')
        self.averageScoreQlb = QLabel('Avg.')
        self.averageGradeQlb = QLabel('Grade')
        self.score_1 = QLabel()
        self.score_2 = QLabel()
        self.score_3 = QLabel()
        self.averageScore = QLabel()
        self.success_grade = QLabel()


    def layouts(self):
        ###################Creating Frames###############
        self.frameInfo = QFrame(self)
        self.frameInfo.setStyleSheet("background-color: white;")
        self.frameInfo.setGeometry(QtCore.QRect(10, 10, 300, 240))
        self.frameInfo.setFrameShape(QFrame.Box)
        self.frameInfo.setFrameShadow(QFrame.Sunken)
        self.frameInfo.setLineWidth(2)

        self.frameSign = QFrame(self)
        self.frameSign.setStyleSheet("background-color: blue;")
        self.frameSign.setGeometry(QtCore.QRect(20, 20, 75, 75))
        self.signShow = QLabel(self.frameSign)

        self.frameScore = QFrame(self)
        # self.frameScore.setStyleSheet("background-color: rgb(255, 170, 0);")
        self.frameScore.setGeometry(QtCore.QRect(10, 260, 300, 70))
        self.frameScore.setFrameShape(QFrame.Box)
        self.frameScore.setFrameShadow(QFrame.Sunken)
        self.frameScore.setLineWidth(2)

        self.frameContInfo = QFrame(self)
        # self.frameContInfo.setStyleSheet("background-color: rgb(255, 170, 0);")
        self.frameContInfo.setGeometry(QtCore.QRect(10, 340, 300, 160))
        self.frameContInfo.setFrameShape(QFrame.Box)
        self.frameContInfo.setFrameShadow(QFrame.Sunken)
        self.frameContInfo.setLineWidth(2)

        self.frameRightMain = QFrame(self)
        # self.frameContInfo.setStyleSheet("background-color: rgb(255, 170, 0);")
        self.frameRightMain.setGeometry(QtCore.QRect(320, 10, 280, 490))
        self.frameRightMain.setFrameShape(QFrame.Box)
        self.frameRightMain.setFrameShadow(QFrame.Sunken)
        self.frameRightMain.setLineWidth(2)
        ###################Creating Main Layouts###############
        self.mainLayout = QHBoxLayout()
        self.leftTopLayout = QFormLayout(self.frameInfo)
        self.leftScoreLayout = QGridLayout(self.frameScore)
        self.leftBottomLayout = QFormLayout(self.frameContInfo)
        self.leftMainLayout = QVBoxLayout()

        self.rightMainLayout = QVBoxLayout(self.frameRightMain)
        self.rightTopLayout = QVBoxLayout()
        self.rightBottomLayout = QHBoxLayout()
        ###########Adding child layouts to main layout###########
        self.leftMainLayout.addLayout(self.leftTopLayout)
        self.leftMainLayout.addLayout(self.leftScoreLayout)
        self.leftMainLayout.addLayout(self.leftBottomLayout)
        # self.mainLayout.addLayout(self.leftMainLayout, 40)

        self.rightMainLayout.addLayout(self.rightTopLayout)
        self.rightMainLayout.addLayout(self.rightBottomLayout)
        # self.mainLayout.addLayout(self.rightMainLayout, 60)
        ############Adding wigdets to layouts#############
        self.leftTopLayout.setVerticalSpacing(10)
        self.leftTopLayout.addRow('', self.img)
        self.leftTopLayout.addRow('T.C. No: ', self.TCNo)
        self.leftTopLayout.addRow('Name: ', self.name)
        self.leftTopLayout.addRow('Surname : ', self.surname)

        self.leftScoreLayout.addWidget(self.scoreQlb,1,0)
        self.leftScoreLayout.addWidget(self.scoreQlb_1,0,1)
        self.leftScoreLayout.addWidget(self.scoreQlb_2,0,2)
        self.leftScoreLayout.addWidget(self.scoreQlb_3,0,3)
        self.leftScoreLayout.addWidget(self.averageScoreQlb,0,4)
        self.leftScoreLayout.addWidget(self.averageGradeQlb,0,5)
        self.leftScoreLayout.addWidget(self.score_1,1,1)
        self.leftScoreLayout.addWidget(self.score_2,1,2)
        self.leftScoreLayout.addWidget(self.score_3,1,3)
        self.leftScoreLayout.addWidget(self.averageScore,1,4)
        self.leftScoreLayout.addWidget(self.success_grade,1,5)

        self.leftBottomLayout.setVerticalSpacing(10)
        self.leftBottomLayout.addRow('Phone: ', self.phone)
        self.leftBottomLayout.addRow('Email: ', self.email)
        self.leftBottomLayout.addRow('Address: ', self.address)

        self.rightTopLayout.addWidget(self.studentList)

        self.rightBottomLayout.addWidget(self.btnNew)
        self.rightBottomLayout.addWidget(self.btnUpdate)
        self.rightBottomLayout.addWidget(self.btnDelete)
        ###########setting main window layout############
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
        query = "SELECT id,name,surname FROM oks"       # listeden istediğini seç
        students = cur.execute(query).fetchall()
        for student in students:
            self.studentList.addItem(str(student[0])+'-'+student[1]+' '+student[2])

    def displayFirstRecord(self):
        query = "SELECT * FROM oks ORDER BY ROWID ASC LIMIT 1"
        student = cur.execute(query).fetchone()
        self.TCNo.setText(str(student[1]))
        self.name.setText(student[2])
        self.surname.setText(student[3])
        self.phone.setText(student[4])
        self.email.setText(student[5])
        self.address.setText(student[6])
        self.img.setText(self.img.setPixmap(QPixmap('images/'+student[7])))
        self.score_1.setText(str(student[8]))
        self.score_2.setText(str(student[9]))
        self.score_3.setText(str(student[10]))
        self.averageScore.setText(str(student[11]))
        self.success_grade.setText(student[12])
        print(student[1], student[2], student[3], student[4], student[6], student[7], student[8], student[9],student[10], student[11], student[12])

        if (student[12] == 'AA' or student[12] == 'BA' or student[12] == 'BB' or student[12] == 'CB' or student[12] == 'CC'):
            self.frameScore.setStyleSheet("background-color: green;")
            self.signShow.setPixmap(QPixmap('images/succeded.png'))

        elif (student[12] == 'CD' or student[12] == 'DC' or student[12] == 'DD'):
            self.frameScore.setStyleSheet("background-color: orange;")
            self.signShow.setPixmap(QPixmap('images/succeded.png'))
        else:
            self.frameScore.setStyleSheet("background-color: red;")
            self.signShow.setPixmap(QPixmap('images/failed.png'))

    def singleClick(self):
        student = self.studentList.currentItem().text()
        id = student.split('-')[0]
        query = ("SELECT * FROM oks WHERE id=?")
        student = cur.execute(query,(id,)).fetchone()
        self.TCNo.setText(str(student[1]))      # Sayı olunca str çevir
        self.name.setText(student[2])
        self.surname.setText(student[3])
        self.phone.setText(student[4])
        self.email.setText(student[5])
        self.address.setText(student[6])
        self.img.setText(self.img.setPixmap(QPixmap('images/'+student[7])))
        self.score_1.setText(str(student[8]))
        self.score_2.setText(str(student[9]))
        self.score_3.setText(str(student[10]))
        self.averageScore.setText(str(student[11]))
        self.success_grade.setText(student[12])

        if (student[12] == 'AA' or student[12] == 'BA' or student[12] == 'BB' or student[12] == 'CB' or student[12] == 'CC'):
            self.frameScore.setStyleSheet("background-color: green;")
            self.signShow.setPixmap(QPixmap('images/succeded.png'))
        elif (student[12] == 'CD' or student[12] == 'DC' or student[12] == 'DD'):
            self.frameScore.setStyleSheet("background-color: orange;")
            self.signShow.setPixmap(QPixmap('images/succeded.png'))
        else:
            self.frameScore.setStyleSheet("background-color: red;")
            self.signShow.setPixmap(QPixmap('images/failed.png'))

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

###############################################################################################################
###############################################################################################################
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
        self.score_1 = QLineEdit('0')       # daha sonra işlem göreceğinden 0 olarak kalmalı
        self.score_1.setPlaceholderText('1st Score')
        self.score_2 = QLineEdit('0')
        self.score_2.setPlaceholderText('2nd Score')
        self.score_3 = QLineEdit('0')
        self.score_3.setPlaceholderText('3rd Score')
        ################Bottom Layout Widgets####################
        self.TCNo = QLineEdit('0')
        self.TCNo.setPlaceholderText('Enter Student T.C. No')
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
        self.btnBrowse = QPushButton('Browse')
        self.btnBrowse.setStyleSheet('background-color: orange; font-size: 10;')
        self.btnBrowse.clicked.connect(self.uploadImage)
        self.btnAdd = QPushButton('Add')
        self.btnAdd.clicked.connect(self.addStudent)
        self.btnAdd.setStyleSheet('background-color: red; font-size: 10;')

    def layouts(self):
        ###################Creating Main Layouts###############
        self.mainLayout = QVBoxLayout()
        self.topImgLayout = QFormLayout()
        self.topScoreLayout = QHBoxLayout()
        self.bottontLayout = QFormLayout()
        ###########Adding child layouts to main layout###########
        self.mainLayout.addLayout(self.topImgLayout)
        self.mainLayout.addLayout(self.bottontLayout)
        ############Adding wigdets to layouts#############
        self.bottontLayout.addRow('', self.title)
        self.bottontLayout.addRow('', self.img)
        self.bottontLayout.addRow('TCNo: ',self.TCNo)
        self.bottontLayout.addRow('Name: ',self.name)
        self.bottontLayout.addRow('Surname: ',self.surname)

        self.topScoreLayout.addWidget(self.score_1)
        self.topScoreLayout.addWidget(self.score_2)
        self.topScoreLayout.addWidget(self.score_3)

        self.bottontLayout.addRow('Scores: ', self.topScoreLayout)
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
        pass
        img=self.uploadedImg
        TCNo=self.TCNo.text()
        name=self.name.text()
        surname=self.surname.text()
        score_1=self.score_1.text()
        score_2=self.score_2.text()
        score_3=self.score_3.text()
        phone=self.phone.text()
        email=self.email.text()
        address=self.address.toPlainText()
        self.averageScore = (int(self.score_1.text()) + int(self.score_2.text()) + int(self.score_3.text())) / 3
        self.success_grade = self.finding_success_grade(self.averageScore)

        if (name and surname and phone !=""):
            try:
                query = "INSERT INTO oks (TCNo,name,surname,phone,email,address,img,score_1,score_2,score_3,averageScore,grade) VALUES(?,?,?,?,?,?,?,?,?,?,?,?)"
                cur.execute(query,(TCNo,name,surname,phone,email,address,img,score_1,score_2,score_3,self.averageScore, self.success_grade))
                con.commit()
                QMessageBox.information(self,'Success','Student has been added')
                self.close()
                self.main=Main()
            except:
                QMessageBox.information(self,'Warning','Student has not been added')
        else:
            QMessageBox.information(self, 'Warning', 'Fields can not be empty')

    def finding_success_grade(self,averageScore):
        if self.averageScore >= 90 and self.averageScore < 100:
            grade = 'AA'
        elif self.averageScore >= 85 and self.averageScore < 89:
            grade = 'BA'
        elif self.averageScore >= 80 and self.averageScore < 84:
            grade = 'BB'
        elif self.averageScore >= 75 and self.averageScore < 79:
            grade = 'CB'
        elif self.averageScore >= 70 and self.averageScore < 74:
            grade = 'CC'
        elif self.averageScore >= 65 and self.averageScore < 69:
            grade = 'DC'
        elif self.averageScore >= 60 and self.averageScore < 64:
            grade = 'DD'
        elif self.averageScore >= 50 and self.averageScore < 59:
            grade = 'FD'
        else:
            grade = 'FF'

        return grade

###############################################################################################################
###############################################################################################################
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
        self.TCNo_sql=str(student[1])           # Sayı olunca str çevir
        self.name_sql=student[2]
        self.surname_sql=student[3]
        self.phone_sql=student[4]
        self.email_sql=student[5]
        self.address_sql=student[6]
        self.image_sql=student[7]
        self.score_1_sql=student[8]
        self.score_2_sql=student[9]
        self.score_3_sql=student[10]
        self.averageScore_sql=student[11]
        self.success_grade_sql=student[12]

    def mainDesign(self):
        ################Top Layout widgets#######################
        self.setStyleSheet('background-color:white;font-size:12pt;font-family:Times;')
        self.title = QLabel('Update Person')
        self.title.setStyleSheet('color:red;font-size:24pt;font-family:Times;')
        self.img = QLabel()
        self.img.setPixmap(QPixmap(f'images/{self.image_sql}'))       # Dikkat
        self.score_1 = QLineEdit(str(self.score_1_sql))
        self.score_2 = QLineEdit(str(self.score_2_sql))
        self.score_3 = QLineEdit(str(self.score_3_sql))
        ################Bottom Layout Widgets####################
        self.btnBrowse = QPushButton('Browse')
        self.btnBrowse.setStyleSheet('background-color: orange; font-size: 10;')
        self.btnBrowse.clicked.connect(self.uploadImage)
        self.btnUpdate = QPushButton('Update')
        self.btnUpdate.clicked.connect(self.updateStudent)
        self.btnUpdate.setStyleSheet('background-color: red; font-size: 10;')
        self.TCNo = QLineEdit(self.TCNo_sql)
        self.name = QLineEdit(self.name_sql)
        self.surname = QLineEdit(self.surname_sql)
        self.phone = QLineEdit(self.phone_sql)
        self.email = QLineEdit(self.email_sql)
        self.address = QTextEdit(self.address_sql)
    #
    def layouts(self):
        ###################Creating Main Layouts###############
        self.mainLayout = QVBoxLayout()
        self.topImgLayout = QFormLayout()
        self.topScoreLayout = QHBoxLayout()
        self.bottontLayout = QFormLayout()
        ###########Adding child layouts to main layout###########
        self.mainLayout.addLayout(self.topImgLayout)
        self.mainLayout.addLayout(self.bottontLayout)
        ############Adding wigdets to layouts#############
        self.bottontLayout.addRow('', self.title)
        self.bottontLayout.addRow('', self.img)
        self.bottontLayout.addRow('TCNo: ',self.TCNo)
        self.bottontLayout.addRow('Name: ',self.name)
        self.bottontLayout.addRow('Surname: ',self.surname)

        self.topScoreLayout.addWidget(self.score_1)
        self.topScoreLayout.addWidget(self.score_2)
        self.topScoreLayout.addWidget(self.score_3)

        self.bottontLayout.addRow('Scores: ', self.topScoreLayout)
        self.bottontLayout.addRow('Phone: ',self.phone)
        self.bottontLayout.addRow('Email: ',self.email)
        self.bottontLayout.addRow('Picture: ',self.btnBrowse)
        self.bottontLayout.addRow('Address: ',self.address)
        self.bottontLayout.addRow('', self.btnUpdate)
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

    def updateStudent(self):
        global person_id        # Dikkat
        img = self.uploadedImg
        TCNo = self.TCNo.text()
        name = self.name.text()
        surname = self.surname.text()
        score_1 = self.score_1.text()
        score_2 = self.score_2.text()
        score_3 = self.score_3.text()
        phone = self.phone.text()
        email = self.email.text()
        address = self.address.toPlainText()
        self.averageScore = (int(self.score_1.text()) + int(self.score_2.text()) + int(self.score_3.text())) / 3
        self.success_grade = self.finding_success_grade(self.averageScore)
        # print(img, TCNo, name, surname,score_1,score_2,score_3,phone,email,address, self.averageScore,self.success_grade)

        if (name and surname and phone != ""):
            try:
                query = "UPDATE oks set TCNo=?, name =?,surname=?,phone=?,email=?,address=?,img=?,score_1=?,score_2=?,score_3=?,averageScore=?,grade=? WHERE id=?"
                cur.execute(query, (TCNo, name, surname, phone, email, address, img, score_1, score_2, score_3, self.averageScore, self.success_grade, person_id))
                con.commit()
                QMessageBox.information(self, 'Success', 'Student has been updated')
                self.close()
                self.main = Main()
            except:
                QMessageBox.information(self, 'Warning', 'Student has not been updated')
        else:
            QMessageBox.information(self, 'Warning', 'Fields can not be empty')

    def finding_success_grade(self, averageScore):
        if self.averageScore >= 90 and self.averageScore < 100:
            grade = 'AA'
        elif self.averageScore >= 85 and self.averageScore < 89:
            grade = 'BA'
        elif self.averageScore >= 80 and self.averageScore < 84:
            grade = 'BB'
        elif self.averageScore >= 75 and self.averageScore < 79:
            grade = 'CB'
        elif self.averageScore >= 70 and self.averageScore < 74:
            grade = 'CC'
        elif self.averageScore >= 65 and self.averageScore < 69:
            grade = 'DC'
        elif self.averageScore >= 60 and self.averageScore < 64:
            grade = 'DD'
        elif self.averageScore >= 50 and self.averageScore < 59:
            grade = 'FD'
        else:
            grade = 'FF'

        return grade


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Main()
    sys.exit(app.exec_())
