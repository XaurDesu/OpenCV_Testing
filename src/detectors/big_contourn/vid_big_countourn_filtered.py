import cv2
import numpy as np

def detector():
    
    vid = cv2.VideoCapture('vids/GOPR6012_Trim2.mp4')

    while True:
        conts = 0

        _, img = vid.read()
        cv2.imshow('original', img)

        edges = cv2.Canny(img,50,90)
        cv2.imshow('canny', edges)

        contours, hierarchy= cv2.findContours(edges,
        cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        
        for x in contours:
            if cv2.contourArea(x) > 250:
                cv2.drawContours(img, x, -1, (0,255,0), 3)
                conts += 1

        cv2.imshow('original', img)
        print(conts)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    cv2.destroyAllWindows()

detector()