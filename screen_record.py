# record screen
import cv2
import numpy as np
from PIL import ImageGrab

SCREEN_SIZE = (1920, 1080)
fourcc = cv2.VideoWriter_fourcc(*"XVID")
out = cv2.VideoWriter("screen_record.avi", fourcc, 10.0, (SCREEN_SIZE))

while True:
    img = ImageGrab.grab()
    img_np = np.array(img)
    frame = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)
    out.write(frame)

    if cv2.waitKey(1) == ord("q"):
        break

out.release()
cv2.destroyAllWindows()