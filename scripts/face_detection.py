import cv2
import numpy

def detect():
    face_cascade = cv2.CascadeClassifier('../data/haarcascades/haarcascade_frontalface_default.xml')
    camera = cv2.VideoCapture(0)

    ret,frame = camera.read()

    while ret:
        ret,frame = camera.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        for (x,y,w,h) in faces:
            cv2.rectangle(frame, (x,y),(x+w, y+h), (255,0,0))
            
        cv2.imshow("camera", frame)
        if cv2.waitKey(10) & 0xff == ord("q"):
            break

    camera.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    detect()
