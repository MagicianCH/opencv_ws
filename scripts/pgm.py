import cv2
import numpy as np
import os

ba = bytearray(os.urandom(1000000))
for i in range(1000000):
    ba[i] = 240
na = np.array(ba)

grayImage = na.reshape(1000, 1000)
cv2.imwrite('../img/test.pgm', grayImage)
