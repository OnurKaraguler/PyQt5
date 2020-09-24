import sys, os
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
import sqlite3
from PIL import Image
import addlesson

con = sqlite3.connect('lessons.db')
cur = con.cursor()

#######################################################################################
class Main(QMainWindow):
#######################################################################################
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Product Manager')
        self.setWindowIcon(QIcon('icons/books.jpg'))
        self.setGeometry(100,100,1200,600)
        self.setFixedSize(self.size())          #Ekran ölçüsünü sabitlemek için
        self.UI()
        self.show()


    def UI(self):
        self.toolBar()
        self.tabWidget()
        self.widgets()
        self.layout()
        self.displaySubjects()

    def toolBar(self):
        self.tb = self.addToolBar('Tool Bar')
        self.tb.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)  # toolbutton altında yazı olması (Qt modülünü import et)
        ######################Toolbar Buttons###################
        ######################Add Subjects###################
        self.addSubject = QAction(QIcon('icons/classroom.png'), 'Add Subject', self)
        self.tb.addAction(self.addSubject)
        self.addSubject.triggered.connect(self.funkAddSubject)
        self.tb.addSeparator()


    def tabWidget(self):
        self.tabs = QTabWidget()
        self.tabs.blockSignals(True)
        self.setCentralWidget(self.tabs)  # tab in gözükmesi için
        self.tab1 = QWidget()
        self.tabs.addTab(self.tab1, 'Subjects')

    def widgets(self):
        ######################Tab1 Widgets###################
        ##################Main Left Layout Widgets##############
        self.lessonsTable = QTableWidget()
        self.lessonsTable.setColumnCount(6)
        self.lessonsTable.setColumnHidden(0, True)  # Kolon u gizlemek için
        self.tabs.currentChanged.connect(self.tabChanged)
        self.lessonsTable.setHorizontalHeaderItem(0, QTableWidgetItem('Lesson Id'))
        self.lessonsTable.setHorizontalHeaderItem(1, QTableWidgetItem('Lesson Name'))
        self.lessonsTable.setHorizontalHeaderItem(2, QTableWidgetItem('Subject'))
        self.lessonsTable.setHorizontalHeaderItem(3, QTableWidgetItem('Progress'))
        self.lessonsTable.setHorizontalHeaderItem(4, QTableWidgetItem('Question'))
        self.lessonsTable.setHorizontalHeaderItem(5, QTableWidgetItem('Status'))
        self.lessonsTable.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)  # Kolonun genişliğini sabitleme
        self.lessonsTable.horizontalHeader().setSectionResizeMode(2, QHeaderView.Stretch)
        self.lessonsTable.doubleClicked.connect(self.selectedLesson)
        ##################Right Top Layout Widgets##############
        self.searchText = QLabel('Search')
        self.searchEntry = QLineEdit()
        self.searchEntry.setPlaceholderText('Search For Lessons')
        self.searchButton = QPushButton('Search')
        self.searchButton.clicked.connect(self.seachSubject)
        ##################Right Middle Layout Widgets##############
        self.allSubjects = QRadioButton('All Lessons')
        self.continuingSubjects = QRadioButton('Continuingg')
        self.completedSubjects = QRadioButton('Completed')
        self.allSubjects.setChecked(True)
        self.listButton = QPushButton('List')
        self.listButton.clicked.connect(self.listLessons)
    def layout(self):
        ###########################################
        ##################Tab1 Layout##############
        ###########################################
        self.mainLayout = QHBoxLayout()

        self.mainLeftLayout = QVBoxLayout()
        self.rightTopLayout = QHBoxLayout()
        self.rightMiddleLayout = QHBoxLayout()
        self.mainRightLayout = QVBoxLayout()

        self.topGroupBox = QGroupBox('Search Box')
        self.topGroupBox.setLayout(self.rightTopLayout)
        self.mainRightLayout.addWidget(self.topGroupBox,20)        # GroupBox lar Widget tir.
        self.middleGroupBox = QGroupBox('List Box')

        self.buttomGroupBox = QGroupBox()                       # yan menü de düzenleme için boş olacak
        self.middleGroupBox.setLayout(self.rightMiddleLayout)
        self.mainRightLayout.addWidget(self.middleGroupBox,20)
        self.mainRightLayout.addWidget(self.buttomGroupBox,60)

        self.mainLayout.addLayout(self.mainLeftLayout,70)       # leftLayout %70 yer kaplayacak
        self.mainLayout.addLayout(self.mainRightLayout,30)

        self.tab1.setLayout(self.mainLayout)            # Mevcut Main Layout u tab1 e bağlama
        ##################Add Widgets##############
        ##################Left Main Layout Widgets##############
        self.mainLeftLayout.addWidget(self.lessonsTable)
        ##################Right Top Layout Widgets##############
        self.rightTopLayout.addWidget(self.searchText)
        self.rightTopLayout.addWidget(self.searchEntry)
        self.rightTopLayout.addWidget(self.searchButton)

        ##################Right Middle Layout Widgets##############
        self.rightMiddleLayout.addWidget(self.allSubjects)
        self.rightMiddleLayout.addWidget(self.continuingSubjects)
        self.rightMiddleLayout.addWidget(self.completedSubjects)
        self.rightMiddleLayout.addWidget(self.listButton)

        self.tabs.blockSignals(False)

    def funkAddSubject(self):
        self.newProduct = addlesson.AddLesson()

    def seachSubject(self):
        value = self.searchEntry.text()
        if value == '':
            QMessageBox.information(self, 'Warning', 'Search query cant be empty')
        else:
            self.searchEntry.setText('')
            query = (
                "SELECT lesson_id, lesson_name, lesson_subject, lesson_progress, lesson_question,"
                     "lesson_status FROM lessons WHERE lesson_name LIKE ? or lesson_subject LIKE ? ")
            results = cur.execute(query, ('%' + value + '%', '%' + value + '%')).fetchall()
            # print(results)

            if results == []:
                QMessageBox.information(self, 'Warning', 'There is no such a lesson or subject')
            else:
                for i in reversed(range(self.lessonsTable.rowCount())):
                    self.lessonsTable.removeRow(i)
                for row_data in results:
                    row_number = self.lessonsTable.rowCount()
                    self.lessonsTable.insertRow(row_number)
                    for column_number, data in enumerate(row_data):
                        self.lessonsTable.setItem(row_number, column_number, QTableWidgetItem(str(data)))

    def listLessons(self):
        if self.allSubjects.isChecked() == True:
            self.displaySubjects()
        elif self.continuingSubjects.isChecked() == True:
            query = ("SELECT lesson_id, lesson_name, lesson_subject, lesson_progress, lesson_question,"
                     "lesson_status FROM lessons WHERE lesson_status='Continuing' ")
            lessons = cur.execute(query).fetchall()       # soru işareti yok

            for i in reversed(range(self.lessonsTable.rowCount())):
                self.lessonsTable.removeRow(i)

            for row_data in lessons:
                row_number = self.lessonsTable.rowCount()
                self.lessonsTable.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.lessonsTable.setItem(row_number, column_number, QTableWidgetItem(str(data)))

        elif self.completedSubjects.isChecked() == True:
            query = ("SELECT lesson_id, lesson_name, lesson_subject, lesson_progress, lesson_question,"
                     "lesson_status FROM lessons WHERE lesson_status='Completed' ")
            lessons = cur.execute(query).fetchall()  # soru işareti yok

            for i in reversed(range(self.lessonsTable.rowCount())):
                self.lessonsTable.removeRow(i)

            for row_data in lessons:
                row_number = self.lessonsTable.rowCount()
                self.lessonsTable.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.lessonsTable.setItem(row_number, column_number, QTableWidgetItem(str(data)))

    def displaySubjects(self):
        self.lessonsTable.setFont(QFont('Times',12))
        for i in reversed(range(self.lessonsTable.rowCount())):
            self.lessonsTable.removeRow(i)

        query = cur.execute('SELECT lesson_id,lesson_name,lesson_subject,lesson_progress,lesson_question,lesson_status FROM lessons')
        for row_data in query:
            row_number = self.lessonsTable.rowCount()
            self.lessonsTable.insertRow(row_number)
            for column_number,data in enumerate(row_data):
                self.lessonsTable.setItem(row_number, column_number, QTableWidgetItem(str(data)))

        self.lessonsTable.setEditTriggers((QAbstractItemView.NoEditTriggers))      # Tabloda verilerin değiştirilmemesi için

    def selectedLesson(self):
        global lessonId
        listLessons = []
        for i in range(0, 6):  # id dahil 6 kolon var
            listLessons.append(self.lessonsTable.item(self.lessonsTable.currentRow(), i).text())

        lessonId = listLessons[0]
        self.display = DisplayLesson()
        self.display.show()

    def tabChanged(self):           # 4  -> Ekranı güncellemek için ÖNEMLİ
        # self.getStatistics()
        self.DisplayLesson()
        # self.displayMember()

    def xxx(self):
        query = cur.execute('SELECT lesson_id,lesson_name,lesson_subject,lesson_progress,lesson_question,lesson_status FROM lessons')

#######################################################################################
class DisplayLesson(QWidget):
#######################################################################################
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Lesson Details')
        self.setWindowIcon(QIcon('icons/books.jpg'))
        self.setGeometry(450,150,350,550)
        self.setFixedSize(self.size())
        self.UI()
        self.show()

    def UI(self):
        self.lessonDetails()
        self.widgets()
        self.layouts()

    def lessonDetails(self):
        global lessonId
        query = ('SELECT * FROM lessons WHERE lesson_id=?')
        lesson = cur.execute(query,(lessonId,)).fetchone()#single item tuple=(1,)
        self.lessonName = lesson[1]
        self.lessonSubject = lesson[2]
        self.lessonProgress = int(lesson[3])
        self.lessonQuestion = str(lesson[4])
        self.lessonStatus = lesson[5]
        # print(self.lessonName, self.lessonSubject,self.lessonProgress, self.lessonQuestion, self.lessonStatus)

    def widgets(self):
        ##################Top Layout Widgets##############
        self.lessonImg = QLabel()
        self.img = QPixmap(f'img/{self.lessonName}.png')
        self.lessonImg.setPixmap(self.img)
        self.lessonImg.setAlignment(Qt.AlignCenter)
        self.lessonImg.setFixedSize(350, 300)
        # self.titleText =QLabel('Update Lesson')
        # self.titleText.setAlignment(Qt.AlignCenter)
        ##################Bottom Layout Widgets##############
        self.lessonsCompo = QComboBox()
        self.lessonsCompo.addItems(['Türkçe','Matematik','Fen'])
        self.lessonsCompo.setCurrentText(self.lessonName)
        self.subjectEntry = QLineEdit()
        self.subjectEntry.setText(self.lessonSubject)
        self.progressEntry = QSpinBox()
        self.progressEntry.setRange(0,100)
        self.progressEntry.setValue(self.lessonProgress)
        self.progressEntry.setSingleStep(5)
        self.questionEntry = QLineEdit()
        self.questionEntry.setText(self.lessonQuestion)
        self.statusCompo = QComboBox()
        self.statusCompo.addItems(['Continuing','Completed'])
        self.deleteBtn = QPushButton('Delete')
        self.deleteBtn.clicked.connect(self.deleteLesson)
        self.updateBtn = QPushButton('Update')
        self.updateBtn.clicked.connect(self.updateLesson)

    def layouts(self):
        self.mainLayout = QVBoxLayout()

        self.topLayout = QVBoxLayout()
        self.bottomLayout = QFormLayout()
        self.topFrame = QFrame()
        self.bottomFrame = QFrame()

        self.mainLayout.addWidget(self.topFrame)
        self.mainLayout.addWidget(self.bottomFrame)

        self.bottomFrame.setLayout(self.bottomLayout)

        self.setLayout(self.mainLayout)
        ##################Top Layout Widgets##############
        # self.topLayout.addWidget(self.titleText)
        self.topLayout.addWidget(self.lessonImg)
        self.topFrame.setLayout(self.topLayout)
        ##################Form Layout Widgets##############
        self.bottomLayout.addRow(QLabel('Lesson: '),self.lessonsCompo)
        self.bottomLayout.addRow(QLabel('Lesson Subject: '),self.subjectEntry)
        self.bottomLayout.addRow(QLabel('Progress (%): '),self.progressEntry)
        self.bottomLayout.addRow(QLabel('Question: '),self.questionEntry)
        self.bottomLayout.addRow(QLabel('Status: '),self.statusCompo)
        self.bottomLayout.addRow(QLabel(''),self.deleteBtn)
        self.bottomLayout.addRow(QLabel(''),self.updateBtn)

    def deleteLesson(self):
        global lessonId

        mbox = QMessageBox.question(self, "Warning", "Are you sure to delete this subject", QMessageBox.Yes | QMessageBox.No,
                                    QMessageBox.No)
        if (mbox == QMessageBox.Yes):
            try:
                cur.execute("DELETE FROM lessons WHERE lesson_id=?", (lessonId,))
                con.commit()
                QMessageBox.information(self, "Information", "Subject has been deleted!")
                self.close()
            except:
                QMessageBox.information(self, "Information", "Subject has not been deleted!")

    def updateLesson(self):
        global lessonId

        name = self.lessonsCompo.currentText()
        subject = self.subjectEntry.text()
        progress = int(self.progressEntry.value())
        question = int(self.questionEntry.text())
        status = self.statusCompo.currentText()
        # if progress == 100:
        #     status == 'Completed'
        # else:
        #     status = self.statusCompo.currentText()

        if (subject != ''):
            try:
                query = "UPDATE lessons set lesson_name=?, lesson_subject=?, lesson_progress=?, lesson_question=?, lesson_status=? WHERE lesson_id=?"
                cur.execute(query, (name, subject, progress, question, status, lessonId))
                con.commit()
                QMessageBox.information(self, 'Info', 'Subject has been updated')
            except:
                QMessageBox.information(self, 'Info', 'Subject has not been updated')
        else:
            QMessageBox.information(self, 'Info', 'Fields can not be empty')

if __name__=='__main__':
    app = QApplication(sys.argv)
    window = Main()
    sys.exit(app.exec_())