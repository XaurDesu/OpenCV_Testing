import cv2
import numpy as np

def rust_detector():
    
    vid = cv2.VideoCapture('vids\GOPR6012_Trim1.mp4')
    

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    lower = np.array([10, 100, 20])
    upper = np.array([20, 255, 200])

    mask = cv2.inRange(hsv, lower, upper)
    cv2.imshow("frame", vid)
    cv2.imshow("mask", mask)
    
    

    cv2.destroyAllWindows()