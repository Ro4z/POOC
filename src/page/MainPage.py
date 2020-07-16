from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget
from setting import WIDTH, HEIGHT

class MainPage(QWidget):
    switch_window_to_log = QtCore.pyqtSignal()
    switch_window_to_preview = QtCore.pyqtSignal()
    switch_window_to_login = QtCore.pyqtSignal()

    def setupUi(self, MainForm):
        self.resize(WIDTH, HEIGHT)

        self.back_1 = QtWidgets.QLabel(MainForm)
        self.back_1.setGeometry(QtCore.QRect(0, 0, 300, 611))
        self.back_1.setStyleSheet("border:5px;\n"
"background-color:rgb(38, 55, 71)\n")

        self.back_2 = QtWidgets.QLabel(MainForm)
        self.back_2.setGeometry(QtCore.QRect(300, 0, 500, 600))
        self.back_2.setStyleSheet("background:rgb(255, 255, 255);")

        self.stImg = QtWidgets.QLabel(MainForm)
        self.stImg.setGeometry(QtCore.QRect(40, 120, 220, 190))
        self.stImg.setStyleSheet("border-radius : 30%;")
        self.stImg.setPixmap(QtGui.QPixmap("student.jpg"))
        self.stImg.setScaledContents(True)


        self.stName = QtWidgets.QTextBrowser(MainForm)
        self.stName.setGeometry(QtCore.QRect(90, 390, 141, 41))
        self.stName.setStyleSheet("background-color:rgb(38, 55, 71);\n"
"color:rgb(255, 255, 255);\n"
"font: 14pt \"HY견고딕\";\n"
"border : 0;")


        self.stNum = QtWidgets.QTextBrowser(MainForm)
        self.stNum.setGeometry(QtCore.QRect(60, 340, 221, 41))
        self.stNum.setStyleSheet("background-color:rgb(38, 55, 71);\n"
"color:rgb(255, 255, 255);\n"
"font: 14pt \"HY견고딕\";\n"
"border : 0;")


        self.showLog = QtWidgets.QPushButton(MainForm)
        self.showLog.setGeometry(QtCore.QRect(10, 20, 131, 31))
        self.showLog.setStyleSheet("background-color : rgb(0, 123, 255);\n"
"border-style:outset;\n"
"border-radius: 10px;\n"
"color: rgb(255, 255, 255);\n"
"font: bold 10pt \"Hancom Gothic\";\n"
"\n"
"\n"
"")
        self.showLog.clicked.connect(self.switch_log_page)

        self.logoutBtn = QtWidgets.QPushButton(MainForm)
        self.logoutBtn.setGeometry(QtCore.QRect(85, 430, 130, 30))
        self.logoutBtn.setStyleSheet("background-color : rgb(0, 123, 255);\n"
                                     "border-style:outset;\n"
                                     "border-radius: 10px;\n"
                                     "color: rgb(255, 255, 255);\n"
                                     "font: bold 10pt \"Hancom Gothic\";\n"
                                     "\n"
                                     "\n"
                                     "")
        self.logoutBtn.clicked.connect(self.switch_login_page)


        self.class_1 = QtWidgets.QPushButton(MainForm)
        self.class_1.setGeometry(QtCore.QRect(330, 20, 450, 90))
        self.class_1.setStyleSheet("background-color : rgb(255, 255, 255);\n"
"border-style:outset;\n"
"border-width:5px;\n"
"border-color:rgb(223, 223, 223);\n"
"border-radius: 10px;\n"
"font: bold 12pt \"Hancom Gothic\";\n"
"")
        self.class_1.clicked.connect(self.switch_preview_page)


        self.class_2 = QtWidgets.QPushButton(MainForm)
        self.class_2.setGeometry(QtCore.QRect(330, 130, 450, 90))
        self.class_2.setStyleSheet("background-color : rgb(255, 255, 255);\n"
"border-style:outset;\n"
"border-width:5px;\n"
"border-color:rgb(223, 223, 223);\n"
"border-radius: 10px;\n"
"font: bold 12pt \"Hancom Gothic\";\n"
"")
        self.class_2.clicked.connect(self.switch_preview_page)


        self.class_3 = QtWidgets.QPushButton(MainForm)
        self.class_3.setGeometry(QtCore.QRect(330, 240, 450, 90))
        self.class_3.setStyleSheet("background-color : rgb(255, 255, 255);\n"
"border-style:outset;\n"
"border-width:5px;\n"
"border-color:rgb(223, 223, 223);\n"
"border-radius: 10px;\n"
"font: bold 12pt \"Hancom Gothic\";\n"
"")
        self.class_3.clicked.connect(self.switch_preview_page)

        self.class_4 = QtWidgets.QPushButton(MainForm)
        self.class_4.setGeometry(QtCore.QRect(330, 350, 450, 90))
        self.class_4.setStyleSheet("background-color : rgb(255, 255, 255);\n"
"border-style:outset;\n"
"border-width:5px;\n"
"border-color:rgb(223, 223, 223);\n"
"border-radius: 10px;\n"
"font: bold 12pt \"Hancom Gothic\";\n"
"")
        self.class_4.clicked.connect(self.switch_preview_page)

        self.class_5 = QtWidgets.QPushButton(MainForm)
        self.class_5.setGeometry(QtCore.QRect(330, 460, 450, 90))
        self.class_5.setStyleSheet("background-color : rgb(255, 255, 255);\n"
"border-style:outset;\n"
"border-width:5px;\n"
"border-color:rgb(223, 223, 223);\n"
"border-radius: 10px;\n"
"font: bold 12pt \"Hancom Gothic\";\n"
"")
        self.class_5.clicked.connect(self.switch_preview_page)


        self.label = QtWidgets.QLabel(MainForm)
        self.label.setGeometry(QtCore.QRect(340, 36, 5, 60))
        self.label.setStyleSheet("background-color:rgb(255, 181, 53);")


        self.label_2 = QtWidgets.QLabel(MainForm)
        self.label_2.setGeometry(QtCore.QRect(340, 370, 5, 60))
        self.label_2.setStyleSheet("background-color:rgb(127, 42, 231)")

        self.label_3 = QtWidgets.QLabel(MainForm)
        self.label_3.setGeometry(QtCore.QRect(340, 150, 5, 60))
        self.label_3.setStyleSheet("background-color:rgb(239, 9, 70)")

        self.label_4 = QtWidgets.QLabel(MainForm)
        self.label_4.setGeometry(QtCore.QRect(340, 260, 5, 60))
        self.label_4.setStyleSheet("background-color:rgb(122, 255, 51)")

        self.label_5 = QtWidgets.QLabel(MainForm)
        self.label_5.setGeometry(QtCore.QRect(340, 480, 5, 60))
        self.label_5.setStyleSheet("background-color:rgb(255, 241, 38)")

        self.back_2.raise_()
        self.back_1.raise_()
        self.stImg.raise_()
        self.stNum.raise_()
        self.stName.raise_()
        self.showLog.raise_()
        self.logoutBtn.raise_()
        self.class_1.raise_()
        self.label.raise_()
        self.class_2.raise_()
        self.class_3.raise_()
        self.class_4.raise_()
        self.class_5.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.label_5.raise_()

        self.retranslateUi(MainForm)
        QtCore.QMetaObject.connectSlotsByName(MainForm)

    def retranslateUi(self, MainForm):
        _translate = QtCore.QCoreApplication.translate
        MainForm.setWindowTitle(_translate("MainForm", "Main Page"))
        self.stName.setHtml(_translate("MainForm", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'HY견고딕\'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">김인하  님</p></body></html>"))
        self.stNum.setHtml(_translate("MainForm", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'HY견고딕\'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1 2 1 9 1 2 3 4</p></body></html>"))
        self.showLog.setWhatsThis(_translate("MainForm", "\n"
"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'HY견고딕\'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1 2 1 9 1 2 3 4</p></body></html>"))
        self.showLog.setText(_translate("MainForm", "알림내역 보기"))
        self.logoutBtn.setWhatsThis(_translate("MainForm", "\n"
                                                           "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                           "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                           "p, li { white-space: pre-wrap; }\n"
                                                           "</style></head><body style=\" font-family:\'HY견고딕\'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
                                                           "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1 2 1 9 1 2 3 4</p></body></html>"))
        self.logoutBtn.setText(_translate("MainForm", "Log out"))
        self.class_1.setText(_translate("MainForm", "  자바 기반 응용 프로그래밍  |  A.M. 10:00"))
        self.class_2.setText(_translate("MainForm", "  인터넷 프로그래밍  |  P.M. 6:00"))
        self.class_3.setText(_translate("MainForm", "  초급 스페인어  |  A.M. 9:50"))
        self.class_4.setText(_translate("MainForm", "  어셈블리어  |  A.M. 11:00"))
        self.class_5.setText(_translate("MainForm", "  댄스 스포츠  |  A.M. 10:00"))

    def switch_log_page(self):
        self.switch_window_to_log.emit()

    def switch_preview_page(self):
        self.switch_window_to_preview.emit()

    def switch_login_page(self):
        self.switch_window_to_login.emit()
