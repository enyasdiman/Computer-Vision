# -*- coding: utf-8 -*-
"""
Created on Mon Jul 18 10:16:03 2022

@author: enyasdiman
"""

import cv2
import numpy as np

def nothing(x):
    pass

cap = cv2.VideoCapture(0)

cv2.namedWindow("frame")

cv2.createTrackbar("test", "frame", 50, 500, nothing)
cv2.createTrackbar("color/gray", "frame", 0, 1, nothing)

while True:
    _, frame = cap.read()
    
    test = cv2.getTrackbarPos("test", "frame")
    font = cv2.FONT_HERSHEY_COMPLEX()
    cv2.putText(frame, str(test), (50, 150), font, 4, (0,0,255))
    
    s = cv2.getRackbarPos("color/gray", "frame")
    if s == 0:
        pass
    else:
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    cv2.imshow("frame", frame)
    
    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()
