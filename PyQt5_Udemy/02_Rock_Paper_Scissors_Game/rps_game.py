import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtCore import QTimer
from random import randint
# from PIL import Image
# from resizeimage import resizeimage

textFont = QFont('Times', 14)
buttonFont = QFont('Arial', 12)
computerScore = 0
playerScore = 0

# with open('images/Stone.png', 'r+b') as f:          # resimi yeniden boyutlandırma
#     with Image.open(f) as image:
#         cover = resizeimage.resize_cover(image, [100, 100])
#         cover.save('images/Stone.jpeg', image.format)
#
# with open('images/paper.jpg', 'r+b') as f:
#     with Image.open(f) as image:
#         cover = resizeimage.resize_cover(image, [100, 100])
#         cover.save('images/paper.jpeg', image.format)
#
# with open('images/scissors.jpg', 'r+b') as f:
#     with Image.open(f) as image:
#         cover = resizeimage.resize_cover(image, [100, 100])
#         cover.save('images/scissors.jpeg', image.format)
#
# with open('images/game.png', 'r+b') as f:
#     with Image.open(f) as image:
#         cover = resizeimage.resize_cover(image, [70, 70])
#         cover.save('images/game.jpeg', image.format)

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Using rps_game')
        self.setGeometry(350,150,500,500)
        self.UI()

    def UI(self):
        ##################Scores########################
        self.scoreComputerText = QLabel('Computer score: ', self)
        self.scoreComputerText.move(30,20)
        self.scoreComputerText.setFont(textFont)
        self.scoreComputerText.resize(150,20)

        self.scorePlayerText = QLabel('Your score: ', self)
        self.scorePlayerText.move(330,20)
        self.scorePlayerText.setFont(buttonFont)
        self.scorePlayerText.resize(150,20)
        #################Images########################
        self.imageComputer = QLabel(self)
        self.imageComputer.setPixmap(QPixmap('images/Stone.jpeg'))
        self.imageComputer.move(50,100)

        self.imagePlayer = QLabel(self)
        self.imagePlayer.setPixmap(QPixmap('images/Stone.jpeg'))
        self.imagePlayer.move(330,100)

        self.imageGame = QLabel(self)
        self.imageGame.setPixmap(QPixmap('images/game.jpeg'))
        self.imageGame.move(210, 120)
        #################Buttons########################
        btnStart = QPushButton('Start', self)
        btnStart.setFont(buttonFont)
        btnStart.move(180,250)
        btnStart.clicked.connect(self.start)

        btnStop = QPushButton('Stop', self)
        btnStop.setFont(buttonFont)
        btnStop.move(270,250)
        btnStop.clicked.connect(self.stop)
        #################Timer########################
        self.timer = QTimer(self)
        self.timer.setInterval(80)
        self.timer.timeout.connect(self.playGame)

    def start(self):
        self.timer.start()

    def playGame(self):
        self.rndComputer = randint(1,3)
        if self.rndComputer == 1:
            self.imageComputer.setPixmap(QPixmap('images/Stone.jpeg'))
        elif self.rndComputer == 2:
            self.imageComputer.setPixmap(QPixmap('images/paper.jpeg'))
        else:
            self.imageComputer.setPixmap(QPixmap('images/scissors.jpeg'))

        self.rndPlayer = randint(1,3)

        if self.rndPlayer == 1:
            self.imagePlayer.setPixmap(QPixmap('images/Stone.jpeg'))
        elif self.rndPlayer == 2:
            self.imagePlayer.setPixmap(QPixmap('images/paper.jpeg'))
        else:
            self.imagePlayer.setPixmap(QPixmap('images/scissors.jpeg'))

    def stop(self):
        global computerScore
        global playerScore
        self.timer.stop()

        if self.rndComputer == 1 and self.rndPlayer == 1:
            mbox = QMessageBox.information(self,'Information', 'Draw Game')
        elif self.rndComputer == 1 and self.rndPlayer == 2:
            mbox = QMessageBox.information(self, 'Information', 'You Win')
            playerScore += 1
            self.scorePlayerText.setText('Your score:{}'.format(playerScore))
        elif self.rndComputer == 1 and self.rndPlayer == 3:
            mbox = QMessageBox.information(self, 'Information', 'Computer Win')
            computerScore += 1
            self.scoreComputerText.setText('Computer score:{}'.format(computerScore))

        elif self.rndComputer == 2 and self.rndPlayer == 1:
            mbox = QMessageBox.information(self, 'Information', 'Computer Win') #
            computerScore += 1
            self.scoreComputerText.setText('Computer score:{}'.format(computerScore))
        elif self.rndComputer == 2 and self.rndPlayer == 2:
            mbox = QMessageBox.information(self, 'Information', 'Draw Game')
        elif self.rndComputer == 2 and self.rndPlayer == 3:
            mbox = QMessageBox.information(self, 'Information', 'You Win')
            playerScore += 1
            self.scorePlayerText.setText('Your score:{}'.format(playerScore))

        elif self.rndComputer == 3 and self.rndPlayer == 1:
            mbox = QMessageBox.information(self, 'Information', 'You Win')  #
            playerScore += 1
            self.scorePlayerText.setText('Your score:{}'.format(playerScore))
        elif self.rndComputer == 3 and self.rndPlayer == 2:
            computerScore += 1
            mbox = QMessageBox.information(self, 'Information', 'Computer Win')
            self.scoreComputerText.setText('Computer score:{}'.format(computerScore))
        elif self.rndComputer == 3 and self.rndPlayer == 3:     #
            mbox = QMessageBox.information(self, 'Information', 'Draw Game')

        if computerScore == 3 or playerScore == 3:
            mbox = QMessageBox.information(self, 'Information', 'Game Over')
            sys.exit()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())