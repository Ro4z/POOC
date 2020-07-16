from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget
from setting import WIDTH, HEIGHT

class ResultPage(QWidget):
    switch_window_to_main = QtCore.pyqtSignal()

    def setupUi(self, ResultForm):
        self.resize(WIDTH, HEIGHT)

        self.back_2 = QtWidgets.QLabel(ResultForm)
        self.back_2.setGeometry(QtCore.QRect(0, 0, 800, 600))
        self.back_2.setPixmap(QtGui.QPixmap("그림2.jpg"))
        self.back_2.setScaledContents(True)

        self.text = QtWidgets.QTextBrowser(ResultForm)
        self.text.setGeometry(QtCore.QRect(180, 240, 440, 160))
        self.text.setStyleSheet("background-color:rgb(255, 255, 255);\n"
"border : 0;\n"
"border-radius:10px;")

        self.mainBtn = QtWidgets.QPushButton(ResultForm)
        self.mainBtn.setGeometry(QtCore.QRect(325, 340, 150, 41))
        self.mainBtn.setStyleSheet("background-color : rgb(0, 123, 255);\n"
"border-style:outset;\n"
"border-radius: 10px;\n"
"color: rgb(255, 255, 255);\n"
"font: bold 10pt \"Hancom Gothic\";\n"
"\n"
"\n"
"")
        self.mainBtn.clicked.connect(self.switch_main_page)

        self.retranslateUi(ResultForm)
        QtCore.QMetaObject.connectSlotsByName(ResultForm)

    def retranslateUi(self, ResultForm):
        _translate = QtCore.QCoreApplication.translate
        ResultForm.setWindowTitle(_translate("ResultForm", "Result Page"))
        self.text.setHtml(_translate("ResultForm", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  </p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:10px; margin-left:10px; margin-right:10px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Hancom Gothic\'; font-size:12pt; font-weight:792;\">시험이 종료되었습니다. </span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Hancom Gothic\'; font-size:12pt; font-weight:792;\">수고하셨습니다.</span></p></body></html>"))
        self.mainBtn.setWhatsThis(_translate("ResultForm", "\n"
"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'HY견고딕\'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1 2 1 9 1 2 3 4</p></body></html>"))
        self.mainBtn.setText(_translate("ResultForm", "메인화면"))

    def switch_main_page(self):
        self.switch_window_to_main.emit()
"""
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ResultForm = QtWidgets.QWidget()
    ui = Ui_ResultForm()
    ui.setupUi(ResultForm)
    ResultForm.show()
    sys.exit(app.exec_())
    """
