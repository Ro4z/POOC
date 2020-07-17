import cv2
from PyQt5 import QtCore
from PyQt5 import QtGui


class ShowWebCam(QtCore.QObject):

    camera = cv2.VideoCapture(0)
    ret, image = camera.read()
    height, width = 480, 600

    VideoSignal1 = QtCore.pyqtSignal(QtGui.QImage)

    run_video = True

    def __init__(self, parent=None):
        super(ShowWebCam, self).__init__(parent)

    @QtCore.pyqtSlot()
    def start_video(self):

        global image

        while self.run_video:
            ret, image = self.camera.read()

            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            color_swapped_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

            qt_image1 = QtGui.QImage(color_swapped_image.data,
                                     self.width,
                                     self.height,
                                     color_swapped_image.strides[0],
                                     QtGui.QImage.Format_RGB888)
            self.VideoSignal1.emit(qt_image1)

            loop = QtCore.QEventLoop()
            QtCore.QTimer.singleShot(25, loop.quit)  # 25 ms
            loop.exec_()