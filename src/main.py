import cv2
import numpy as np
import open_camera as opc
import record_video as rcv
import color_filter as clf

def main():
    print("---OpenCV Test---")
    print("Select script to run:")
    # Functions
    print("1: Simple camera test.")
    print("2. Video Recording ")
    print("3. Color Filter")
    print("0. Quit")

    i = input("Select one: ")
    if i == "1":
        opc.open_camera()
        main()

    elif i == "2":
        rcv.record_video()
        main()

    elif i == "3":
        clf.color_filter()
        main()

    elif i == "0":
        pass

if __name__ == '__main__':
    main()
