import cv2
import numpy as np

capture = cv2.VideoCapture(0)

while True:
    ret, frame = capture.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    features = cv2.goodFeaturesToTrack(gray, 100, 0.5, 10)
    
    if hasattr(features, '__iter__'):
        features = np.int0(features)
        for feature in features:
            x, y = feature.ravel()
            cv2.circle(frame, (x, y), 5, (0, 0, 255), 1)

    cv2.imshow("Capture", frame)

    if cv2.waitKey(1) == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()