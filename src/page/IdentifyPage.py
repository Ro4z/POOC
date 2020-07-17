from PySide2.QtCore import QTimer
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QPixmap
from setting import WIDTH, HEIGHT
from src.module.face_finder import FaceFinder
import cv2
import qimage2ndarray




class IdenPage(QWidget):
    switch_window_to_exam = QtCore.pyqtSignal()
    correct_num = 0
    user_name = "Inseong"
    cap = cv2.VideoCapture(0)
    label = None
    timer = QTimer()
    thread = FaceFinder()
    check = False

    def displayFrame(self):
        ret, frame = self.cap.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        image = qimage2ndarray.array2qimage(frame)
        self.webcam.setPixmap(QPixmap(image))
        self.webcam.setScaledContents(True)
        find_name = self.thread.find_face(frame)
        print(find_name)
        if find_name == self.user_name:
            self.correct_num += 1

        if self.correct_num == 7:
            self.startBtn.raise_()

    def start_timer(self):
        self.timer.timeout.connect(self.displayFrame)
        self.timer.start(60)

    def stop_timer(self):
        self.timer.stop()

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