import sys
import cv2
import base64

class CameraHandler:
    def __init__(self):
        self.__capture = cv2.VideoCapture(0)
        print("camera", self.__capture)
        pass

    def release(self):
        self.__capture.release()
        pass

    def getFrames(self):
        while True:
            success, frame = self.__capture.read()
            print("getFrame", success, frame)
            if success:
                frame = cv2.resize(frame, (0, 0), fx=0.3, fy=0.3)

                _, buffer = cv2.imencode(".png", frame)
                encodedBuffer = base64.b64encode(buffer)
                yield b'data:image/png;base64,' + encodedBuffer
            else:
                sys.exit(1)
