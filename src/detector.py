import cv2 
import numpy as np

def detector():
    cap = cv2.VideoCapture('.fish_practice_video_12.mp4')
    
        
    if not cap.isOpened():
        print("Cannot open camera")
        exit()

    while True:
        _, img = cap.read()
        
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        blur = cv2.blur(gray,(5,5))

        edges = cv2.Canny(blur,100,200)
        cv2.imshow("100-200", edges)


cv2.destroyAllWindows()