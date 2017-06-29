import cv2
import numpy as np
from scipy import ndimage

kernel3 = np.array([[-1,-1,-1], [-1,8,-1], [-1,-1,-1]])
kernel5 = np.array([[-1,-1,-1,-1,-1],
                   [-1, 1, 2, 1,-1],
                   [-1, 2, 4, 2,-1],
                   [-1, 1, 2, 1,-1],
                   [-1,-1,-1,-1,-1]])

img = cv2.imread('../img/lufei2.jpg', 0)
k3 = ndimage.convolve(img, kernel3)
k5 = ndimage.convolve(img, kernel5)

blurred = cv2.GaussianBlur(img, (11,11), 0)
g_hpf = img - blurred

cv2.imshow('img', img)
cv2.imshow('3x3', k3)
cv2.imshow('5x5', k5)
cv2.imshow('g_hpt', g_hpf)
cv2.waitKey()
cv2.destroyAllWindows()
