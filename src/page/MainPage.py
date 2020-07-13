import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QWidget

class MainPage(QWidget):
    switch_window_to_log = QtCore.pyqtSignal()
    switch_window_to_preview = QtCore.pyqtSignal()
    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("Main Page")
        self.resize(600, 480)

        layout = QtWidgets.QGridLayout()

        self.log_button = QtWidgets.QPushButton("go log")
        self.log_button.clicked.connect(self.switch_log_page)
        layout.addWidget(self.log_button)

        self.preview_button = QtWidgets.QPushButton("go preview")
        self.preview_button.clicked.connect(self.switch_window_to_preview)
        layout.addWidget(self.preview_button)

        self.setLayout(layout)

    def switch_log_page(self):
        self.switch_window_to_log.emit()

    def switch_preview_page(self):
        self.switch_window_to_preview.emit()