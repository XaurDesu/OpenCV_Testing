import cv2 
import numpy as np

def detector():
    vid = cv2.VideoCapture('Gopro1.mp4')
    
    while True:
        _, img = vid.read()
        cv2.imshow('original', img)

        edges = cv2.Canny(img,50,90)
        cv2.imshow('canny', edges)

        contours, hierarchy= cv2.findContours(edges.copy(), 
            cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

        print(len(contours))
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    

    cv2.destroyAllWindows()

detector()