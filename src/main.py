import cv2
import numpy as np
import open_camera as opc
import record_video as rcv

def main():
    print("---OpenCV Test---")
    print("Select script to run:")
    # Functions
    print("1: Simple camera test.")
    print("2. Video Recording ")

    i = input("Select one: ")
    if i == "1":
        opc.open_camera()
    if i == "2":
        rcv.record_video()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
