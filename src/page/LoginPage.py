from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QWidget
from setting import WIDTH, HEIGHT


class LoginPage(QWidget):
    switch_window_to_main = QtCore.pyqtSignal()

    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("Login Page")
        self.resize(WIDTH, HEIGHT)
        layout = QtWidgets.QGridLayout()

        self.login_button = QtWidgets.QPushButton("Login")
        self.login_button.clicked.connect(self.swtich_login_page)

        layout.addWidget(self.login_button)

        self.setLayout(layout)

    def swtich_login_page(self):
        self.switch_window_to_main.emit()
