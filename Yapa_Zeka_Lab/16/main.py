from PyQt5.QtWidgets import QApplication
from main_page import MainPage

app = QApplication([])
window = MainPage()
window.show()
app.exec_()