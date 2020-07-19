#detect keyboard press
import sys
import keyboard
import time
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QLabel, QGridLayout, QWidget, QApplication
from PyQt5.QtCore import QSize

list=[]

class MainWindow(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        self.setMinimumSize(QSize(300, 200))
        self.setGeometry(100,100,200,80)
        self.setWindowTitle("PyQt messagebox example")


        while True:
            if keyboard.is_pressed('ctrl'):
                str = "Press Ctrl Key"
                print(str)
                list.append(str)
                time.sleep(1)

            elif keyboard.is_pressed('alt'):
                str = "Press Alt Key"
                print(str)
                list.append(str)
                time.sleep(1)


            elif keyboard.is_pressed('win'):
                str = "Press Window Key"
                print(str)
                list.append(str)
                time.sleep(1)

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
    mainWin.show()
    sys.exit(app.exec())