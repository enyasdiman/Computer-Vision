# -*- coding: utf-8 -*-
"""
Created on Tue Jul  5 16:38:00 2022

@author: enyasdiman
"""

import cv2

cap = cv2.VideoCapture("C:/Users/enyas/YOLO/red_panda_snow.mp4")

fourcc = cv2.VideoWriter_fourcc(*"XVID")
out = cv2.VideoWriter("flipped_red_pandas.avi", fourcc, 25, (640, 360))

while True:
    ret, frame = cap.read() #takes the frames
    #print(frame.shape)
    frame2 = cv2.flip(frame, 1) #can be 0 and 1
    
    cv2.imshow("flipping", frame2)
    cv2.imshow("frame", frame) #shows the frames
    
    out.write(frame2)
    
    key = cv2.waitKey(30) #milisaniye, latency
    if key == 27:
        break
    
out.release()
cap.release()
cv2.destroyAllWindows()