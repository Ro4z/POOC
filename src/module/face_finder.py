import dlib
import os
from PyQt5.QtCore import QThread
import face_recognition as fr
import numpy as np


class FaceFinder(QThread):
    path = os.path.dirname(os.path.abspath(__file__))
    image1 = fr.load_image_file(os.path.join(path, 'data/inseong.jpeg'))
    face_encoding1 = fr.face_encodings(image1)[0]

    image2 = fr.load_image_file(os.path.join(path, 'data/jimin.jpeg'))
    face_encoding2 = fr.face_encodings(image2)[0]

    known_face_encodings = [face_encoding1, face_encoding2]
    known_face_names = ["Inseong", "Jimin"]

    def find_face(self, image):
        rgb_frame = image[:, :, ::-1]
        face_locations = fr.face_locations(rgb_frame)
        face_encodings = fr.face_encodings(rgb_frame, face_locations)
        name = "Unknown"
        for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
            matches = fr.compare_faces(self.known_face_encodings, face_encoding)
            face_distances = fr.face_distance(self.known_face_encodings, face_encoding)

            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                name = self.known_face_names[best_match_index]

        return name
