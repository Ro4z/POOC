from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget
from setting import WIDTH, HEIGHT


class NoticePage(QWidget):
    switch_window_to_exam = QtCore.pyqtSignal()

    def setupUi(self, NoticeForm):
        self.resize(WIDTH, HEIGHT)

        self.back = QtWidgets.QLabel(NoticeForm)
        self.back.setGeometry(QtCore.QRect(0, 0, 800, 600))
        self.back.setPixmap(QtGui.QPixmap("그림2.jpg"))
        self.back.setScaledContents(True)

        self.innerSQ = QtWidgets.QLabel(NoticeForm)
        self.innerSQ.setGeometry(QtCore.QRect(350, 250, 100, 100))
        self.innerSQ.setStyleSheet("border-radius : 30%;\n"
"background-color:rgb(255, 255, 255)")

        self.outerSQ = QtWidgets.QLabel(NoticeForm)
        self.outerSQ.setGeometry(QtCore.QRect(300, 200, 200, 200))
        self.outerSQ.setStyleSheet("border-radius : 70%;\n"
"background-color:rgb(38, 55, 71);")

        self.startBtn = QtWidgets.QPushButton(NoticeForm)
        self.startBtn.setGeometry(QtCore.QRect(630, 540, 150, 41))
        self.startBtn.setStyleSheet("background-color : rgb(0, 123, 255);\n"
"border-style:outset;\n"
"border-radius: 10px;\n"
"color: rgb(255, 255, 255);\n"
"font: bold 10pt \"Hancom Gothic\";\n"
"\n"
"\n")

        self.startBtn.clicked.connect(self.switch_exam_page)

        self.text = QtWidgets.QLabel(NoticeForm)
        self.text.setGeometry(QtCore.QRect(155, 100, 490, 81))
        self.text.setStyleSheet("font: 13pt \"HY견고딕\";\n"
"")

        self.back.raise_()
        self.outerSQ.raise_()
        self.innerSQ.raise_()
        self.startBtn.raise_()
        self.text.raise_()

        self.retranslateUi(NoticeForm)
        QtCore.QMetaObject.connectSlotsByName(NoticeForm)

    def retranslateUi(self, NoticeForm):
        _translate = QtCore.QCoreApplication.translate
        NoticeForm.setWindowTitle(_translate("NoticeForm", "Form"))
        self.startBtn.setWhatsThis(_translate("NoticeForm", "\n"
"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'HY견고딕\'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1 2 1 9 1 2 3 4</p></body></html>"))
        self.startBtn.setText(_translate("NoticeForm", "시험 시작"))
        self.text.setText(_translate("NoticeForm", "주의사항을 듣고 \'시험 시작\'버튼을 클릭하십시오."))


    def switch_exam_page(self):
        self.switch_window_to_exam.emit()

