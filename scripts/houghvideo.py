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
        #size = gray.shape
        #print(size)
        dst = cv2.Canny(gray, 50, 200)
        lines = cv2.HoughLinesP(dst, 1, math.pi/180.0, 100, np.array([]), 50, 20)
        if lines is None:
            continue
        num,b,c = lines.shape
        cnt = 0
        for i in range(num):
            for x1,y1,x2,y2 in lines[i]:
                if x1 != x2 and y1 > 200 and y2 > 200:
                    k = (y1-y2)/(x1-x2)
                    a = (math.atan(k)+math.pi) % math.pi 
                    if (a > math.radians(55)  and a < math.radians(75)) \
                       or (a > math.radians(105) and a < math.radians(125)):
                        cv2.line(frame, (x1,y1), (x2,y2), (0,0,255), 3)
                        cnt += 1
        cv2.imshow("img", frame) 
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break
    cv2.destroyAllWindows()
