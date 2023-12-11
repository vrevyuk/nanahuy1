import sys
import base64
from picamera2 import Picamera2, Preview
from picamera2.encoders import H264Encoder
from libcamera import ColorSpace
import time
import cv2

class PiCameraHandler:
    def __init__(self):
        picam2 = Picamera2()
        for mode in picam2.sensor_modes:
            print("MODE:", mode)

        camera_config = picam2.create_still_configuration(main={"format": "XRGB8888"}, buffer_count=2)
        #camera_config = picam2.create_still_configuration(lores={"size": (640, 480)})
        picam2.configure(camera_config)
        picam2.start()
        time.sleep(2)
        self.picam2 = picam2
        print("camera has been intialized")
        pass

    def release(self):
        pass

    def getFrames(self):
        while True:
            frame = self.picam2.capture_array()
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            # print(frame.shape) 1944, 2592
            frame = cv2.resize(frame, (864, 648))

            _, buffer = cv2.imencode(".png", frame)
            encodedBuffer = base64.b64encode(buffer)
            yield b'data:image/png;base64,' + encodedBuffer
