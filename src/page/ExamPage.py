import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QWidget

class ExamPage(QWidget):
    switch_window_to_result = QtCore.pyqtSignal()

    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("Exam Page")
        self.resize(600,480)
        layout = QtWidgets.QGridLayout()

        self.start_button = QtWidgets.QPushButton("GO RESULT PAGE")
        self.start_button.clicked.connect(self.switch_result_page)

        layout.addWidget(self.start_button)

        self.setLayout(layout)

    def switch_result_page(self):
        self.switch_window_to_result.emit()