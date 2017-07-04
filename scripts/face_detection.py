import cv2
import numpy
import serial
import struct 

def handle_direction(x,y, s):
    print("x:%d, y:%d" % (x, y))
    if(x < 280):
        print('you must turn left')
        data = struct.pack('B', 2)
        s.write(data)
    elif x > 360:
        print('you must turn right')
        data = struct.pack('B', 1)
        s.write(data)
    else:
        data = struct.pack('B', 3)
        s.write(data)
        print('you just stay there')

def detect(ser):
    face_cascade = cv2.CascadeClassifier('../data/haarcascades/haarcascade_frontalface_default.xml')
    camera = cv2.VideoCapture(0)

    ret,frame = camera.read()

    while ret:
        ret,frame = camera.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        for (x,y,w,h) in faces:
            cv2.rectangle(frame, (x,y),(x+w, y+h), (255,0,0))
            x = int(x+w/2)
            y = int(y+h/2)
            handle_direction(x, y, ser)
            
        cv2.imshow("camera", frame)
        if cv2.waitKey(100) & 0xff == ord("q"):
            break

    camera.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    servo = serial.Serial('/dev/ttyACM0', 115200)
    detect(servo)
