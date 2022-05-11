import cv2
import numpy as np

def rust_detector():
    
    vid = cv2.VideoCapture(0)
    
    while True:
        
        _,frame=vid.read()
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        lower = np.array([10, 100, 20])
        upper = np.array([20, 255, 200])

        mask = cv2.inRange(hsv, lower, upper)
        result = cv2.bitwise_and(frame, frame, mask=mask)


        cv2.imshow("frame", frame)
        cv2.imshow("mask", mask)        
        cv2.imshow("result", result)


        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cv2.destroyAllWindows()

rust_detector()