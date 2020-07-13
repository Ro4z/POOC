import cv2
import dlib
from PyQt5 import QtCore
from PyQt5 import QtWidgets
from PyQt5 import QtGui
from track_gaze import get_gaze_ratio

import numpy as np
import face_recognition as fr

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


class ShowVideo(QtCore.QObject):
    flag = 0

    camera = cv2.VideoCapture(0)

    ret, image = camera.read()
    height, width = image.shape[:2]

    VideoSignal1 = QtCore.pyqtSignal(QtGui.QImage)
    VideoSignal2 = QtCore.pyqtSignal(QtGui.QImage)

    run_video = True

    def __init__(self, parent=None):
        super(ShowVideo, self).__init__(parent)

    @QtCore.pyqtSlot()
    def start_video(self):

        global image
        # set detector
        detector = dlib.get_frontal_face_detector()
        # set predictor
        predictor = dlib.shape_predictor("shape_68.dat")

        my_image = fr.load_image_file("inseong.jpeg")
        my_face_encoding = fr.face_encodings(my_image)[0]

        known_face_encodings = [my_face_encoding]
        known_face_names = ["Inseong"]

        while self.run_video:
            ret, image = self.camera.read()
            # face finder
            rgb_frame = image[:, :, ::-1]
            face_locations = fr.face_locations(rgb_frame)
            face_encodings = fr.face_encodings(rgb_frame, face_locations)
            for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
                matches = fr.compare_faces(known_face_encodings, face_encoding)

                name = "Unknown"

                face_distances = fr.face_distance(known_face_encodings, face_encoding)

                best_match_index = np.argmin(face_distances)
                if matches[best_match_index]:
                    name = known_face_names[best_match_index]

                cv2.rectangle(image, (left, top), (right, bottom), (0, 0, 255), 2)

                cv2.rectangle(image, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)

                font = cv2.FONT_HERSHEY_SIMPLEX
                cv2.putText(image, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

            cv2.imshow('Webcam_facerecognition', image)
            # end of face finder
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            color_swapped_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            # face detector
            faces = detector(gray)
            for face in faces:

                landmarks = predictor(gray, face)
                gaze_ratio_left_eye = get_gaze_ratio([36, 37, 38, 39, 40, 41], landmarks, image, gray)
                gaze_ratio_right_eye = get_gaze_ratio([42, 43, 44, 45, 46, 47], landmarks, image, gray)
                gaze_ratio = (gaze_ratio_right_eye + gaze_ratio_left_eye) / 2
                print(gaze_ratio)
                if gaze_ratio <= 0.8:
                    print('right')
                elif gaze_ratio <= 3:
                    print('center')
                else:
                    print('left')
            #########################

            qt_image1 = QtGui.QImage(color_swapped_image.data,
                                     self.width,
                                     self.height,
                                     color_swapped_image.strides[0],
                                     QtGui.QImage.Format_RGB888)
            self.VideoSignal1.emit(qt_image1)

            if self.flag:
                img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
                img_canny = cv2.Canny(img_gray, 50, 100)

                qt_image2 = QtGui.QImage(img_canny.data,
                                         self.width,
                                         self.height,
                                         img_canny.strides[0],
                                         QtGui.QImage.Format_Grayscale8)

                self.VideoSignal2.emit(qt_image2)

            loop = QtCore.QEventLoop()
            QtCore.QTimer.singleShot(25, loop.quit)  # 25 ms
            loop.exec_()

    @QtCore.pyqtSlot()
    def canny(self):
        self.flag = 1 - self.flag

    def exit(self):
        self.run_video = False
        QtCore.QCoreApplication.instance().quit()