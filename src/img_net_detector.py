import cv2 
import numpy as np

def detector():
    
    img = cv2.imread('OpenCV_Testing/badminton_net.jpg', cv2.IMREAD_GRAYSCALE)

    while True:
        cv2.imshow('original', img)

        edges = cv2.Canny(img,100,200)
        cv2.imshow('canny', edges)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cv2.destroyAllWindows()

detector()