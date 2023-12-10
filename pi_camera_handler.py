import sys
import base64
from picamera2 import Picamera2, Preview
import time
import cv2

class PiCameraHandler:
    def __init__(self):
        self.picam2 = Picamera2()
        camera_config = self.picam2.create_preview_configuration()
        self.picam2.configure(camera_config)
        # self.picam2.start_preview(Preview.DRM)
        self.picam2.start()
        time.sleep(2)
        pass

    def release(self):
        pass

    def getFrames(self):
        while True:
            frame = self.picam2.capture_buffer()
            print("frame_picam", frame)
            frame = cv2.resize(frame, (0, 0), fx=0.3, fy=0.3)

            _, buffer = cv2.imencode(".png", frame)
            encodedBuffer = base64.b64encode(buffer)
            yield b'data:image/png;base64,' + encodedBuffer
