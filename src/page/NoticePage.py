from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QWidget
from setting import WIDTH, HEIGHT


class NoticePage(QWidget):
    switch_window_to_exam = QtCore.pyqtSignal()

    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("Notice Page")
        self.resize(WIDTH, HEIGHT)
        layout = QtWidgets.QGridLayout()

        self.start_button = QtWidgets.QPushButton("START EXAM")
        self.start_button.clicked.connect(self.switch_exam_page)

        layout.addWidget(self.start_button)

        self.setLayout(layout)

    def switch_exam_page(self):
        self.switch_window_to_exam.emit()