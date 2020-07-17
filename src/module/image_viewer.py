from PyQt5 import QtCore
from PyQt5 import QtWidgets
from PyQt5 import QtGui

class ImageViewer(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(ImageViewer, self).__init__(parent)
        self.image = QtGui.QImage()
        self.setAttribute(QtCore.Qt.WA_OpaquePaintEvent)

    def paintEvent(self, event):
        painter = QtGui.QPainter(self)
        painter.drawImage(0, 0, self.image)
        self.image = QtGui.QImage()

    def init_ui(self):
        self.setWindowTitle('Test')

    @QtCore.pyqtSlot(QtGui.QImage)
    def set_image(self, _image):
        if _image.isNull():
            print("Viewer Dropped frame!")

        self.image = _image
        if _image.size() != self.size():
            self.setFixedSize(_image.size())
        self.update()