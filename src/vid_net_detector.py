import cv2 
import numpy as np

def detector():
    vid = cv2.VideoCapture('OpenCV_Testing/fishnet.mp4')
    
    while True:
        _, img = vid.read()
        cv2.imshow('original', img)

        edges = cv2.Canny(img,75,140)
        cv2.imshow('canny', edges)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    

    cv2.destroyAllWindows()

detector()