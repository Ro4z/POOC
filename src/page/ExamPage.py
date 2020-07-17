from PySide2.QtCore import *
from PySide2.QtGui import *
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QPixmap
from setting import CAM_WIDTH, CAM_HEIGHT
import cv2
import qimage2ndarray
from src.module.gaze_detector import GazeDetector
from src.module.recode_cam import RecodeCam

class ExamPage(QWidget):
    switch_window_to_result = QtCore.pyqtSignal()

    cap = cv2.VideoCapture(0)
    label = None
    timer = QTimer()
    gazeDetector = GazeDetector()
    recodeCam = RecodeCam()

    def displayFrame(self):
        ret, frame = self.cap.read()
        self.recodeCam.recode_cam(frame)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        image = qimage2ndarray.array2qimage(frame)
        self.webcam.setPixmap(QPixmap(image))
        self.webcam.setScaledContents(True)
        self.gazeDetector.detect_gaze(frame)

    def start_timer(self):
        self.timer.timeout.connect(self.displayFrame)
        self.timer.start(60)

    def stop_timer(self):
        self.timer.stop()

    def setupUi(self, ExamForm):
        self.resize(CAM_WIDTH, CAM_HEIGHT)
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 40)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 30)


        self.endBtn = QtWidgets.QPushButton(ExamForm)
        self.endBtn.setGeometry(QtCore.QRect(270, 250, 121, 41))
        self.endBtn.setStyleSheet("background-color : rgb(0, 123, 255);\n"
"border-style:outset;\n"
"border-radius: 10px;\n"
"color: rgb(255, 255, 255);\n"
"font: bold 10pt \"Hancom Gothic\";\n"
"\n"
"")
        self.endBtn.clicked.connect(self.switch_result_page)

        self.webcam = QtWidgets.QLabel(ExamForm)
        self.webcam.setGeometry(QtCore.QRect(0, 0, 400, 300))
        self.webcam.setStyleSheet("background-color:rgb(255, 255, 255)")

        self.webcam.raise_()
        self.endBtn.raise_()

        self.retranslateUi(ExamForm)
        QtCore.QMetaObject.connectSlotsByName(ExamForm)

    def retranslateUi(self, ExamForm):
        _translate = QtCore.QCoreApplication.translate
        ExamForm.setWindowTitle(_translate("ExamForm", "Exam Page"))
        self.endBtn.setText(_translate("ExamForm", "시험 종료"))

    def switch_result_page(self):
        self.switch_window_to_result.emit()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ExamForm = QtWidgets.QWidget()
    ui = ExamPage()
    ui.setupUi(ExamForm)
    ExamForm.show()
    sys.exit(app.exec_())

