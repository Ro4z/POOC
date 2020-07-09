#detect keyboard press
import sys
import keyboard
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QLabel, QGridLayout, QWidget, QApplication
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import QSize


class MainWindow(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        self.setMinimumSize(QSize(300, 200))
        self.setGeometry(100,100,200,80)
        self.setWindowTitle("PyQt messagebox example")




        while True:  # making a loop
        # used try so that if user pressed other than the given key error will not be shown
            if keyboard.is_pressed('ctrl'):  # if key 'ctrl' is pressed
                print('You Pressed ctrl Key!')
                self.show_alert()
                break

            elif keyboard.is_pressed('alt'):  # if key 'alt' is pressed
                print('You Pressed Alt Key!')
                self.show_alert()
                break

            elif keyboard.is_pressed('win'):  # if key 'window' is pressed
                print('You Pressed window Key!')
                self.show_alert()
                break

    def show_alert(self):
        QtWidgets.QMessageBox.about(self,"Warning","Don't press this key")
    """
    def detect(self):
        while True:
            if keyboard.is_pressed('a'):
                QMessageBox.about(self, "WARNING", "특수키를 입력하였습니다.")
                break

        #pybutton = QPushButton('Show messagebox', self)
        #pybutton.clicked.connect(self.clickMethod)
        #pybutton.resize(200,64)

        #pybutton.move(50, 50)
        """



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    #app = QApplication(sys.argv)
    mainWin = MainWindow()
    msg = QLabel('<h1>hello</h1>', parent=mainWin)
    mainWin.show()
    sys.exit(app.exec())