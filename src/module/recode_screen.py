import cv2
import numpy as np
from PIL import ImageGrab
from datetime import date


class RecodeScreen:
    SCREEN_SIZE = (1920, 1080)
    fourcc = cv2.VideoWriter_fourcc(*"XVID")
    today = date.today()
    file_name = today.strftime("%Y-%m-%d_screen")
    file_name += '.avi'
    out = cv2.VideoWriter("recode/" + file_name, fourcc, 25.0, (SCREEN_SIZE))

    def recode_screen(self):
        img = ImageGrab.grab()
        img_np = np.array(img)
        frame = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)
        self.out.write(frame)

    def __del__(self):
        self.out.release()
        cv2.destroyAllWindows()

