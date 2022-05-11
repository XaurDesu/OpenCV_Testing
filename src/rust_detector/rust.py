import cv2
import numpy as np

# This function allows us to create a descending sorted list of contour areas.
def contour_area(contours):
    cnt_area = []
 
    for i in range(0,len(contours),1):
        cnt_area.append(cv2.contourArea(contours[i]))
 
    list.sort(cnt_area, reverse=True)
    return cnt_area

def draw_bounding_boxes(contours, image):
    cnt_area = contour_area(contours)
 
    for i in range(0,len(contours),1):
        cnt = contours[i]
        x,y,w,h = cv2.boundingRect(cnt)         
        image=cv2.rectangle(image,(x,y),(x+w,y+h),(0,0,255),2)
 
    return image

def rust_detector():
    
    vid = cv2.VideoCapture(0)
    
    while True:
        
        _,frame=vid.read()
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        lower = np.array([10, 100, 20])
        upper = np.array([20, 255, 200])

        mask = cv2.inRange(hsv, lower, upper)
        result = cv2.bitwise_and(frame, frame, mask=mask)

        contours,hierarchy = cv2.findContours(mask, 1, 2)
        bounding = draw_bounding_boxes(contours, frame)
        
        
        cv2.imshow("frame", frame)
        cv2.imshow("mask", mask)        
        cv2.imshow("result", result)


        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cv2.destroyAllWindows()

rust_detector()