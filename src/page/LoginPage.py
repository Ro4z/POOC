from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget
from setting import WIDTH, HEIGHT
import os
from PyQt5.QtGui import QIcon, QPixmap


class LoginPage(QWidget):
    switch_window_to_main = QtCore.pyqtSignal()

    def setupUi(self, LoginForm):
        path = os.path.dirname(os.path.abspath(__file__))
        self.resize(WIDTH, HEIGHT)
        self.back_1 = QtWidgets.QLabel(LoginForm)
        self.back_1.setGeometry(QtCore.QRect(0, 0, 300, 600))
        self.back_1.setStyleSheet("background-color:rgb(255, 255, 255);")

        self.back_2 = QtWidgets.QLabel(LoginForm)
        self.back_2.setGeometry(QtCore.QRect(299, 0, 501, 600))
        self.back_2.setToolTip("")
        self.back_2.setPixmap(QtGui.QPixmap(os.path.join(path, 'Img/login.png')))
        self.back_2.setScaledContents(True)

        self.loginBtn = QtWidgets.QPushButton(LoginForm)
        self.loginBtn.setGeometry(QtCore.QRect(45, 410, 210, 40))
        self.loginBtn.setStyleSheet("background-color : rgb(0, 123, 255);\n"
"border-style:outset;\n"
"border-radius: 10px;\n"
"color: rgb(255, 255, 255);\n"
"font: bold 10pt \"Hancom Gothic\";\n"
"\n")
        self.loginBtn.clicked.connect(self.swtich_login_page)

        self.ID = QtWidgets.QLineEdit(LoginForm)
        self.ID.setGeometry(QtCore.QRect(45, 270, 210, 40))
        self.ID.setStyleSheet("border-color:rgb(0, 183, 206);\n")

        self.PWD = QtWidgets.QLineEdit(LoginForm)
        self.PWD.setEchoMode(QtWidgets.QLineEdit.Password)
        self.PWD.setGeometry(QtCore.QRect(45, 340, 210, 40))

        self.label_3 = QtWidgets.QLabel(LoginForm)
        self.label_3.setGeometry(QtCore.QRect(25, 40, 250, 220))
        self.label_3.setPixmap(QtGui.QPixmap(os.path.join(path, 'Img/logo.png')))
        self.label_3.setScaledContents(True)


        self.stId = QtWidgets.QLabel(LoginForm)
        self.stId.setGeometry(QtCore.QRect(50, 250, 64, 21))
        self.stId.setStyleSheet("font: bold 8pt \"Hancom Gothic\";")


        self.stPwd = QtWidgets.QLabel(LoginForm)
        self.stPwd.setGeometry(QtCore.QRect(50, 320, 64, 21))
        self.stPwd.setStyleSheet("font: bold 8pt \"Hancom Gothic\";")


        self.back_1.raise_()
        self.PWD.raise_()
        self.loginBtn.raise_()
        self.back_2.raise_()
        self.ID.raise_()
        self.label_3.raise_()
        self.label_3.show()
        self.stId.raise_()
        self.stPwd.raise_()

        self.retranslateUi(LoginForm)
        QtCore.QMetaObject.connectSlotsByName(LoginForm)

    def retranslateUi(self, LoginForm):
        _translate = QtCore.QCoreApplication.translate
        LoginForm.setWindowTitle(_translate("LoginForm", "Login Page"))
        self.loginBtn.setText(_translate("LoginForm", "Login"))
        self.stId.setText(_translate("LoginForm", "학번"))
        self.stPwd.setText(_translate("LoginForm", "비밀번호"))

    def swtich_login_page(self):
        self.switch_window_to_main.emit()