# -*- coding: utf-8 -*-
"""
Created on Tue Jul  5 16:38:00 2022

@author: enyasdiman
"""

import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read() #takes the frames
    gray_scale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #convert gray
    
    cv2.imshow("gray scale", gray_scale) #shows the frames
    cv2.imshow("frame", frame) #shows the frames
    
    key = cv2.waitKey(1) #milisaniye, latency
    if key == 27:
        break
    
cap.release()
cv2.destroyAllWindows()