import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QWidget

class PreViewPage(QWidget):
    switch_window_to_notice = QtCore.pyqtSignal()

    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("Preview Page")
        self.resize(600,480)
        layout = QtWidgets.QGridLayout()

        self.start_button = QtWidgets.QPushButton("START EXAM")
        self.start_button.clicked.connect(self.switch_notice_page)

        layout.addWidget(self.start_button)

        self.setLayout(layout)

    def switch_notice_page(self):
        self.switch_window_to_notice.emit()