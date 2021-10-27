import cv2 as cv
import sys
import numpy as np
import matplotlib.pyplot as plt
import imageio
from time import sleep
from openpiv import tools, pyprocess, validation, filters, scaling

cap = cv.VideoCapture("./test_data_1/video/videoplayback.mp4")

if not cap.isOpened():
    print("Cannot open camera")
    exit()

for i in range(0, 1199, 1):
    ret, frame = cap.read()

    dosya_adi = "./test_data_2/" + "test_img_" + str(i) + ".bmp"

    cv.imshow("frame: ", frame)
    cv.imwrite(dosya_adi, frame)
    
    if (cv.waitKey(1) & 0xFF == ord("q")):
        cv.destroyAllWindows()
        print("Program Sonlandirildi.")
        break
cap.release()
cv.destroyAllWindows()
