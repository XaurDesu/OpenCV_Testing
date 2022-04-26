import cv2
import numpy as np

def detector():
    cv2.destroyAllWindows()
    img = cv2.imread('vids/badminton_net.jpg', cv2.IMREAD_GRAYSCALE)
        
    cv2.imshow('original', img)

    edges = cv2.Canny(img,100,200)
        
    cv2.imshow('canny', edges)
    contours, hierarchy= cv2.findContours(edges.copy(), 
        cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    cv2.drawContours(img, contours, -1, (0, 255, 0), 2, cv2.LINE_AA)
        
    while True:
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

detector()