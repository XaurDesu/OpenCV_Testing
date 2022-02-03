import cv2
import numpy as np

def open_camera():
    cap = cv2.VideoCapture(0)
    while True:
        _, frame = cap.read()
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cv2.destroyAllWindows()