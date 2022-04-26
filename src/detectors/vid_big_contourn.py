import cv2
import numpy as np

def detector():
    
    
    vid = cv2.imread('vids/REC00032.AVI', cv2.IMREAD_GRAYSCALE)

    while True:
        
        _, img = vid.read()
        cv2.imshow('original', img)

        edges = cv2.Canny(img,50,90)
        cv2.imshow('canny', edges)

        contours, hierarchy= cv2.findContours(edges.copy(), 
            cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        
        cv2.drawContours(img, contours, -1, (0, 255, 0), 2, cv2.LINE_AA)

        break
    
    cv2.destroyAllWindows()
detector()