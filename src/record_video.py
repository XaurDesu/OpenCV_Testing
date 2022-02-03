import cv2
import os
import numpy

def record_video():

    namefile = input("Please, input the name of the output file: ")
    cap = cv2.VideoCapture(0)

    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    video_writer = cv2.VideoWriter((namefile+".avi"), fourcc, 25.0, (640, 480))

    while True:
        _, frame = cap.read()
        video_writer.write(frame)
        cv2.imshow('Video Stream', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    _.release()
    video_writer.release()
    cv2.destroyAllWindows()