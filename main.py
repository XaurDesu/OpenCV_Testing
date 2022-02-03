# This is a sample Python script.
import cv2
import numpy as np
# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def main():
    print("---OpenCV Test---")

    cap=cv2.VideoCapture(0)
    while True:
        _, frame = cap.read()

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        threshole = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

        mean = cv2.blur()

        #
        #
        #
        cv2.imshow('frame', frame)
        cv2.imshow("gray", gray)
        cv2.imshow("mean", mean)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
