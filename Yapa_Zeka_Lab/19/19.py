from PyQt5.QtWidgets import *
from qt_designer_python import Ui_MainWindow

class dersler_19(QMainWindow):

    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton_critical.clicked.connect(self.critical_slot)
        self.ui.pushButton_information.clicked.connect(self.information_slot)
        self.ui.pushButton_question.clicked.connect(self.question_slot)
        self.ui.pushButton_warning.clicked.connect(self.warning_slot)
        self.ui.pushButton_about.clicked.connect(self.about_slot)
        self.ui.pushButton_about_qt.clicked.connect(self.about_qt_slot)
        self.ui.pushButton_numbers.clicked.connect(self.numbers_slot)

    #=================================================================================
    def critical_slot(self):

        #QMessageBox.critical(self,"Kritik Mesaj", "Bu kritik bir mesajdır")

        QMessageBox.critical(self, "Kritik Mesaj", "Bu kritik bir mesajdır", QMessageBox.Yes, QMessageBox.No)

    #=================================================================================
    def information_slot(self):

        result = QMessageBox.information(self, "Bilgi Mesajı", "Bu bir bilgi mesajdır", QMessageBox.Yes, QMessageBox.No)
        print("result : ", result)

        #if result == 16384:
            #print("Kullanıcı Evet dedi")
        #elif result == 65536:
            #print("Kullanıcı Hayır dedi")

        if result == QMessageBox.Yes:
            print("Kullanıcı Evet dedi")
        elif result == QMessageBox.No:
            print("Kullanıcı Hayır dedi")
    #=================================================================================
    def question_slot(self):
        result = QMessageBox.question(self, "Soru Mesajı", "Bu bir soru mesajdır", QMessageBox.Yes | QMessageBox.No | QMessageBox.Ok | QMessageBox.Open | QMessageBox.Save)

    #=================================================================================
    def warning_slot(self):
        QMessageBox.warning(self, "Kritik Mesaj", "Bu kritik bir mesajdır")

    #=================================================================================
    def about_slot(self):
        QMessageBox.about(self, "ders_19 hakkında", "<font size = 5>Bu ders <b>Yapay Zeka labs</b> tarafından anlatılmaktadır"
                                                    "<br><br>"
                                                    "<b>Abone Ol</b>"
                                                    "<br>"
                                                    "<a href=\'https://www.youtube.com/watch?v=Dh4Lcxfjk_4'>Yapay Zeka Labs</a>"
                                                    "<br><br>"
                                                    "<b>İletişim :</b>"
                                                    "<br>"
                                                    "<a href=\'mailto:yapayzekalabs@gmail.com\'>yapayzekalabs@gmail.com</a>"
                                                    "</font>"
                                                    )

    #=================================================================================
    def about_qt_slot(self):
        QMessageBox.aboutQt(self,"Qt hakkında")

    #=================================================================================
    def numbers_slot(self):

        my_message_box = QMessageBox()
        my_message_box.setIcon(QMessageBox.Question)
        my_message_box.setText("Hangi sayıları kullanmak istiyorsun?")
        my_message_box.setWindowTitle("Özel Kullanım")
        my_message_box.setStandardButtons(QMessageBox.Yes|QMessageBox.No)
        my_message_box.setEscapeButton(QMessageBox.Yes)

        button_evet = my_message_box.button(QMessageBox.Yes)
        button_evet.setText("Tek Sayılar")

        button_no = my_message_box.button(QMessageBox.No)
        button_no.setText("Çift Sayılar")

        result = my_message_box.exec_()

        stop = 50
        step = 2
        start = 2

        if result == QMessageBox.Yes:
            start = 1

        elif result == QMessageBox.No:
            start = 0

        self.ui.comboBox_numbers.clear()

        for i in range (start, stop, step):

            self.ui.comboBox_numbers.addItem(str(i))


uygulama = QApplication ([])
pencere = dersler_19()
pencere.show()
uygulama.exec_()