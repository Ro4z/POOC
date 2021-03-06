from PySide2.QtCore import QTimer
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout
import cv2 # OpenCV
import qimage2ndarray # for a memory leak,see gist
from setting import WIDTH, HEIGHT
import os
from src.module.face_finder import FaceFinder


class PreViewPage(QWidget):
    switch_window_to_notice = QtCore.pyqtSignal()
    switch_window_to_main = QtCore.pyqtSignal()

    cap = cv2.VideoCapture(0)
    label = None
    timer = QTimer()

    def displayFrame(self):
        ret, frame = self.cap.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        image = qimage2ndarray.array2qimage(frame)
        self.webcam.setPixmap(QPixmap(image))
        self.webcam.setScaledContents(True)

    def start_timer(self):
        self.timer.timeout.connect(self.displayFrame)
        self.timer.start(60)

    def stop_timer(self):
        self.timer.stop()

    def setupUi(self, PreviewForm):
        path = os.path.dirname(os.path.abspath(__file__))
        self.resize(WIDTH, HEIGHT)
        # self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 40)
        # self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 30)

        # self.label = QLabel('No Camera Feed')
        # layout = QVBoxLayout()
        # layout.addWidget(self.label)
        # PreviewForm.setLayout(layout)

        self.webcam = QtWidgets.QLabel(PreviewForm)
        self.webcam.setGeometry(QtCore.QRect(225, 120, 350, 221))
        self.webcam.setStyleSheet("background-color:rgb(255, 255, 127)")

        self.startBtn = QtWidgets.QPushButton(PreviewForm)
        self.startBtn.setGeometry(QtCore.QRect(325, 490, 150, 41))
        self.startBtn.setStyleSheet("background-color : rgb(0, 123, 255);\n"
"border-style:outset;\n"
"border-radius: 10px;\n"
"color: rgb(255, 255, 255);\n"
"font: bold 10pt \"Hancom Gothic\";\n"
"\n"
"\n"
"")
        self.startBtn.clicked.connect(self.switch_notice_page)

        self.back = QtWidgets.QLabel(PreviewForm)
        self.back.setGeometry(QtCore.QRect(0, 0, 800, 600))
        self.back.setPixmap(QtGui.QPixmap(os.path.join(path, 'Img/preview.jpg')))
        self.back.setScaledContents(True)

        self.text = QtWidgets.QTextBrowser(PreviewForm)
        self.text.setGeometry(QtCore.QRect(180, 390, 440, 160))
        self.text.setStyleSheet("background-color:rgb(255, 255, 255);\n"
"border : 0;\n"
"border-radius:10px;")

        self.backArrow = QtWidgets.QPushButton(PreviewForm)
        self.backArrow.setGeometry(QtCore.QRect(740, 10, 50, 50))

        self.backArrow.setStyleSheet("background-color : rgb(0, 123, 255);\n"
                                     "border-style:outset;\n"
                                     "border-radius: 10px;")
        self.backArrow.setIcon(QtGui.QIcon(os.path.join(path, 'Img/back_arrow.png')))
        self.backArrow.clicked.connect(self.switch_login_page)

        self.back.raise_()
        self.text.raise_()
        self.startBtn.raise_()
        self.backArrow.raise_()
        self.webcam.raise_()

        self.retranslateUi(PreviewForm)
        QtCore.QMetaObject.connectSlotsByName(PreviewForm)

    def retranslateUi(self, PreviewForm):
        _translate = QtCore.QCoreApplication.translate
        PreviewForm.setWindowTitle(_translate("PreviewForm", "Preview Page"))
        self.startBtn.setWhatsThis(_translate("PreviewForm", "\n"
"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'HY견고딕\'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1 2 1 9 1 2 3 4</p></body></html>"))
        self.startBtn.setText(_translate("PreviewForm", "시험 시작"))
        self.text.setHtml(_translate("PreviewForm", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  </p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:10px; margin-left:10px; margin-right:10px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Hancom Gothic\'; font-size:12pt; font-weight:792;\">웹캠을 점검하시고 시험 준비가 완료되었다면 </span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Hancom Gothic\'; font-size:12pt; font-weight:792;\">아래의 \'시험 시작\' 버튼을 클릭하여 주십시오.</span></p></body></html>"))


    def switch_notice_page(self):
        self.switch_window_to_notice.emit()

    def switch_login_page(self):
        self.switch_window_to_main.emit()
