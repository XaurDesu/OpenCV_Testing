import cv2
import numpy as np

def detector():
    img = cv2.imread('./vids/badminton_net.jpg', cv2.IMREAD_GRAYSCALE)
        
    cv2.imshow('original', img)

    edges = cv2.Canny(img,100,200)
        
    
    contours, hierarchy= cv2.findContours(edges.copy(), 
        cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    """
    https://docs.opencv.org/4.x/dd/d49/tutorial_py_contour_features.html

    contours = list(contours)
    for x in contours:
        if cv2.contourArea(x) < 300:
            contours.pop(x)
    contours = tuple(contours)
    """
    cv2.drawContours(img, contours, -1, (0, 255, 0), 2, cv2.LINE_AA)        


    while True:
        cv2.imshow('canny', edges)
        cv2.imshow('original', img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        
        cv2.destroyAllWindows()
    
detector()