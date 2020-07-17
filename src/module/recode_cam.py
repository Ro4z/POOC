import cv2
from datetime import date

class RecodeCam:
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    today = date.today()
    file_name = today.strftime("%Y-%m-%d_webcam")
    file_name += '.avi'
    out = cv2.VideoWriter("recode/" + file_name, fourcc, 15.0, (640, 480))

    def recode_cam(self, frame):
        self.out.write(frame)