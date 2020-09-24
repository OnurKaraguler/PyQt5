import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt



class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Slider Widget')
        self.setGeometry(350,150,600,500)
        self.UI()

    def UI(self):
        vbox = QVBoxLayout()
        self.slider = QSlider(Qt.Horizontal)     # Boş olursaVertical Slider
        self.slider.setMinimum(0)
        self.slider.setMaximum(100)
        self.slider.setTickPosition(QSlider.TicksAbove)
        self.slider.setTickInterval(10)
        self.slider.valueChanged.connect(self.getValue)
        self.text1 = QLabel('0')
        self.text1.setAlignment(Qt.AlignHCenter)
        self.text2 = QLabel('Hello Python')

        vbox.addStretch()
        vbox.addWidget(self.text1)
        vbox.addWidget(self.text2)
        vbox.addWidget(self.slider)


        self.setLayout(vbox)

    def getValue(self):
        val = self.slider.value()
        self.text1.setText(str(val))            # integer değeri string değere çevirmelisin
        fontSize = self.slider.value()
        font = QFont('Times', fontSize)
        self.text2.setFont(font)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())