from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QWidget
from setting import WIDTH, HEIGHT


class LogPage(QWidget):
    switch_window = QtCore.pyqtSignal()

    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("Log Page")
        self.resize(WIDTH, HEIGHT)
