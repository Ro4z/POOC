from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QWidget
from setting import WIDTH, HEIGHT


class ResultPage(QWidget):
    switch_window_to_main = QtCore.pyqtSignal()

    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("Result Page")
        self.resize(WIDTH, HEIGHT)
        layout = QtWidgets.QGridLayout()

        self.start_button = QtWidgets.QPushButton("GO MAIN PAGE")
        self.start_button.clicked.connect(self.switch_main_page)

        layout.addWidget(self.start_button)

        self.setLayout(layout)

    def switch_main_page(self):
        self.switch_window_to_main.emit()