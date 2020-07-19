from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget
from setting import WIDTH, HEIGHT
from src.page.ExamPage import log_list

list = [["2020-07-19(21:26:43)","out of visual range(right)"],["2020-07-19(21:26:50)","out of visual range(left)"],["2020-07-19(21:27:03)","press Alt key"]]

class LogPage(QWidget):
    switch_window = QtCore.pyqtSignal()
    switch_window_to_main = QtCore.pyqtSignal()

    def setupUi(self, LogForm):
        self.resize(WIDTH, HEIGHT)
        self.back_1 = QtWidgets.QLabel(LogForm)
        self.back_1.setGeometry(QtCore.QRect(0, 0, 300, 611))
        self.back_1.setStyleSheet("border:5px;\n"
"background-color:rgb(38, 55, 71)\n"
"")

        self.logList = QtWidgets.QTextBrowser(LogForm)
        self.logList.setGeometry(QtCore.QRect(300, 0, 500, 600))
        self.logList.clear()
        self.logList.setStyleSheet("border:0; font: 12pt \"Hancom Gothic\";")
        self.logList.setText("\n\n")
        #self.set_log_text()

        self.backArrow = QtWidgets.QPushButton(LogForm)
        self.backArrow.setGeometry(QtCore.QRect(740, 10, 50, 50))
        self.backArrow.setStyleSheet("background-color : rgb(0, 123, 255);\n"
                                     "border-style:outset;\n"
                                     "border-radius: 10px;")
        self.backArrow.setIcon(QtGui.QIcon("/Users/ewqaz/Desktop/UI/back-arrow.png"))
        self.backArrow.clicked.connect(self.swtich_login_page)

        self.class_1 = QtWidgets.QPushButton(LogForm)
        self.class_1.setGeometry(QtCore.QRect(30, 60, 251, 71))
        self.class_1.setStyleSheet("background-color :rgb(38, 55, 71);\n"
"border-style:outset;\n"
"border-width:5px;\n"
"border-color:rgb(38, 55, 71);\n"
"border-radius: 10px;\n"
"color:rgb(255, 255, 255);\n"
"font: bold 12pt \"Hancom Gothic\";\n"
"")

        self.class_1.clicked.connect(self.set_log_text)

        self.class_2 = QtWidgets.QPushButton(LogForm)
        self.class_2.setGeometry(QtCore.QRect(30, 160, 251, 71))
        self.class_2.setStyleSheet("background-color :rgb(38, 55, 71);\n"
"border-style:outset;\n"
"border-width:5px;\n"
"border-color:rgb(38, 55, 71);\n"
"border-radius: 10px;\n"
"color:rgb(255, 255, 255);\n"
"font: bold 12pt \"Hancom Gothic\";\n"
"")

        self.class_2.clicked.connect(self.set_log_text2)
        self.class_3 = QtWidgets.QPushButton(LogForm)
        self.class_3.setGeometry(QtCore.QRect(30, 260, 251, 71))
        self.class_3.setStyleSheet("background-color :rgb(38, 55, 71);\n"
"border-style:outset;\n"
"border-width:5px;\n"
"border-color:rgb(38, 55, 71);\n"
"border-radius: 10px;\n"
"color:rgb(255, 255, 255);\n"
"font: bold 12pt \"Hancom Gothic\";\n"
"")

        self.class_4 = QtWidgets.QPushButton(LogForm)
        self.class_4.setGeometry(QtCore.QRect(30, 360, 251, 71))
        self.class_4.setStyleSheet("background-color :rgb(38, 55, 71);\n"
"border-style:outset;\n"
"border-width:5px;\n"
"border-color:rgb(38, 55, 71);\n"
"border-radius: 10px;\n"
"color:rgb(255, 255, 255);\n"
"font: bold 12pt \"Hancom Gothic\";\n"
"")

        self.class_5 = QtWidgets.QPushButton(LogForm)
        self.class_5.setGeometry(QtCore.QRect(30, 460, 251, 71))
        self.class_5.setStyleSheet("background-color :rgb(38, 55, 71);\n"
"border-style:outset;\n"
"border-width:5px;\n"
"border-color:rgb(38, 55, 71);\n"
"border-radius: 10px;\n"
"color:rgb(255, 255, 255);\n"
"font: bold 12pt \"Hancom Gothic\";\n"
"")


        self.label_1 = QtWidgets.QLabel(LogForm)
        self.label_1.setGeometry(QtCore.QRect(50, 115, 221, 5))
        self.label_1.setStyleSheet("background-color:rgb(255, 181, 53);")

        self.label_2 = QtWidgets.QLabel(LogForm)
        self.label_2.setGeometry(QtCore.QRect(50, 215, 221, 5))
        self.label_2.setStyleSheet("background-color:rgb(239, 9, 70)")

        self.label_3 = QtWidgets.QLabel(LogForm)
        self.label_3.setGeometry(QtCore.QRect(50, 315, 221, 5))
        self.label_3.setStyleSheet("background-color:rgb(122, 255, 51);")

        self.label_4 = QtWidgets.QLabel(LogForm)
        self.label_4.setGeometry(QtCore.QRect(50, 415, 221, 5))
        self.label_4.setStyleSheet("background-color:rgb(127, 42, 231);")

        self.label_5 = QtWidgets.QLabel(LogForm)
        self.label_5.setGeometry(QtCore.QRect(50, 515, 221, 5))
        self.label_5.setStyleSheet("background-color:rgb(255, 241, 38)")


        self.retranslateUi(LogForm)
        QtCore.QMetaObject.connectSlotsByName(LogForm)

    def retranslateUi(self, LogForm):
        _translate = QtCore.QCoreApplication.translate
        LogForm.setWindowTitle(_translate("LogForm", "Log Page"))
        self.class_1.setText(_translate("LogForm", "  자바 기반 응용 프로그래밍"))
        self.class_2.setText(_translate("LogForm", "인터넷 프로그래밍"))
        self.class_3.setText(_translate("LogForm", "초급 스페인어"))
        self.class_4.setText(_translate("LogForm", "어셈블리어"))
        self.class_5.setText(_translate("LogForm", "댄스스포츠"))

    def swtich_login_page(self):
        self.switch_window_to_main.emit()

    def set_log_text(self):
        for i in range(0,len(list)):
            self.logList.append("  "+list[i][0] + "    "+list[i][1]+"\n")
            #self.logList.append("  "+list[i][0] + "    "+list[i][1]+"\n")

            #print("  "+log_list[i][0] + "    "+log_list[i][1]+"\n")

    def set_log_text2(self):
        self.logList.append("\n\n\n")
