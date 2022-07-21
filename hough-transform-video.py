# -*- coding: utf-8 -*-
"""
Created on Thu Jul 21 14:34:56 2022

@author: enyasdiman
"""

import cv2
import numpy as np

video = cv2.VideoCapture("C:/Users/enyas/YOLO/red_panda_snow.mp4")

while True:
    ret, frame = video.read()
    gray = cv2.cvtColor()
    
    if not ret:
        video = cv2.VideoCapture("C:/Users/enyas/YOLO/red_panda_snow.mp4")
        continue
    
    cv2.imshow("frame", frame)
    
    key = cv2.waitKey(25)
    
    if key == 27:
        break

video.release()
cv2.destroyAllWindows()
    