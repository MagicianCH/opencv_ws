'''
houghlinesP from camera frame
'''

# Python 2/3 compatibility
from __future__ import print_function

import cv2
import numpy as np
import sys
import math

if __name__ == '__main__':
    print(__doc__)

    camera = cv2.VideoCapture(0)

    while True:
        ret,frame = camera.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        dst = cv2.Canny(gray, 50, 200)
        lines = cv2.HoughLinesP(dst, 1, math.pi/180.0, 100, np.array([]), 50, 20)
        if lines is None:
            continue
        a,b,c = lines.shape
        for i in range(a):
            for x1,y1,x2,y2 in lines[i]:
                if math.fabs(x1-x2) < math.fabs(y1-y2): 
                    cv2.line(frame, (x1,y1), (x2,y2), (0,0,255), 3)
        cv2.imshow("img", frame) 
        cv2.waitKey()
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break
    cv2.destroyAllWindows()

