import sys, os
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import QtGui
from PyQt5.QtCore import *
from PIL import Image
from datetime import datetime
from datetime import timedelta      # ileri tarihi hesaplamak için
# from datetime import date
# from datetime import time
# import datetime       # tüm modülleri import ediyor


class Main(QWidget):
    count = 0
    def __init__(self,parent=None):
        super(Main, self).__init__(parent)
        self.setWindowTitle('QSplitter demo')
        self.setGeometry(500,150,400,400)
        # self.setFixedSize(self.size())
        self.UI()
        self.show()

    def UI(self):
        self.window()

    def window(self):
        cal = QCalendarWidget(self)
        cal.setGridVisible(True)
        cal.move(20, 20)
        cal.clicked.connect(self.showDate)

        self.lbl = QLabel(self)
        date = cal.selectedDate()
        # self.lbl.setText(str(date))
        # self.lbl.setText(date.toString(Qt.ISODate))
        # self.lbl.setText(date.toString(Qt.DefaultLocaleLongDate))
        # self.lbl.move(20, 200)

        dateTime = QDateTime.currentDateTime()
        print(dateTime.toString())
        print(dateTime.toString(Qt.ISODate))
        print(dateTime.toString(Qt.DefaultLocaleLongDate))
        print('=======================================')
        date = QDate.currentDate()
        print(date.toString())
        print(date.toString(Qt.ISODate))
        print(date.toString(Qt.DefaultLocaleLongDate))
        print('=======================================')
        time = QTime.currentTime()
        print(time.toString())
        print(time.toString(Qt.ISODate))
        print(time.toString(Qt.DefaultLocaleLongDate))
        print('=======================================')
        date_year = QDate.currentDate().year()
        date_month = QDate.currentDate().month()
        date_day = QDate.currentDate().day()
        time_hour = QTime.currentTime().hour()
        time_min = QTime.currentTime().minute()
        print(time_hour, time_min)
        print(date_year,date_month, date_day)
        print('===================BTK====================')
        # simdi = datetime.now()      # datetime.now()=datetime.today()
        # print(simdi.year)
        # print(simdi.month)
        # print(simdi.day)
        # print(simdi.hour)
        # print(simdi.minute)
        # print(simdi.second)

        # result = datetime.ctime(simdi)
        # result = datetime.strftime(simdi,'%Y')         # String olarak veriyor
        # result = datetime.strftime(simdi,'%X')
        # result = datetime.strftime(simdi,'%d')
        # result = datetime.strftime(simdi,'%A')
        # result = datetime.strftime(simdi,'%B')
        # result = datetime.strftime(simdi,'%Y %B %A')    # https://www.w3schools.com/python/python_datetime.asp
        # print(result)

        # t = '21 Nisan 2019'         # elimizde bir obje var diyelim
        # gun, ay, yil = t.split()
        # print(gun)
        # print(ay)
        # print(yil)

        # veya

        # t = '15 April 2019 hour 10:12:30'           # ingilizce olacak
        # dt = datetime.strptime(t, '%d %B %Y hour %H:%M:%S')
        # print(dt)
        # print(dt.year)

        # birthday = datetime(1977,10,20,12,30,00)     # kendimiz de tarih oluşturabiliriz
        # print(birthday)
        # result = datetime.timestamp(birthday)   # tarihi saniye cinsinden verir
        # result = datetime.fromtimestamp(result)     # saniye yi tarih cinsine geri çevirir
        # result = datetime.fromtimestamp(0)          # saniye 1970 ten itibaren hesaplanır.
        simdi = datetime.now()

        # result = simdi - birthday       # timedelta dan gelen bilgi
        # # result1 = result.days
        # result1 = result.seconds
        # print(result, result1)

        # result = simdi + timedelta(days=10)         # ileri tarih hesaplaması için timedelta yı import etmen gerekli
        # result = simdi + timedelta(days=750)
        result = simdi - timedelta(days=10)
        print(result)






        self.vbox=QVBoxLayout()
        self.vbox.addWidget(cal)
        self.vbox.addWidget(self.lbl)

        self.mainLayout = QVBoxLayout()
        self.mainLayout.addLayout(self.vbox)
        self.setLayout(self.mainLayout)

    def showDate(self, date):
        # self.lbl.setText(date.toString())
        # self.lbl.setText(date.toString(Qt.ISODate))
        self.lbl.setText(date.toString(Qt.DefaultLocaleLongDate))

if __name__=='__main__':
    app = QApplication(sys.argv)
    window = Main()
    sys.exit(app.exec_())