import sys, os
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt


class Main(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('SpinBox demo')
        self.setGeometry(500,150,300,300)
        self.setFixedSize(self.size())          #Ekran ölçüsünü sabitlemek için
        self.UI()
        self.show()

    def UI(self):
        self.window()

    def window(self):
        self.l1=QLabel("current value:")
        self.l1.setAlignment(Qt.AlignCenter)

        self.sp = QSpinBox()
        self.sp.valueChanged.connect(self.valuechange)
        # self.sp.setMinimum(20)
        # self.sp.setMaximum(100)
        self.sp.setRange(20,100)
        self.sp.setValue(50)
        # self.sp.singleStep()

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.l1)
        self.layout.addWidget(self.sp)

        self.mainLayout = QHBoxLayout()
        self.mainLayout.addLayout(self.layout)
        self.setLayout(self.mainLayout)

    def valuechange(self):
        self.l1.setText("current value:" + str(self.sp.value()))




if __name__=='__main__':
    app = QApplication(sys.argv)
    window = Main()
    sys.exit(app.exec_())