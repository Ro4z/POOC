from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget
from setting import WIDTH, HEIGHT

check = False

class IdenPage(QWidget):
    switch_window_to_exam = QtCore.pyqtSignal()

    def setupUi(self, IdenForm):
        self.resize(WIDTH, HEIGHT)

        self.text = QtWidgets.QLabel(IdenForm)
        self.text.setGeometry(QtCore.QRect(0, 0, 800, 70))
        self.text.setStyleSheet("background-color:rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"font: bold 12pt \"Hancom Gothic\";\n"
"\n")

        self.webcam = QtWidgets.QLabel(IdenForm)
        self.webcam.setGeometry(QtCore.QRect(0, 70, 800, 530))
        self.webcam.setStyleSheet("background-color:rgb(255, 217, 178);\n")

        self.startBtn = QtWidgets.QPushButton(IdenForm)
        self.startBtn.setGeometry(QtCore.QRect(630, 540, 150, 40))
        self.startBtn.setStyleSheet("background-color : rgb(0, 123, 255);\n"
"border-style:outset;\n"
"border-radius: 10px;\n"
"color: rgb(255, 255, 255);\n"''
"font: bold 10pt \"Hancom Gothic\";\n"
"\n"
"\n"
"")
        self.startBtn.clicked.connect(self.switch_exam_page)

        self.webcam.raise_()
        self.text.raise_()
        self.startBtn.raise_()

        if check:
            self.startBtn.raise_()

        self.retranslateUi(IdenForm)
        QtCore.QMetaObject.connectSlotsByName(IdenForm)

    def retranslateUi(self, IdenForm):
        _translate = QtCore.QCoreApplication.translate
        IdenForm.setWindowTitle(_translate("IdenForm", "Form"))
        self.text.setText(_translate("IdenForm", "                                        사용자 본인 확인을 위해 정면을 응시하여 주십시오."))
        self.startBtn.setWhatsThis(_translate("IdenForm", "\n"
"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'HY견고딕\'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1 2 1 9 1 2 3 4</p></body></html>"))
        self.startBtn.setText(_translate("IdenForm", "시험 시작"))

    def switch_exam_page(self):
        self.switch_window_to_exam.emit()