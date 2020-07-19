from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget
from setting import WIDTH, HEIGHT
import os

class NoticePage(QWidget):
    switch_window_to_iden = QtCore.pyqtSignal()

    def setupUi(self, NoticeForm):
        path = os.path.dirname(os.path.abspath(__file__))
        self.resize(WIDTH, HEIGHT)

        self.back = QtWidgets.QLabel(NoticeForm)
        self.back.setGeometry(QtCore.QRect(0, 0, 800, 600))
        self.back.setPixmap(QtGui.QPixmap(os.path.join(path, 'Img/preview.jpg')))
        self.back.setScaledContents(True)


        self.startBtn = QtWidgets.QPushButton(NoticeForm)
        self.startBtn.setGeometry(QtCore.QRect(630, 540, 150, 41))
        self.startBtn.setStyleSheet("background-color : rgb(0, 123, 255);\n"
"border-style:outset;\n"
"border-radius: 10px;\n"
"color: rgb(255, 255, 255);\n"
"font: bold 10pt \"Hancom Gothic\";\n"
"\n"
"\n")

        self.startBtn.clicked.connect(self.switch_iden_page)

        self.text = QtWidgets.QLabel(NoticeForm)
        self.text.setGeometry(QtCore.QRect(60, 115, 680, 370))
        self.text.setStyleSheet("font: 20pt \"HY견고딕\";\n"
                                "background-color:rgb(255, 255, 255);\n"
                                "line-height:10;\n"
                                "border-radius:10px;")

        self.back.raise_()
        self.startBtn.raise_()
        self.text.raise_()



        self.retranslateUi(NoticeForm)
        QtCore.QMetaObject.connectSlotsByName(NoticeForm)




    def retranslateUi(self, NoticeForm):
        _translate = QtCore.QCoreApplication.translate
        NoticeForm.setWindowTitle(_translate("NoticeForm", "Notice Page"))
        self.startBtn.setWhatsThis(_translate("NoticeForm", "\n"
"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'HY견고딕\'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1 2 1 9 1 2 3 4</p></body></html>"))
        self.startBtn.setText(_translate("NoticeForm", "시험 시작"))
        self.text.setText(_translate("NoticeForm", "  지금부터 사용자의 모습과 노트북 화면이 녹화됩니다. \n"
                                                   "\n"
                                                   "  부정행위가 5회 이상 감지될 경우, 감독관의 요청에 따라야 합니다. \n"
                                                   "\n"
                                                   "\n"
                                                   "\n"
                                                   "  부정 행위 판단 기준은 다음과 같습니다.\n"
                                                   "\n"
                                                   "  첫째. alt, window, control key등의 특수키를 눌렀을 경우\n"
                                                   "\n"
                                                   "  둘째. 눈이 노트북화면을 향하지 않고 왼쪽, 오른쪽을 향하는 경우\n"
                                                   "\n"
                                                   "  셋째. 사용자를 제외한 다른 사람이 인식될 경우"))

    def switch_iden_page(self):
        self.switch_window_to_iden.emit()
