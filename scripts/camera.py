import cv2
import numpy

def camera():
    camera = cv2.VideoCapture(0)
    ret,frame = camera.read()
    while ret:
        ret, frame = camera.read()
        cv2.imshow("camera", frame)
        if (cv2.waitKey(10) & 0xFF) == ord("q"):
            break
    camera.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    camera()
