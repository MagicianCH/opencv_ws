import cv2
import numpy as np
from urllib.request import urlopen

#resp = urlopen("http://image.tianjimedia.com/uploadImages/2014/287/52/N0E668O0PEF5.jpg")
while True:
    resp = urlopen("http://localhost:8081")
    frame = np.asarray(bytearray(resp.read()), dtype="uint8")
    frame = cv2.imdecode(frame, cv2.IMREAD_COLOR)
    cv2.imshow("image", frame)
    if cv2.waitKey(100):
        break
