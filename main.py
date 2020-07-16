import sys
from PyQt5 import QtCore, QtWidgets
from src.controller import Controller

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    controller = Controller()
    controller.show_login_page()
    sys.exit(app.exec_())