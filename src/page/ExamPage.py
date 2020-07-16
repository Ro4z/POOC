from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QWidget
from setting import CAM_WIDTH, CAM_HEIGHT

class ExamPage(QWidget):
    switch_window_to_result = QtCore.pyqtSignal()

    def setupUi(self, ExamForm):
        self.resize(CAM_WIDTH, CAM_HEIGHT)

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

