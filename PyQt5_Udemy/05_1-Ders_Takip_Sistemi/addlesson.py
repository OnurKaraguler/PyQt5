import sys, os
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
import sqlite3
from PIL import Image

con = sqlite3.connect('lessons.db')
cur = con.cursor()

#######################################################################################
class AddLesson(QWidget):
#######################################################################################
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Add Subject")
        self.setWindowIcon(QIcon('icons/books.jpg'))
        self.setGeometry(450,150,350,550)
        self.setFixedSize(self.size())
        self.UI()
        self.show()

    def UI(self):
        self.widgets()
        self.layouts()

    def widgets(self):
        ##################Top Layout Widgets##############
        self.addLessonImg = QLabel()
        self.img = QPixmap('img/Türkçe.png')
        self.addLessonImg.setPixmap(self.img)
        self.addLessonImg.setAlignment(Qt.AlignCenter)
        self.addLessonImg.setFixedSize(350, 300)
        self.titleText =QLabel('Add Subject')
        self.titleText.setAlignment(Qt.AlignCenter)

        ##################Bottom Layout Widgets##############
        self.lessonsCompo = QComboBox()
        self.lessonsCompo.addItems(['Türkçe','Matematik','Fen'])
        self.lessonsCompo.activated[str].connect(self.changeImg)
        self.subjectEntry = QLineEdit()
        self.subjectEntry.setPlaceholderText('Enter name of subject')
        self.progressEntry = QSpinBox()
        self.progressEntry.setRange(0,100)
        self.progressEntry.setSingleStep(5)
        self.submitBtn = QPushButton('Submit')
        self.submitBtn.clicked.connect(self.addSubject)

    def layouts(self):
        self.mainLayout = QVBoxLayout()

        self.topLayout = QHBoxLayout()
        self.bottomLayout = QFormLayout()
        self.topFrame = QFrame()
        self.bottomFrame = QFrame()

        self.mainLayout.addWidget(self.topFrame,70)
        self.mainLayout.addWidget(self.bottomFrame,30)

        self.bottomFrame.setLayout(self.bottomLayout)

        self.setLayout(self.mainLayout)
        ##################Top Layout Widgets##############
        # self.topLayout.addWidget(self.titleText)
        self.topLayout.addWidget(self.addLessonImg)
        self.topFrame.setLayout(self.topLayout)
        ##################Form Layout Widgets##############
        self.bottomLayout.addRow(QLabel('Lesson: '),self.lessonsCompo)
        self.bottomLayout.addRow(QLabel('Lesson Subject: '),self.subjectEntry)
        self.bottomLayout.addRow(QLabel('Progress (%): '),self.progressEntry)
        self.bottomLayout.addRow(QLabel(''),self.submitBtn)

    def changeImg(self,text):
        self.lessonsText = text
        if (self.lessonsText == 'Türkçe'):
            self.img = QPixmap('img/Türkçe.jpg')
            self.addLessonImg.setPixmap(self.img)
        elif (self.lessonsText == 'Matematik'):
            self.img = QPixmap('img/Matematik.png')
            self.addLessonImg.setPixmap(self.img)
        else:
            self.img = QPixmap('img/Fen.png')
            self.addLessonImg.setPixmap(self.img)

    def addSubject(self):
        name = self.lessonsCompo.currentText()
        subject = self.subjectEntry.text()
        progress = self.progressEntry.value()

        if (name and subject and progress != ''):
            try:
                query = "INSERT INTO lessons (lesson_name,lesson_subject,lesson_progress) VALUES(?,?,?)"
                cur.execute(query,(name, subject, progress))
                con.commit()
                QMessageBox.information(self,'Info','Subject has been added')
                self.subjectEntry.setText('')
                # self.progressEntry.setValue(0)
            except:
                QMessageBox.information(self, 'Info', 'Subject has not been added')
        else:
            QMessageBox.information(self,'Info','Fields can not be empty')
